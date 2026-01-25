label fight_screen_heal():
    show screen screen_alpha_choice_lock  # Bloquea la UI durante la selección

    python:
        valid_heals = []  # Lista para mapear el action_id con las opciones correctas
        
        for heal in HEALS:
            item_name = heal["item"]
            
            # Si el jugador tiene al menos 1 unidad del ítem, se agrega la opción
            if globals()[item_name] > 0:
                valid_heals.append(f"{heal['name']}"+ " | " + f"+{heal['heal_amount']} hp")
                #list_skills.append(f"{ability.name} - {ability.mana_cost} SP") --- {space=140}

        valid_heals.append("Back") 

    call screen choice_list(valid_heals)

    $ player_action = "heal" 

    # Si elige "Back", no hace nada
    if choice_id == len(valid_heals) -1:
        $ player_action = "none"

    elif player_hp >= RPGPlayer.true_hp_max():
        $ talk_random = renpy.random.choice([
                _("You're in full health"),
                _("No healing needed"),
            ])

        $ player_action = "none"
        hide screen screen_alpha_choice_lock
        narrador "[talk_random]"

    hide screen screen_alpha_choice_lock
    return player_action, choice_id  # Devolvemos el action_id correcto
