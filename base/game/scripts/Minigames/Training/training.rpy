# Version event: 2
# Version game: 0.36

screen s_miniGameWeight(gameWeight = v_miniGameWeight):
    add gameWeight

init python:
    class MinigameWeightBarHorizontal(renpy.Displayable):
        def __init__(self, xpos, ypos, width=400, height=50, **kwargs):
            super(MinigameWeightBarHorizontal, self).__init__(**kwargs)
            self.imgBack = renpy.displayable("minigames training bar_yamato_back")
            self.imgGreen = renpy.displayable("minigames training bar_yamato_green")
            self.imgYellow = renpy.displayable("minigames training bar_yamato_yellow")
            self.imgRed = renpy.displayable("minigames training bar_yamato_red")

            self.x = xpos 
            self.y = ypos
            self.width = width
            self.height = height
            self.progress = 100

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)

            # Renderizar fondo
            render.place(self.imgBack, x=self.x, y=self.y)

            # Calcular ancho de la barra según progreso
            bar_width = int((self.progress * self.width) / 100)

            # Elegir color según progreso
            if self.progress >= 70:
                imgBar = Crop((0, 0, bar_width, self.height), self.imgGreen)
            elif self.progress >= 30:
                imgBar = Crop((0, 0, bar_width, self.height), self.imgYellow)
            else:
                imgBar = Crop((0, 0, bar_width, self.height), self.imgRed)
    
            render.place(imgBar, x=self.x, y=self.y)

            renpy.redraw(self, .0)
            return render

        def visit(self):
            return [self.imgBack, self.imgGreen, self.imgYellow, self.imgRed]

    class MinigameWeightBarVertical(renpy.Displayable):
        def __init__(self, xpos, ypos, **kwargs):
            super(MinigameWeightBarVertical, self).__init__(**kwargs)
            self.imgBack = renpy.displayable("minigames training bar_player_back")
            self.imgGreen = renpy.displayable("minigames training bar_player_green")
            self.imgYellow = renpy.displayable("minigames training bar_player_yellow")
            self.imgRed = renpy.displayable("minigames training bar_player_red")

            self.x = xpos 
            self.y = ypos


            self.progress = 100

        def render(self, width, height, st, at):
            render = renpy.Render(50, 768)

            # Renderizar fondo
            render.place(self.imgBack, x=self.x, y=self.y)

            nCrop = int(((100 - self.progress) * 768) / 100)

            if self.progress >= 70:
                imgCrop = Crop((0, nCrop, 50, 768 - nCrop), self.imgGreen)
            elif self.progress >= 30:
                imgCrop = Crop((0, nCrop, 50, 768 - nCrop), self.imgYellow)
            else:
                imgCrop = Crop((0, nCrop, 50, 768 - nCrop), self.imgRed)
    
            render.place(imgCrop, x=self.x, y=self.y + nCrop)

            renpy.redraw(self, .0)
            return render

        def visit(self):
            return [ self.img ]

    class MinigameWeight(renpy.Displayable):
        def __init__(self, yamato_duration=15.0, weight=50, **kwargs):
            super(renpy.Displayable, self).__init__(**kwargs)

            #self.training_background = renpy.displayable("minigames training training_run")
            
            # Barra horizontal de Yamato
            screen_center_x = 1920 // 2 
            bar_yamato_width = 800
            yamato_x = screen_center_x - (bar_yamato_width // 2)
            self.barYamato = MinigameWeightBarHorizontal(xpos=yamato_x, ypos=50, width=bar_yamato_width, height=50)

            # Label Yamato
            self.yamato_label = Transform( 
            Text(
                "{size=35}{color=#ffffff}[yamato_name]{/color}{/size}",
                substitute=True,                 # habilita la interpolación [ ... ]
                scope=renpy.store.__dict__,      # para que encuentre 'yamato' en el store
            ),
            xpos=screen_center_x,
            ypos=100,                         # 8 px por encima de la barra
            anchor=(0.5, 1.0)
            )
            
            # Barra vertical del jugador 
            self.barPlayer = MinigameWeightBarVertical(xpos=50, ypos=156)
            
            # Variables del juego
            self.yamato_duration = yamato_duration  # Duración en segundos
            self.weight = weight  # Peso del objeto
            self.player_strength = Strength  # Variable global de fuerza
            
            # Estado del juego
            self.player_resistance = 100.0
            self.yamato_resistance = 100.0
            self.elapsed_time = 0.0
            self.click_boost = 0.0  # Boost temporal por click
            
            # Control de oscilación de Yamato
            self.yamato_struggle_timer = 0.0
            self.yamato_struggle_phase = 0  # 0: bajando, 1: subiendo un poco
            
            # Timer
            self.last_time = time.time()
            self.delta_time = 0

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            current_time = time.time()
            self.delta_time = current_time - self.last_time
            self.last_time = current_time
            
            # Actualizar juego
            self.run()
            
            # Actualizar barras
            self.barYamato.progress = max(0, min(100, self.yamato_resistance))
            self.barPlayer.progress = max(0, min(100, self.player_resistance))
            
            # Render
            #render.place(self.training_background)
            render.place(self.barYamato)
            render.place(self.yamato_label)
            render.place(self.barPlayer)

            renpy.redraw(self, .0)
            return render

        def calculate_drop_rate(self):
            """
            Calcula qué tan rápido cae la barra del jugador basado en:
            - Peso del objeto
            - Fuerza del jugador (strength)
            - Fatiga acumulada (tiempo transcurrido)
            
            Fórmula inspirada en: damage * (100 / (100 + armor))
            Aquí: weight * (100 / (100 + strength)) * fatiga_multiplicador
            """
            # Multiplicador base por peso (reducido por strength)
            base_drop = self.weight * (100.0 / (100.0 + self.player_strength))
            
            # Multiplicador de fatiga que aumenta con el tiempo
            # Empieza en 1.0 y puede llegar hasta 3.0 en ~15 segundos
            max_fatigue = 7.0
            fatigue_growth_rate = (max_fatigue - 1.0) / 12.0
            fatigue_multiplier = 1.0 + (self.elapsed_time * fatigue_growth_rate)
            fatigue_multiplier = min(fatigue_multiplier, max_fatigue)
            
            # Drop rate final (ajustado para ~15 segundos de juego)
            final_drop = (base_drop * fatigue_multiplier) / 3.5
            
            return final_drop

        def calculate_click_boost(self):
            """
            Calcula cuánto sube la barra por cada click
            Basado en la fuerza del jugador pero con un máximo
            """
            # Base boost 
            base_boost = 8.0 + (self.player_strength * (12.0 / (100.0 + self.player_strength * 0.5)))
            
            # Máximo boost para evitar spam excesivo
            return min(base_boost, 20.0)

        def update_yamato(self):
            """
            Actualiza la barra de Yamato con oscilaciones para simular esfuerzo
            """
            # Yamato pierde resistencia constantemente
            yamato_drop_rate = (100.0 / self.yamato_duration)  # Baja uniformemente
            
            self.yamato_struggle_timer += self.delta_time
            
            # Fase de lucha: baja más rápido, luego sube un poco
            if self.yamato_struggle_phase == 0:  # Bajando
                self.yamato_resistance -= yamato_drop_rate * self.delta_time * 1.3
                
                if self.yamato_struggle_timer >= 1.2:  # Cada 1.2 segundos cambia de fase
                    self.yamato_struggle_phase = 1
                    self.yamato_struggle_timer = 0.0
                    
            else:  # Subiendo un poco (recuperación)
                self.yamato_resistance += yamato_drop_rate * self.delta_time * 0.4
                
                if self.yamato_struggle_timer >= 0.3:  # Sube por 0.3 segundos
                    self.yamato_struggle_phase = 0
                    self.yamato_struggle_timer = 0.0

        def run(self):
            self.elapsed_time += self.delta_time
            
            # Actualizar Yamato
            self.update_yamato()
            
            # Calcular caída del jugador
            drop_rate = self.calculate_drop_rate()
            
            # Aplicar caída y boost por clicks
            self.player_resistance -= drop_rate * self.delta_time
            
            # Aplicar boost si hay clicks recientes (decae rápidamente)
            if self.click_boost > 0:
                boost_amount = self.click_boost * self.delta_time * 10  # Aplica el boost rápidamente
                self.player_resistance += boost_amount
                self.click_boost -= boost_amount
                
                if self.click_boost < 0:
                    self.click_boost = 0
            
            # Limitar valores
            self.yamato_resistance = max(0, min(100, self.yamato_resistance))
            self.player_resistance = max(0, min(100, self.player_resistance))
            
            # Condiciones de victoria/derrota
            if self.yamato_resistance <= 0 and self.player_resistance > 0:
                renpy.music.stop("sound", 0.5)
                self.win()
            elif self.player_resistance <= 0:
                renpy.music.stop("sound", 0.5)
                self.gameOver()

        def gameOver(self):
            renpy.jump("training_gameover")

        def win(self):
            renpy.jump("training_win")

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                # Calcular boost por click
                boost = self.calculate_click_boost()
                self.click_boost += boost
                
                # Sonido de click (opcional)
                # renpy.sound.play("click_sound", "sound")
                
            return None


default v_miniGameWeight = MinigameWeight(yamato_duration=15.0, weight=40)