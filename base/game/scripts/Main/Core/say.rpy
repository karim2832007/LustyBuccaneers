# Version event: 2
# Version game: 0.31

default persistent.textbox_alpha = 0.90

init python:
    def is_screen_active(screen_name):
        return renpy.get_screen(screen_name) is not None

    
screen say(who, what):
    zorder 10
    style_prefix "say"

    window:
        id "window"

        # Opaciti
        background Transform(
            Image("gui/textbox.webp"),
            xalign=0.5, yalign=1.0,
            alpha=persistent.textbox_alpha
        )

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what" 

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    #if not renpy.variant("small"):
    #    add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default:
    #bold True
    outlines [(2.5, "#6b5440", 1, 1)]

style say_dialogue is default:
    outlines [(2, "#f0efd8", 0, 0)]

style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background None #Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False
