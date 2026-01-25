# Version event: 1
# Version game: 0.23

label fight_items():
    show screen screen_alpha_choice_lock

    menu m_fight_items:
        "Food{space=140}+50hp":
            hide screen screen_alpha_choice_lock

            if RPGPlayer.hp() == RPGPlayer.true_hp_max():

                $ talk_random = renpy.random.choice([
                        _("You're in full health"),
                        _("No healing needed"),
                    ])

                narrador "[talk_random]"

                call fight_items from _call_fight_items_fullhp
                return

            elif food <= 0:

                $ talk_random = renpy.random.choice([
                        _("You don't have enough Food!"),
                        _("You need more Food!"),
                    ])

                narrador "[talk_random]"

                call fight_items from _call_fight_items_nofood
                return

            $ food -= 1
            $ talk_random = RPGPlayer.heal()

            #$ talk_random = renpy.random.choice([
            #        _("You have been healed!"),
            #        _("You have recovered!"),
            #    ])

            narrador "[talk_random]"

        "Back":
            hide screen screen_alpha_choice_lock
            call screen s_fight with Dissolve(0.5)
            
    return