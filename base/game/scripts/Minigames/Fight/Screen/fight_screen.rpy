# Version event: 1
# Version game: 0.23

label l_fight_screen():
    # black
    window hide
    show screen screen_black with Dissolve(0.6)
    
    if enemy_location != None:
        $ game.location = enemy_location

        python:
            if hide_label:
                if renpy.has_label(hide_label):
                    renpy.call(hide_label)
                hide_label = None

    $ ui_interface = False
    show screen s_fight_nohide 
    play music fight_music fadein 2.0
    hide screen screen_black with Dissolve(0.3)
    window auto
    return

screen s_fight_nohide():
    zorder -20
    use s_fight

screen s_fight():
    zorder -20

    add "BG locations":
        blur 3

    if clock_rain:
        add "black_30"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        add [enemy_figth.image]

    if clock_rain:
        add "a_rain"

    frame:
        background None
        yoffset 15
        xalign 0.5
        yalign 0.0
        xsize 800
        ysize 60

        if enemy_figth.mana > 0:
            bar value enemy_figth.mana:
                range enemy_figth.max_mana
                xysize(700,40)
                yalign 0.5
                xalign 0.5
                yoffset 35
                left_bar "minigames fight bar_enemy_mana"
                right_bar "minigames fight bar_enemy_mana_back"

        bar value enemy_figth.hp:
            range enemy_figth.max_health
            xysize(800,60)
            if(enemy_figth.hp < enemy_figth.max_health/2):
                if(enemy_figth.hp < enemy_figth.max_health/4):
                    left_bar "minigames fight bar_enemy_health_red"
                else:
                    left_bar "minigames fight bar_enemy_health_yellow"
            else:
                left_bar "minigames fight bar_enemy_health"

            right_bar "minigames fight bar_enemy_health_back"

        
        text "[enemy_figth.hp]/[enemy_figth.max_health]":
            font gui.interface_text_font
            color "#110f0e"
            xalign 0.5
            yalign 0.5
            size 36



    frame:
        background None
        yoffset 1
        yalign 1.0
        xalign 0.5

        vbox:
            #frame:
            #    background None
            #    xalign 0.5
            #    add [enemy_img] #at enemy_zoom

            frame:
                background None
                xsize 1800
                ysize 360
                add "minigames fight ui_fight"
                
                hbox:
                    frame:
                        background None
                        xsize 800
                        ysize 360

                        vbox:
                            style_prefix "fight_ui"
                            yalign 0.5
                            xalign 0.5

                            hbox:
                                frame:
                                    button:
                                        #action Call("fight_atack")
                                        action [Return(["attack", 0])]
                                        sensitive not is_screen_active("say")

                                    text "Attack":
                                        yalign 0.3
                                        xalign 0.5
                                        xoffset -30

                                frame:
                                    button:
                                        action [Return(["guard", 0])]#Call("fight_guard")
                                        sensitive not is_screen_active("say")

                                    text "Guard":
                                        yalign 0.3
                                        xalign 0.5
                                        xoffset 30

                            hbox:
                                frame:
                                    button:
                                        action Call("fight_screen_skills")
                                        sensitive not is_screen_active("say")

                                    text "Skills":
                                        yalign 0.7
                                        xalign 0.5
                                        xoffset -30

                                frame:
                                    button:
                                        action Call("fight_screen_heal")
                                        #action Call("fight_items")
                                        sensitive not is_screen_active("say")

                                    text "Item":
                                        yalign 0.7
                                        xalign 0.5
                                        xoffset 30

                    frame:
                        background None
                        ysize 360
                        xsize 1000

                        frame:
                            background None
                            ysize 300
                            xsize 930
                            yalign 0.5
                            xalign 0.5

                            vbox:
                                style_prefix "fight_ui_healt"

                                frame:
                                    background None
                                    ysize 75

                                    hbox:
                                        frame: 
                                            ysize 75
                                            xsize 310

                                            text "[player_name]":
                                                yalign 0.8
                                                xalign 0.0
                                                size 48
                                                xoffset 25

                                        frame: 
                                            ysize 75
                                            xsize 310
                                            
                                            bar value RPGPlayer.hp():
                                                range RPGPlayer.true_hp_max()
                                                xysize(280,25)
                                                yalign 0.8
                                                xalign 0.5
                                                if(RPGPlayer.hp() < RPGPlayer.true_hp_max()/2):
                                                    if(RPGPlayer.hp() < RPGPlayer.true_hp_max()/4):
                                                        left_bar "minigames fight bar_player_health_red"
                                                    else:
                                                        left_bar "minigames fight bar_player_health_yellow"
                                                else:
                                                    left_bar "minigames fight bar_player_health"

                                                right_bar "minigames fight bar_player_health_back"

                                            text "HP":
                                                outlines [(4, "#281400", 0, 0)]
                                                color "#ffffff"
                                                yalign 0.4
                                                xalign 0.0
                                                xoffset 25

                                            text "[RPGPlayer.hp()]/[RPGPlayer.true_hp_max()]":
                                                font gui.interface_text_font
                                                outlines [(4, "#281400", 0, 0)]
                                                color "#ffffff"
                                                xalign 1.0
                                                yalign 0.5
                                                xoffset -25

                                        frame: 
                                            ysize 75
                                            xsize 310
                                            
                                            bar value player_mana:
                                                range RPGPlayer.true_mana_max()
                                                xysize(280,25)
                                                yalign 0.8
                                                xalign 0.5
                                                left_bar "minigames fight bar_player_sp"
                                                right_bar "minigames fight bar_player_health_back"

                                            text "SP":
                                                outlines [(4, "#281400", 0, 0)]
                                                color "#ffffff"
                                                yalign 0.4
                                                xalign 0.0
                                                xoffset 25

                                            text "[player_mana]/[RPGPlayer.true_mana_max()]":
                                                font gui.interface_text_font
                                                outlines [(4, "#281400", 0, 0)]
                                                color "#ffffff"
                                                xalign 1.0
                                                yalign 0.5
                                                xoffset -25

                                frame:
                                    #background None
                                    ysize 75

                                frame:
                                    #background None
                                    ysize 75

                                frame:
                                    #background None
                                    ysize 75 

    if not player_turn:
        frame:
            background None
            xsize 1920
            ysize 1080
            xalign 0.5
            yalign 0.5

            button:
                sensitive not is_screen_active("say")
                action NullAction()
                background None
                xsize 1920
                ysize 1080
    



#STYLES
style fight_ui_frame:
    background None
    xsize 340
    ysize 140

style fight_ui_text:
    size 72
    color "#ffffff"
    font gui.interface_text_font

style fight_ui_healt_frame:
    background None

style fight_ui_healt_text:
    color "#ffffff"