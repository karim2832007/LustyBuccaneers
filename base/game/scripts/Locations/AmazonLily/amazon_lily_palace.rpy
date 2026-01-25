# Version event: 1
# Version game: 0.10

label amazon_lily_palace():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "amazon_lily_palace"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_amazonlily()
    
    jump m_amazon_lily_palace

label m_amazon_lily_palace():
    menu:
        "Go to the Empress Room":
            jump al_palace_room
        
        "Back":
            jump amazon_lily_city