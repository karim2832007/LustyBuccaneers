# Version event: 1
# Version game: 0.23

label ar_alubarna_palace():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True
    $ game.location = "ar_alubarna_palace"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_alubarna_palace

label m_ar_alubarna_palace():
    
    menu:
        "Go to Room" if not game.clock.night:
            jump ar_alubarna_palace_room

        "Back":
            jump ar_alubarna

