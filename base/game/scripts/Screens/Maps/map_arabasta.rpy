# Version event: 4
# Version game: 0.11  map_arabasta

default arabasta_location = "Nanohana"
default arabasta_target = "Nanohana"

define travel_costs = {
    "Nanohana": {"food": 0, "water": 0},
    "Erumalu": {"food": 2, "water": 2},
    "Yuba": {"food": 4, "water": 4},
    "Katorea": {"food": 4, "water": 4},
    "Rainbase": {"food": 6, "water": 6},
    "Alubarna": {"food": 6, "water": 6},
}

label map_arabasta:
    $ ui_interface = False
    call screen ui_map_arabasta()
    $ ui_interface = True
    hide s_map_arabasta_nohide

    jump expression "m_"+ game.location


screen ui_map_arabasta():
    modal True
    zorder -20

    add "GUI maps arabasta map_arabasta"

    text "ARABASTA  KINGDOM":
        font gui.interface_text_font
        color "#ffffff"
        outlines [(3, "#083019ff", 0, 0)]  
        xalign 0.522
        yoffset 2
        size 57

    frame:
        background None
        area (0, 0, 200, 200)

        button:
            focus_mask None
            action Return()


    frame:
        background None
        area (1780, 0, 520, 104)

        vbox:
            add "obj_food":
                zoom 0.8

            frame:
                background None
                xsize 150
                ysize 104

                text "{size=-15}x{/size}[food]":
                    font gui.interface_text_font
                    color "#ffffff"
                    outlines [(3, "#083019ff", 0, 0)]  
                    yalign 0.5
                    yoffset -25
                    size 64

            #null width 10
            null height 30

            add "obj_water":
                zoom 0.8

            frame:
                background None
                xsize 150
                ysize 104

                text "{size=-15}x{/size}[water]":
                    font gui.interface_text_font
                    color "#ffffff"
                    outlines [(3, "#083019ff", 0, 0)]  
                    yalign 0.5
                    yoffset -25
                    size 64




    frame:
        background None
        area (1040, 640, 435, 255)

        add "GUI maps arabasta map_name":
            yoffset -30

        add "GUI maps arabasta map_nanohana"

        text "NANOHANA":
            font gui.interface_text_font
            color "#ffffff"
            outlines [(3, "#083019ff", 0, 0)]  
            xalign 0.50
            yoffset -16
            size 42

        frame:
            background None
            xsize 375
            ysize 220
            yoffset 20
            xoffset 30

            #add "black_10"
            button:
                focus_mask None
                action [SetVariable ("arabasta_target", "Nanohana"), Jump("map_arabasta_jump")]


    frame:
        background None
        area (375, 535, 435, 255)

        add "GUI maps arabasta map_name":
            yalign 1.0

        add "GUI maps arabasta map_erumalu"

        text "ERUMALU":
            font gui.interface_text_font
            color "#ffffff"
            outlines [(3, "#083019ff", 0, 0)]  
            xalign 0.50
            yalign 1.0
            yoffset -12
            size 42

        frame:
            background None
            xsize 320
            ysize 220
            yoffset 20
            xoffset 60
        
            #add "black_10"
            button:
                focus_mask None
                action [SetVariable ("arabasta_target", "Erumalu"), Jump("map_arabasta_jump")]

    if Arabasta.h >= 5:
        frame:
            background None
            area (110, 350, 435, 255)

            add "GUI maps arabasta map_name":
                yalign 0.95
                xoffset -30

            add "GUI maps arabasta map_yuba":
                yoffset -30
                xoffset 20

            text "YUBA":
                font gui.interface_text_font
                color "#ffffff"
                outlines [(3, "#083019ff", 0, 0)]  
                xalign 0.50
                yalign 1.0
                yoffset -21
                xoffset -30
                size 42

            frame:
                background None
                xsize 400
                ysize 180
                yoffset 20
                xoffset -10

                #add "black_10"
                button:
                    focus_mask None
                    action [SetVariable ("arabasta_target", "Yuba"), Jump("map_arabasta_jump")]



    if Arabasta.h >= 9:
        frame:
            background None
            area (200, 50, 435, 255)

            add "GUI maps arabasta map_name":
                yalign 0.95
                yoffset 30

            add "GUI maps arabasta map_rainbase":
                yoffset -30
                xoffset 20

            text "RAINBASE":
                font gui.interface_text_font
                color "#ffffff"
                outlines [(3, "#083019ff", 0, 0)]  
                xalign 0.50
                yalign 1.0
                yoffset 8
                #xoffset -30
                size 42

            frame:
                background None
                xsize 400
                ysize 180
                yoffset 20
                xoffset -10

                #add "black_10"
                button:
                    focus_mask None
                    action [SetVariable ("arabasta_target", "Rainbase"), Jump("map_arabasta_jump")]

        frame:
            background None
            area (1480, 580, 435, 255)

            add "GUI maps arabasta map_name":
                yalign 0.95
                yoffset 20

            add "GUI maps arabasta map_katorea":
                yoffset -30
                xoffset 20

            text "KATOREA":
                font gui.interface_text_font
                color "#ffffff"
                outlines [(3, "#083019ff", 0, 0)]  
                xalign 0.50
                yalign 1.0
                yoffset -2
                #xoffset -30
                size 42

            frame:
                background None
                xsize 400
                ysize 180
                yoffset 20
                xoffset -10

                #add "black_10"
                button:
                    focus_mask None
                    action [SetVariable ("arabasta_target", "Katorea"), Jump("map_arabasta_jump")]

    if Arabasta.h >= 13:
        frame:
            background None
            area (1250, 80, 435, 255)

            add "GUI maps arabasta map_name":
                yalign 0.95
                yoffset 60

            add "GUI maps arabasta map_alubarna":
                yoffset -30
                xoffset 20

            text "ALUBARNA":
                font gui.interface_text_font
                color "#ffffff"
                outlines [(3, "#083019ff", 0, 0)]  
                xalign 0.50
                yalign 1.0
                yoffset 38
                size 42

            frame:
                background None
                xsize 450
                ysize 200
                #add "black_10"
                button:
                    focus_mask None
                    action [SetVariable ("arabasta_target", "Alubarna"), Jump("map_arabasta_jump")]




screen s_map_arabasta_nohide():
    use ui_map_arabasta
    
    button:
        focus_mask None
        action Return()
        area (0, 0, 1920, 1080)


label map_arabasta_jump():
    if arabasta_location != arabasta_target:
        $ renpy.show_screen("s_map_arabasta_nohide", _layer="master")
        if arabasta_target == "Nanohana":
            menu:
                narrador "Do you want to travel to [arabasta_target]?"
                "Yes":
                    pass
                "No":
                    jump map_arabasta
        else:
            $ cost_food = travel_costs[arabasta_target]["food"]
            $ cost_water = travel_costs[arabasta_target]["water"]

            menu:
                narrador "Do you want to travel to [arabasta_target]?\n\nRequires: [cost_food] Food and [cost_water] Water"
                "Yes":
                    if food >= cost_food and water >= cost_water:
                        $ food -= cost_food
                        $ water -= cost_water

                    else:
                        narrador "Insufficient resources"
                        jump map_arabasta
                "No":
                    jump map_arabasta

    if arabasta_target == "Yuba":
        if Arabasta.h > 8:
            jump ar_yuba_oasis

    jump expression "ar_" + arabasta_target.lower()
    
