# Version event: 1
# Version game: 0.22

default ar_rebel_army = False

label ar_katorea():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True
    $ game.location = "ar_katorea"
    $ arabasta_location = "Katorea"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_katorea

label m_ar_katorea():

    if Arabasta.h <= 13 and not ar_rebel_army:
        jump ar_nanohana_h

    
    menu:
        "Map" if map_arabasta and not game.clock.night:
            jump map_arabasta

        "Back":
            jump arabasta

