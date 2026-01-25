# Version event: 2
# Version game: 0.18

label cactus_island():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ game.location = "cactus_island"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    #$ music_thrillerbark()
    jump m_cactus_island

label m_cactus_island():
    if CactusIsland.h == 0:
        nami "We've arrived, Captain. This should be [CactusIsland.n]!!!"
        window hide
        pause 0.8
        window auto

        nami "It's gigantic... Now I understand why they gave it this name.." 
        nami "From a distance, this island looks like a cluster of enormous cacti."        
        robin "From the information I was able to gather..."
        robin "This island seems to be a hub for a large number of bounty hunters, a border outpost where the World Government's law isn't very present..."
        yamato "We have to be careful, but if they want trouble with us... They'll get it! There's no need to be afraid."
        nami "Over there, I see a passage leading to what looks like a village, with several buildings. We could dock nearby."
        player "Sounds good to me, let's dock there and see what this island has to offer!"

        $ CactusIsland.h = 1

    menu:
        "Land":
            jump ci_whisky_peak

        "Back":
            jump ship_mid
