# Version event: 2
# Version game: 0.9

label drum_island_castle():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "drum_island_castle"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_drumisland()
    jump m_drum_island_castle

label m_drum_island_castle():
    if DrumIsland.h == 5:
    
        nami "Wow, look at that castle, it's huge!"

        yamato "It doesn't seem very well maintained, looks like it's seen better days... Are you sure someone lives here?"

        robin "It seems to be a very old castle, definitely someone royal lived or still lives here... But you're right, it's quite neglected!"
        robin "It looks like several rooms are frozen over..."

        nami "Let's go inside, Captain, I'm freezing!"
        nami "I don't want to stay out here another minute!"

        player "It's strange that no one has come to greet us... We'd better go inside, but stay alert, ladies!"

        $ DrumIsland.h = 6
        
    menu:
        "Enter the castle":
            jump di_castle_mid
        
        "Back":
            jump drum_island_forest
