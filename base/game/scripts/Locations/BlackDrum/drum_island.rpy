# Version event: 2
# Version game: 0.9

label drum_island():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "drum_island"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_drumisland()
    jump m_drum_island

label m_drum_island():
    if DrumIsland.h == 2:

        nami "Land ho, Captain!"

        yamato "Wow, it's a winter island!"

        nami "Why a winter island?!?... I was hoping for a tropical one, I could use some warmth and beaches!!"

        robin "What kind of medicinal plant could grow on an island like this?"

        yamato "Look over there, starboard side! It looks like a village!"

        robin "We could ask for directions, maybe they know the doctor we're looking for!"

        player "Excellent! Let's find a spot to dock and hide the ship, then head toward that village!"

        $ DrumIsland.h = 3

    menu:
        "Go to the village":
            jump drum_island_village
        
        "Back":
            jump ship_mid
