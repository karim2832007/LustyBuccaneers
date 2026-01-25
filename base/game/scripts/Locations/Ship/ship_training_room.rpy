# Version event: 5
# Version game: 0.3

default ship_training_room = False

label ship_training_room():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ ui_interface = True
    $ game.location = "ship_training_room"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_time_day()
    
    call m_ship_training_room from _call_ship_training_room


label m_ship_training_room():
    if ship_training_room:
        $ ui_strength = True
        menu:
            "Training with Yamato" if not game.clock.night:
                jump event_yamato_training

            "Train Strength" if not game.clock.night:
                if Strength >= 10 * player_level:
                    narrador "You've reached the strength limit for your current level."
                    jump m_ship_training_room

                $ Strength += 1
                narrador "Strength +1"

                $ game.clock.next()
                jump m_ship_training_room

            "Take [yamato.n]'s panties" if Haki.h == 5 and not haki_yamato_panties:
                $ ui_strength = False
                jump haki_h5_yamato

            "Back":
                $ ui_strength = False
                jump ship_mid
    else:
        menu:
            "Repair the Training Room" if not game.clock.night:
                menu:
                    narrador "Requires: 8 wood, 4 iron and 200 [Berries.n]"
                    "Yes":
                        if wood >= 8 and iron >= 4 and berries >= 200:
                            $ wood -= 8
                            $ iron -= 4
                            $ berries -= 200

                            play sound "repair"
                            $ ship_training_room = True

                            window hide
                            with t_black
                            window auto
                            $ game.clock.next()
                            jump m_ship_training_room 
                        else:
                            narrador "Insufficient resources"
                    "No":
                        pass
                
                jump m_ship_training_room

            "Back":
                jump ship_mid
