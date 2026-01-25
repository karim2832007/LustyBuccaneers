# Version event: 1
# Version game: 0.1

screen confirm(message, yes_action, no_action):

    ## Asegura que otras pantallas no reciban entrada mientras se muestra esta
    ## pantalla.
    modal True

    zorder 200

    style_prefix "confirm"

    add "BG locations"

    add "BG locations":
        alpha 0.8
        blur 16

    add "black_50"

    add "GUI windows small_window":
        yoffset 277
        xoffset 510

    frame:
        background None

        vbox:
            xalign .5
            yalign .5
            spacing 105
            

            label _(message):
                style "confirm_prompt"
                xalign 0.5


            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Clic derecho o escape responden "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text:
    size 45

style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text:
    size 45

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")