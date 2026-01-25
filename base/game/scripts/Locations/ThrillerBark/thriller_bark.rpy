# Version event: 3
# Version game: 0.5

label thriller_bark():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ game.location = "thriller_bark"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_thrillerbark()
    jump m_thriller_bark

label m_thriller_bark():
    if ThrillerBark.h == 0:
        nami "We've arrived, Captain. This is where the Eternal Pose points us to... this should be [ThrillerBark.n]!!!"
        window hide
        pause 0.8
        window auto
        
        robin "It's supposed to be a ship according to the reports... But there's even an island inside, that's why we could reach it..."
        nami "It's enormous... There are walls so high... they surround everything as far as the eye can see..."
        yamato "The walls are huge, but there seems to be an opening over there... Maybe we could dock."
        yamato "We have to be careful, Captain!"
        yamato "We don't know what dangers await us when we get off the ship..."
        robin "It would be best to go prepared..."

        $ ThrillerBark.h = 1

    menu:
        "Arrival":
            jump thriller_bark_entrance

        "Back":
            jump ship_mid
