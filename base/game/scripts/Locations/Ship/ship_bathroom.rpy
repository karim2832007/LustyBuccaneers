# Version event: 1
# Version game: 0.37

default ship_bathroom = False

label ship_bathroom():
    if ship_bathroom:
        call m_ship_bathroom_event from _call_m_ship_bathroom_event

    $ _window_hide()
    show screen screen_black with Dissolve(0.6)

    $ ui_interface = True
    $ game.location = "ship_bathroom"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)

    $ ambient_ship()
    $ music_time_day()
    
    if ship_bathroom:
        call m_ship_bathroom from _call_ship_bathroom
    else:
        call m_ship_bathroom_repair from _call_ship_bathroom_repair


label m_ship_bathroom_event():
    if renpy.random.choice([True, True, True, False]):
        if renpy.random.choice([True, False]):
            menu:
                narrador "It looks like there’s someone in the bathroom since the light is on, It seems to be [robin.n]. Do you want to go in anyway?"
                "Yes":
                    jump robin_undressing
                "No":
                    jump m_ship_rooms

        else:
            menu:
                narrador "It looks like there’s someone in the bathroom since the light is on, It seems to be [nami.n]. Do you want to go in anyway?"
                "Yes":
                    jump nami_bathroom
                "No":
                    jump m_ship_rooms
        
    return

label m_ship_bathroom():
    menu:
        "Back":
            jump ship_mid


label m_ship_bathroom_repair():
    menu:
        "Repair the bathroom" if not game.clock.night:
            menu:
                narrador "Requires: 10 wood, 4 iron and 300 [Berries.n]"
                "Yes":
                    if wood >= 10 and iron >= 4 and berries >= 300:
                        $ wood -= 10
                        $ iron -= 4
                        $ berries -= 300

                        play sound "repair"
                        $ ship_bathroom = True

                        $ _window_hide()
                        with t_black
                        $ game.clock.next()
                        
                        jump m_ship_bathroom

                    else:
                        narrador "Insufficient resources"
                "No":
                    pass
            
            jump m_ship_bathroom_repair

        "Back":
            jump ship_mid