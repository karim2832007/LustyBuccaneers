# Version event: 1
# Version game: 0.1

define id_inventory = 0
define ui_inventory_id = ["inventory", "tools"]

screen ui_inventory_base():
    modal True
    zorder 15 #-15 # con 0 tapo todo

    add "BG locations"

    imagebutton:
        idle "black_40"
        hover "black_40"
        action [Hide("ui_inventory_base"), SetVariable ("id_inventory", 0)]

    button:
        focus_mask None
        action NullAction()
        area (360, 40, 1200, 1000)

    add "GUI inventory ui_"+ ui_inventory_id[globals()['id_inventory']]:
        xalign 0.5
        yalign 0.5

    frame:
        background None
        area (1580, 40, 320, 120)

        button:
            focus_mask None
            action NullAction()

        add "GUI inventory ui_inventory_berries"

        text "[berries]":
            font gui.interface_text_font
            color "#f1e3da"
            outlines [(2, "#000000cc", 0, 0)]  
            xalign 0.5
            xoffset 40
            yalign 0.5
            size 54

    hbox:
        #background "black_100"
        area (360, 40, 1200, 1000)
        
        frame:
            background None
            xsize 270
            ysize 1000

            # SOLAPAS
            vbox:
                yoffset 30
                xoffset 25
                spacing 20

                #frame:
                #    background None
                #    xsize 220
                #    ysize 220
                button:
                    xsize 220
                    ysize 220
                    action [SetVariable ("id_inventory", 0)] 

                #frame:
                #    background None
                #    xsize 220
                #    ysize 220

                button:
                    xsize 220
                    ysize 220
                    action [SetVariable ("id_inventory", 1)] 

                frame:
                    background None
                    xsize 220
                    ysize 220

                frame:
                    background None
                    xsize 220
                    ysize 220


        use expression "ui_" + ui_inventory_id[globals()['id_inventory']]
        

screen ui_inventory():
    # IF INVENTARIO
    vbox:
        xsize 930
        ysize 1000

        frame:
            background None
            xsize 930
            ysize 295

            vbox:
                yoffset 40
                xoffset 40
                spacing 15

                hbox:
                    spacing 20

                    frame:
                        background None
                        xsize 270
                        ysize 120

                        text "[gold]":
                            font gui.interface_text_font
                            color "#f1e3da"
                            outlines [(2, "#000000cc", 0, 0)]  
                            xalign 0.5
                            xoffset 65
                            yalign 0.5
                            size 54

                    frame:
                        background None
                        xsize 270
                        ysize 120

                        text "[iron]":
                            font gui.interface_text_font
                            color "#f1e3da"
                            outlines [(2, "#000000cc", 0, 0)]  
                            xalign 0.5
                            xoffset 65
                            yalign 0.5
                            size 54

                    frame:
                        background None
                        xsize 270
                        ysize 120

                        text "[wood]":
                            font gui.interface_text_font
                            color "#f1e3da"
                            outlines [(2, "#000000cc", 0, 0)]  
                            xalign 0.5
                            xoffset 65
                            yalign 0.5
                            size 54

                hbox:
                    spacing 20

                    frame:
                        background None
                        xsize 270
                        ysize 120

                        text "[food]":
                            font gui.interface_text_font
                            color "#f1e3da"
                            outlines [(2, "#000000cc", 0, 0)]  
                            xalign 0.5
                            xoffset 65
                            yalign 0.5
                            size 54

                    frame:
                        background None
                        xsize 270
                        ysize 120

                        text "[paper]":
                            font gui.interface_text_font
                            color "#f1e3da"
                            outlines [(2, "#000000cc", 0, 0)]  
                            xalign 0.5
                            xoffset 65
                            yalign 0.5
                            size 54

                    frame:
                        background None
                        xsize 270
                        ysize 120

                        text "[fabric]":
                            font gui.interface_text_font
                            color "#f1e3da"
                            outlines [(2, "#000000cc", 0, 0)]  
                            xalign 0.5
                            xoffset 65
                            yalign 0.5
                            size 54

        frame:
            background None
            xsize 930
            ysize 705

            vpgrid:
                yoffset 35
                xoffset 80
                cols 5
                spacing 30

                for name_object in Inventory:
                    if globals()[name_object] > 0:
                        frame:
                            xsize 130
                            ysize 130
                            background None

                            add "obj_" + name_object:
                                xalign 0.5
                                yalign 0.5

                            if type(globals()[name_object]) is not bool:
                                text "x["+ name_object +"]":
                                    font gui.interface_text_font
                                    color "#f1e3da"
                                    outlines [(2, "#000000cc", 0, 0)]                       
                                    xalign 1.0
                                    yalign 0.98
                                    xoffset -5
                                    size 40


screen ui_tools():
    # IF INVENTARIO
    frame:
        background None
        xsize 930
        ysize 1000

        hbox:
            yalign 0.5
            xalign 0.5
            xsize 530
            ysize 800
            spacing 90
            
            vbox:
                spacing 70
        
                frame:
                    
                    background None
                    xsize 220
                    ysize 220

                    if tool_rod:
                        add "obj_rod":
                            xalign 0.5
                            yalign 0.5

                frame:
                    background None
                    xsize 220
                    ysize 220

                frame:
                    background None
                    xsize 220
                    ysize 220

            vbox:
                spacing 70
        
                frame:
                    background None
                    xsize 220
                    ysize 220

                    if tool_shovel:
                        add "obj_shovel":
                            xalign 0.5
                            yalign 0.5

                frame:
                    background None
                    xsize 220
                    ysize 220

                frame:
                    background None
                    xsize 220
                    ysize 220