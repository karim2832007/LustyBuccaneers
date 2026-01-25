# Version event: 1
# Version game: 0.10

label amazon_lily_city():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "amazon_lily_city"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    play ambient "market" fadein 1.0
    $ music_amazonlily()
    
    jump m_amazon_lily_city

label m_amazon_lily_city():
    menu:
        "Go to the Palace":
            jump amazon_lily_palace
        
        "Back":
            jump amazon_lily