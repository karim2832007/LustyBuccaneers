# Version event: 2
# Version game: 0.39

default active_animations = {}

init -1 python:
    import time

    # Agregamos obj_ref=None al final
    def update_stat_logic(stat_name, start_val, target_val, start_time, duration, obj_ref=None):
        global_vars = globals()
        
        current_time = time.time()
        elapsed = current_time - start_time
        progress = elapsed / duration
        
        # Lógica de finalización
        if progress >= 1.0:
            if obj_ref:
                # Si es un objeto (enemigo), usamos setattr
                setattr(obj_ref, stat_name, int(target_val))
            else:
                # Si es global (jugador), usamos globals()
                global_vars[stat_name] = int(target_val)
                
            renpy.end_interaction(True) 
            return

        # Matemática (Easing)
        ease_progress = 1 - (1 - progress) ** 2
        total_change = target_val - start_val
        new_val = start_val + (total_change * ease_progress)
        
        # Actualización de variable
        if obj_ref:
            setattr(obj_ref, stat_name, int(new_val))
        else:
            global_vars[stat_name] = int(new_val)
        
        renpy.restart_interaction()

    # --- FUNCIÓN PARA LLAMAR DESDE TU JUEGO ---
    def animate_bar(stat_name, min_value, max_value, change, obj_ref=None):
        global_vars = globals()
        
        # Detectar valor actual
        if obj_ref:
            # Leemos del objeto (ej: enemy.hp)
            current = getattr(obj_ref, stat_name, 0)
        else:
            # Leemos global (ej: player_hp)
            current = global_vars.get(stat_name, 0)

        final_target = max(min_value, min(max_value, current + change))
        real_change = final_target - current
        
        if real_change == 0:
            return

        # Pasamos obj_ref a la pantalla también
        renpy.call_screen("blocking_animator", stat_name=stat_name, change=real_change, obj_ref=obj_ref)


    def animate_bar_background(stat_name, min_value, max_value, change):
        """Prepara la animación para que corra en segundo plano."""
        global_vars = globals()
        
        if stat_name not in global_vars:
            return

        current_value = global_vars[stat_name]
        target_value = max(min_value, min(max_value, current_value + change))
        
        # Si ya estamos en el valor, no hacemos nada
        if current_value == target_value:
            return

        # Definimos la velocidad - ajustable 50 mientras mas alto sea mas lenta la animacion
        step = (target_value - current_value) / 50.0 
        
        # Agregamos a la cola de animaciones
        active_animations[stat_name] = {
            "target": target_value,
            "current": float(current_value), # Usamos float para suavidad interna
            "step": step
        }
        
        # Activamos la pantalla encargada de procesar esto si no está activa
        if not renpy.get_screen("background_animator"):
            renpy.show_screen("background_animator")

    def process_animations():
        """Esta función se llama muchas veces por segundo por la screen."""
        global_vars = globals()
        to_remove = []

        for stat, data in active_animations.items():

            # --- SEGURIDAD ANTI-CRASH ---
            # Si cargamos un save viejo y esta variable ('stat') ya no existe en el juego,
            # marcamos para borrar y saltamos al siguiente.
            if stat not in global_vars:
                to_remove.append(stat)
                continue

            # Actualizamos el valor interno
            data["current"] += data["step"]
            
            # Verificamos si llegamos (o nos pasamos)
            reached = False
            if data["step"] > 0 and data["current"] >= data["target"]:
                data["current"] = data["target"]
                reached = True
            elif data["step"] < 0 and data["current"] <= data["target"]:
                data["current"] = data["target"]
                reached = True
            
            # Aplicamos el cambio a la variable real (como entero si tus stats son ints)
            global_vars[stat] = int(data["current"])
            
            if reached:
                to_remove.append(stat)
        
        # Limpiamos las animaciones terminadas
        for stat in to_remove:
            del active_animations[stat]
            
        # Si no queda nada por animar, ocultamos la pantalla para ahorrar recursos
        if not active_animations:
            renpy.hide_screen("background_animator")
            
        # Forzamos a Ren'Py a refrescar las pantallas para ver los cambios
        renpy.restart_interaction()

    def finish_background_animations():
        """
        Finaliza inmediatamente todas las animaciones activas, 
        estableciendo las variables en su valor objetivo (target).
        """
        global_vars = globals()
        
        # Si no hay animaciones, no hacemos nada
        if not active_animations:
            return

        # Recorremos todas las animaciones pendientes
        for stat, data in active_animations.items():
            target_val = int(data["target"]) # Aseguramos que sea entero, igual que en tu lógica original
            
            # Aplicamos el valor final directamente a la variable global
            if stat in global_vars:
                global_vars[stat] = target_val
        
        # Limpiamos el diccionario de animaciones porque ya se completaron
        active_animations.clear()
        
        # Ocultamos la pantalla del timer
        renpy.hide_screen("background_animator")
        
        # Refrescamos para asegurar que las barras se vean llenas
        renpy.restart_interaction()


# Esta pantalla es invisible y actúa como el "motor" detrás de escena
screen background_animator():
    # El timer repite la acción cada 0.02 segundos (aprox 50 FPS)
    timer 0.02 repeat True action Function(process_animations)



screen blocking_animator(stat_name, change, duration=1.5, obj_ref=None):
    modal True 
    
    # Lógica híbrida para encontrar el valor inicial
    default start_val = getattr(obj_ref, stat_name) if obj_ref else globals()[stat_name]
    
    default target_val = start_val + change
    default start_time = time.time()
    
    # Pasamos obj_ref a la función lógica
    timer 0.016 repeat True action Function(
        update_stat_logic, 
        stat_name, 
        start_val, 
        target_val, 
        start_time, 
        duration,
        obj_ref   # <--- Importante pasarlo aquí
    )

    # Nota: No necesitamos UI visual aquí, se asume que tu HUD lee la variable global.