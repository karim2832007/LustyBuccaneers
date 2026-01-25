# Version event: 3
# Version game: 0.27

default elegia_forest = 0
default elegia_forest_map = False
default elegia_forest_bg = 1

# Secuencia correcta del laberinto (en orden)
# 2 = arriba, 1 = izquierda, 3 = derecha
define forest_path = [2, 1, 3]

label elegia_forest():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ elegia_forest_bg = 1
    $ game.location = "elegia_forest"

    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ music_elegia()
    jump m_elegia_forest

label m_elegia_forest():

    if elegia_forest == 0:
        
        pause 0.5

        show yamato with dissolve:
            yalign 1.0
            xalign 0.45

        yamato "Clearly that guy [kaginote.n] escaped this way..."
        yamato "The coward must have fled through this forest after throwing the smoke bomb... It's the only path around here..."

        show nami with dissolve:  
            yalign 1.0  
            xalign 0.90  

        nami "He really tricked us... Everything pointed to him escaping toward the city at first..."

        show robin with dissolve:  
            yalign 1.0  
            xalign 0.05  

        robin "Yes, it's a very vast and thick forest from what I can see... Ideal for hiding"
        robin "In any case, there's a clear trail. If we're careful, we shouldn't get lost!"
        robin "I'll try to analyze the path as we go..."
        player "Perfect [robin.n], I'm counting on you!"
        player "I don't think it'll be too hard to find the way out, let's go girls!"

        window hide
        window auto
        hide robin 
        hide yamato
        hide nami
        with dissolve

        $ elegia_forest = 1

    elif elegia_forest == 1:

        player "Damn, looks like we went all the way around... We're back at the start!"

        show robin at center with dissolve

        robin "Yes, this is definitely the beginning..."
        robin "According to my notes... First we need to go straight from here."
        player "Good! Then let's start that way!"

        window hide
        hide robin
        with dissolve
        window auto

        $ elegia_forest = 2

    elif elegia_forest == 2:

        show yamato at center with dissolve

        yamato "Damn it... We're lost again..."
        yamato "Damn forest..."
        yamato "Maybe we should look for help..."
        player "Relax, I've got it now... According to [robin.n], we go straight first, then left, and finally right!"
        player "If we follow those instructions, we should be out of here!"

        window hide
        hide yamato
        with dissolve
        window auto

        $ elegia_forest = 3
        
    else:
        menu:
            "Continue":
                pass
            "Back":
                jump elegia_road

    $ ui_interface = False
    $ step = 0
    while step < len(forest_path):
        call screen forest_arrows with Dissolve(1.0)
        if _return == forest_path[step]:
            $ step += 1
            call elegia_forest_call(bg=elegia_forest_bg+1) from _call_elegia_forest_call
        else:
            jump elegia_forest

    # Si completa todos los pasos:
    $ elegia_forest = 4
    $ ui_interface = True
    jump elegia_church


screen forest_arrows():
    modal True
    zorder 15
    tag menu

    imagebutton:
        idle "GUI forest forest_arrow"
        hover "GUI forest forest_arrow"
        action Return(1)  # Izquierda
        xoffset 100
        yalign 0.5

    imagebutton at rotate_90:
        idle "GUI forest forest_arrow"
        hover "GUI forest forest_arrow"
        action Return(2)  # Arriba
        xalign 0.5
        yalign 0.0

    imagebutton at flip:
        idle "GUI forest forest_arrow"
        hover "GUI forest forest_arrow"
        action Return(3)  # Derecha
        xalign 1.0
        xoffset -100
        yalign 0.5

label elegia_forest_call(bg=1):
    window hide
    show screen screen_black with Dissolve(0.6)

    $ elegia_forest_bg = bg
    $ game.location = "elegia_forest"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto
    return



