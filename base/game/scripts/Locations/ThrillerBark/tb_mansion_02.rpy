# Version event: 4
# Version game: 0.5

label tb_mansion_02():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
    
    $ game.location = "tb_mansion_02"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_thrillerbark()
    jump m_tb_mansion_02

label m_tb_mansion_02():
    if ThrillerBark.h == 6:
        window hide
        pause 1.0
        window auto
        show nami at center with dissolve
        nami "This door on the left leads to a bathroom..."
        
        pause 0.5
        show nami:
            linear 0.4 xalign 0.15

        pause 0.4
        
        nami "It would be great to relax... Take a hot bath..."

        show robin with dissolve:
            yalign 1.0
            xalign 0.5

        robin "After traveling so much and going through the forest... We're covered in mud and dust..."
        robin "It wouldn't be a bad idea... But I'm not sure if it's the best idea..."
    
        show robin:
            linear 0.4 xalign 0.85 

        pause 0.4

        show yamato anger c1 at center with dissolve
        yamato "Of course not! It's not time to relax, we don't know when an enemy might appear..."
        nami "Alright, alright... I think you're right!"

        $ ThrillerBark.h = 7

    menu:
        "Advance":
            jump tb_mansion_03

        "Back":
            jump tb_mansion_01
