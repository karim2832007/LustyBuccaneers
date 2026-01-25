# Version event: 4
# Version game: 0.31

label ci_whisky_peak():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ game.location = "ci_whisky_peak"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    #$ music_thrillerbark()
    jump m_ci_whisky_peak

label m_ci_whisky_peak():
    if CactusIsland.h == 1:

        pause 1.0
        show yamato smile at center with dissolve
        yamato "So here we are..."        
        yamato "All the buildings seem to be in terrible condition around here..."
        show yamato happy with Dissolve(0.2)
        yamato "This place is a mess..." 

        hide yamato with dissolve

        show robin at center with dissolve
            
        robin "[CactusIsland.n]... The rumors seem to be true, It's full of bounty hunters and smugglers... Perhaps we could gather some valuable information here."
        
        pause 0.5
       
        menu:
            "There are almost no women here...":
                player "There are almost no women here... What kind of island is this?!?"
                show robin happy with Dissolve(0.2)            
                robin "Always thinking about other women Captain..."
            
                $ robin_love -= 1
                narrador "[robin.n] Love -1"

            "Better not say anything":                
                player "(There are almost no women here... And the ones that are, I'm not even sure they are women... What kind of island is this?!?)"
     
        show robin:
            linear 0.4 xalign 0.85

        pause 0.4

        show yamato with dissolve:
            yalign 1.0
            xalign 0.5 

        yamato "No one seems to be looking for trouble with us... But let's not lower our guard."
        show robin neutral with Dissolve(0.2) 
        
        show yamato:
            linear 0.4 xalign 0.15

        pause 0.4

        show nami at center with dissolve       
        
        nami "We could take a break and grab a drink at the bar… It seems to be the hub of everything here, maybe we can find out something interesting."
        show yamato happy with Dissolve(0.2)
        yamato "That doesn't sound like not lowering our guard… But I like that idea, hahaha!"
        player "Alright, let's go. It seems like there's nothing else to do here anyway!"

        window hide
        hide nami
        hide robin
        hide yamato
        with dissolve
        window auto

        $ CactusIsland.h = 2

    menu:
        "Go to the Bar" if CactusIsland.h == 2:
            jump event_cactusisland_vivi

        "Back":
            jump cactus_island
