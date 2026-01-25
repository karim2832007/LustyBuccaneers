# Version event: 3
# Version game: 0.9

label drum_island_forest():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "drum_island_forest"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_drumisland()
    jump m_drum_island_forest

label m_drum_island_forest():
    if DrumIsland.h == 4:
        
        show robin at center with dissolve

        robin "We'll have to cover quite a distance, but luckily, we just need to keep going up... We shouldn't lose our way."

        window hide
        hide robin with dissolve
        pause 1.2
        window auto

        show yamato:
            yalign 1.0
            xalign 0.5

        yamato "We need to stay alert and watch out for wild animals... These mountains are pretty inhospitable."

        show yamato with dissolve:
            yalign 1.0
            xalign 0.5

        show yamato:
            linear 0.4 xalign 0.15

        pause 0.4

        show nami with dissolve:
            yalign 1.0
            xalign 0.85


        nami "We should've brought more winter clothing! I'll keep this in mind for the next islands..."
    
        player "Alright, let's keep moving. Let's try to spend as little time as possible out here..."

        hide yamato
        hide nami
        with dissolve

        $ DrumIsland.h = 5
        
    menu:
        "Head to the Sakura tree" if DrumIsland.h >= 8:
            if DrumIsland.h == 8:
                yamato "It should be around here, Captain... Let's follow this path!"
            jump drum_island_sakura

        "Advance":
            jump drum_island_castle
        
        "Back":
            jump drum_island_village
