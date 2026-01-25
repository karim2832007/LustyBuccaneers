# Version event: 1
# Version game: 0.23

label fight_screen_skills():
    show screen screen_alpha_choice_lock  # Bloquea la UI durante la selección

    python:
        list_skills = []
        active_skills_map = []
        for ability_name, condition in player_abilities:

            if eval(condition):
                ability = ABILITIES.get(ability_name, None)
                if ability and ability.mana_cost <= player_mana:
                    list_skills.append(f"{ability.name} | -{ability.mana_cost} SP")
                    active_skills_map.append(ability_name)

        list_skills.append("Run") 
        list_skills.append("Back") 

    call screen choice_list(list_skills)

    #$ print("choice_id: " + str(choice_id))
    #$ print("len list_skills: " + str(len(list_skills)))

    $ player_action = "none"
    #$ selected_skill_key = None

    # "run" 
    if choice_id == len(list_skills)-2:

        hide screen screen_alpha_choice_lock
        if no_run:
            narrador "There is no escape from this fight."
        else:
            $ player_action = "run"

    # "back"
    elif choice_id == len(list_skills)-1:
        hide screen screen_alpha_choice_lock

    else:
        $ player_action = "skill"
        $ choice_id = active_skills_map[choice_id]
        hide screen screen_alpha_choice_lock

    return player_action, choice_id


screen skill_effect(effect_image):
    zorder -20  # Asegura que esté por encima de todo
    add effect_image:
        xalign 0.0
        yalign 0.35
    #timer 1.5 action Hide("skill_effect")  # Se oculta tras 0.5 segundos

screen skill_effect_player(effect_image):
    zorder -20  # Asegura que esté por encima de todo
    add effect_image:
        xalign 1.0
        yalign 0.35