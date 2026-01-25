# Version event: 2
# Version game: 0.9

label set_player_name:
    call screen s_set_player_name

    $ player_name = _return.strip()
        
    return


screen s_set_player_name:
    modal True

    add "black_100"

    default default_name = player_name

    add "GUI windows small_window":
        yoffset 277
        xoffset 510

    vbox:
        align (0.5, 0.46)
        
        frame:
            padding (0, 0)
            background None
            ypos 0.5
            yanchor 0.5
    
            has vbox:
                at a_change_name

                frame:
                    background None
                    align (0.5, 0.5)
                    size_group "change_name"

                    text _("Enter your name: "):
                        size 45

                frame:
                    background None
                    size_group "change_name"

                    input:
                        xalign 0.5
                        # Se edita de forma predeterminada al apretar enter
                        value ScreenVariableInputValue("default_name", returnable=True)
                        pixel_width 400
                        size 45
                        allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'`."

            fixed:
                xfit True
                yfit True
                align (0.5, 0.5)
                yoffset 100
                xoffset 0


                textbutton "Continue":
                    action If(
                        default_name,
                        Return(default_name),
                        NullAction(),
                    )
                    #action (Return(default_name))
                    keysym('K_RETURN', 'K_KP_ENTER')
                    text_size 50


screen s_set_girl_name(nameGirl = ""):
    modal True

    #add "black_100"

    default girl_name = nameGirl

    #default default_name = name

    add "GUI windows small_window":
        yoffset 670
        xoffset 510

    vbox:
        align (0.5, 0.82)
        
        frame:
            padding (0, 0)
            background None
            ypos 0.7
            yanchor 0.5
    
            has vbox:
                #at a_change_name
                spacing 30

                frame:
                    background None
                    align (0.5, 0.5)
                    size_group "change_name"

                    text _("What is her name?"):
                        size 45

                frame:
                    background None
                    size_group "change_name"

                    input:
                        xalign 0.5
                        # Se edita de forma predeterminada al apretar enter
                        value ScreenVariableInputValue("girl_name", returnable=True)
                        pixel_width 450
                        size 70
                        allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'`."

            fixed:
                xfit True
                yfit True
                align (0.5, 0.5)
                yoffset 50
                xoffset 0

                textbutton "Continue":
                    action If(
                        girl_name,
                        Return(girl_name),
                        NullAction(),
                    )
                    keysym('K_RETURN', 'K_KP_ENTER')
                    text_size 50



