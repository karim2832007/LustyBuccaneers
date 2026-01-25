# Version event: 2
# Version game: 0.9

label di_castle_mid():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "di_castle_mid"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ music_drumisland()
    jump m_di_castle_mid

label m_di_castle_mid():
    if DrumIsland.h == 6:

        yamato "Well, it's all frozen in here too..."

        nami "We're sheltered from the wind a bit in here, but it's not much better than outside..."

        robin "The temperature is extremely low, many things are frozen, and there's a lot of snow... This place really needs maintenance."

        nami "Let's get the information quickly and get off this frozen island... Someone must live around here!"

        $ DrumIsland.h = 7
        
    menu:
        "Enter the doctorine room":
            jump di_castle_room
        
        "Back":
            jump drum_island_castle
