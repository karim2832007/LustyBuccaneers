# Version event: 1
# Version game: 0.23

default player_turn = True
default player_action = "none"
default player_skill = "none"
default player_item = "none"
default action_id = 0

label fight_round():
    while True:
        $ player_turn = True
        $ player_guard = False
        $ player_action = "none"

        # Player Turn
        while player_action == "none":
            call screen s_fight
            $ player_action, action_id = _return
            #$ print(f"player_action: {player_action}")


        $ player_turn = False
        if player_action == "attack":
            call fight_attack from _call_fight_attack_round

        elif player_action == "guard":
            call fight_guard from _call_fight_guard_round

        elif player_action == "run":
            if RPGPlayer.run():
                call fight_run from _call_fight_run
                return
            else:
                narrador "You couldn't escape."

        elif player_action == "skill":
            call fight_skills from _call_fight_skills_round

        elif player_action == "heal":
            call fight_heal from _call_fight_heal_round


        hide screen skill_effect_player with Dissolve(0.3)

        # check enemy health
        if enemy_figth.is_dead():
            $ talk_random = renpy.random.choice([
                    _("You have won the fight!"),
                    _("Victory!!"),
                ])

            narrador "[talk_random]"
            
            call fight_win from _call_fight_win
            return

        # ------------------------- Enemy turn -------------------------
        $ talk, action_type, details = enemy_figth.decide_action()


        if action_type == "attack":
            if details.get("image"):
                show screen skill_effect(details.get("image")) with Dissolve(0.3)

            narrador "[talk]"

            if RPGPlayer.dodge(enemy_figth.agility):
                $ talk = "You dodged the attack!"

            else:
                if details.get("crit_attack"):
                    narrador "A CRITICAL HIT!"

                $ talk = RPGPlayer.take_damage(damage=details["damage"], damage_type=details["damage_type"])

        #elif action_type == "heal":
        #    narrador "[talk]"
        #
        #elif action_type == "buff":
        #    narrador "[talk]"
        #    # 📌 Aquí podrías aplicar el buff al enemigo
        #
        #elif action_type == "defend":
        #    narrador "[talk]"
        #    # 📌 Aquí podrías activar la defensa del enemigo

        # Mostrar narración general
        narrador "[talk]"

        hide screen skill_effect with Dissolve(0.3)

        # 📌 Verificar si el jugador ha muerto después de la acción del enemigo
        if RPGPlayer.is_dead():
            call fight_died from _call_fight_died
            return
        
    return

#gCharacter(enemy_img) "Ya vas a ver"
