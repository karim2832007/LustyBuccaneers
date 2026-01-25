# Version event: 1
# Version game: 0.1

default ui_interface = True

default ui_berries = False
default ui_ship = False
default ui_hp = False
default ui_strength = False

screen main_interface():
    zorder -15
    
    if ui_interface:
        add "GUI main_interface clock":
            pos(0, 0)

        frame:
            background None
            pos(0, 22)
            xsize 330
            text _("Day [game.clock.getDay]"):
                font gui.interface_text_font
                color "#6b5440"
                size 40
                xalign 0.5

        frame:
            pos(0, 62)
            background None
            xsize 330
            text get_day():     #[game.clock.getTime]":
                font gui.interface_text_font
                color "#6b5440"
                size 40
                xalign 0.5

        vbox:
            yoffset 15
            spacing 20
            xalign 1.0

            frame:
                xsize 372
                ysize 100
                background None
                
                imagebutton:
                    idle "GUI main_interface button_rigth_idle"
                    hover "GUI main_interface button_rigth_hover"
                    #action Show("girls_stats")
                    action ToggleScreen("girls_stats")

                text _("Girls Stats"):
                    font gui.interface_text_font
                    color "#6b5440"
                    xalign 0.6
                    yalign 0.45
                    size 40

            frame:
                xsize 372
                ysize 100
                background None
                
                imagebutton:
                    idle "GUI main_interface button_rigth_idle"
                    hover "GUI main_interface button_rigth_hover"
                    action ToggleScreen("ui_inventory_base")

                text _("Inventory"):
                    font gui.interface_text_font
                    color "#6b5440"
                    xalign 0.6
                    yalign 0.45
                    size 40

            if not renpy.variant("pc"):
                frame:
                    xsize 372
                    ysize 100
                    background None
                    
                    imagebutton:
                        idle "GUI main_interface button_rigth_idle"
                        hover "GUI main_interface button_rigth_hover"
                        action ShowMenu('save')

                    text "Menu":
                        font gui.interface_text_font
                        color "#6b5440"
                        xalign 0.6
                        yalign 0.45
                        size 40

            #frame:
            #    xsize 372
            #    ysize 100
            #    background None
            #    
            #    imagebutton:
            #        idle "GUI main_interface button_rigth_idle"
            #        hover "GUI main_interface button_rigth_hover"
            #        action NullAction()
            #
            #    text "Quests":
            #        font gui.interface_text_font
            #        color "#6b5440"
            #        xalign 0.6
            #        yalign 0.45
            #        size 40

        vbox:
            spacing 15
            xoffset 40
            yoffset 150

            use hud_player

            use hud_ship


    if ui_berries:
        frame:
            background None
            area (1580, 940, 320, 120)

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
    
    if ui_ship:
        frame:
            background None
            area (1580, 940, 320, 120)

            button:
                focus_mask None
                action NullAction()

            add "GUI ui_basic"

            text "Ship HP\n[ship_player_health]/[ships_hp_max[ship_player_lvl]]":
                font gui.interface_text_font
                color "#f1e3da"
                outlines [(2, "#000000cc", 0, 0)]  
                text_align 0.5
                xalign 0.5
                yalign 0.5
                size 40

    if ui_hp:
        frame:
            background None
            area (1580, 940, 320, 120)

            button:
                focus_mask None
                action NullAction()

            add "GUI ui_basic"

            text "HP\n[player_hp]/[RPGPlayer.true_hp_max()]":
                font gui.interface_text_font
                color "#f1e3da"
                outlines [(2, "#000000cc", 0, 0)]  
                text_align 0.5
                xalign 0.5
                yalign 0.5
                size 40

    if ui_strength:
        frame:
            background None
            area (1580, 940, 320, 120)

            button:
                focus_mask None
                action NullAction()

            add "GUI ui_basic"

            text "Strength\n[Strength]":
                font gui.interface_text_font
                color "#f1e3da"
                outlines [(2, "#000000cc", 0, 0)]  
                text_align 0.5
                xalign 0.5
                yalign 0.5
                size 40