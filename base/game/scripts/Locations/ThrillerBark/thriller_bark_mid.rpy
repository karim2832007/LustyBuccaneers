# Version event: 4
# Version game: 0.5

label thriller_bark_mid():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None

    $ game.location = "thriller_bark_mid"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    
    $ music_thrillerbark()
    jump m_thriller_bark_mid

label m_thriller_bark_mid():
    if ThrillerBark.h == 3:
        window hide
        pause 1.2
        window auto

        show nami at center with dissolve
        nami "Phew, finally!"
        nami "We've been walking for a long time! But we're finally reaching somewhere civilized!"
        hide nami with dissolve

        show robin at center with dissolve
            
        robin "The path is surrounded by a very dense forest. If we enter the forest, we might get lost, but it could be interesting..."
        robin "On the other hand, the gate in front of us seems to lead to the entrance of some kind of castle or mansion!"
        
        show robin:
            linear 0.4 xalign 0.85

        pause 0.4

        show yamato with dissolve:
            yalign 1.0
            xalign 0.5        
        
        yamato "In that castle, there's surely a worthy opponent, but it would be interesting to explore the surroundings first!"
        
        show yamato:
            linear 0.4 xalign 0.15

        pause 0.4

        show nami at center with dissolve       
        
        nami "Look over there!... It looks like a cemetery, we could loot some graves... maybe we'll find something valuable!!!"
        nami "Where are we going, [player.n]? What do you think, Captain?"

        window hide
        hide nami
        hide robin
        hide yamato
        with dissolve
        window auto

        $ ThrillerBark.h = 4

    menu:
        "Open the Gate":
            jump thriller_bark_mansion

        "Explore Forest":
            jump tb_forest

        "Go to the Cemetery":
            #narrador "In this version, the Cemetery is not available."
            jump thriller_bark_cemetery

        "Back":
            jump thriller_bark_entrance
