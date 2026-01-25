# Version event: 2
# Version game: 0.23

screen choice(items):
    style_prefix "choice"
    zorder -20

    # Pongo en falce todos los choice
    default choice_hovered = {i: False for i in range(len(items))}

    # enumerate: En "i" e "item" mete los valores de items i siendo numeros item el valor
    default choice_help = {i: item.kwargs["help"].upper() if "help" in item.kwargs else "" for i, item in enumerate(items)}


    fixed:
        style "choice_fixed"
        for i, item in enumerate(items):
            button at choice_zoom, choice_appear(i, len(items)):
                sensitive (not item.kwargs["disabled"] if "disabled" in item.kwargs else True)

                action item.action  
                hovered SetDict(choice_hovered, i, True)
                unhovered SetDict(choice_hovered, i, False)

                has fixed
                showif ((item.kwargs["disabled"] if "disabled" in item.kwargs else False) and choice_help[i] != ""):
                    frame:
                        style_prefix "choice_help"
                        text _(choice_help[i])

                text item.caption style "choice_button_text"


default choice_id = ""

screen choice_list(items):
    style_prefix "choice"
    zorder -20

    fixed:
        style "choice_fixed"
        for i, item in enumerate(items):
            if " | " in item:
                $ name, value = item.split(" | ")
                button at choice_zoom, choice_appear(i, len(items)):
                    text name xalign 0.0 xoffset 200 style "choice_button_text"
                    text value xalign 1.0 xoffset -200 style "choice_button_text"
                    action [SetVariable("choice_id", i), Return()]

            else:                
                button at choice_zoom, choice_appear(i, len(items)):
                    text [item] style "choice_button_text"
                    action [SetVariable("choice_id", i), Return()]




style choice_fixed is fixed
style choice_button is button
style choice_button_text is button_text

style choice_fixed:
    xfill True
    xalign 0.5
    yalign 1.0
    yanchor 1.0

style choice_frame is empty:
    background Solid("#000C")
    align (0.5, 0.5)
    xfill True
    
style choice_text:
    size 22
    #outlines [(2, "#ffd4af", 0, 0)]
    align (0.5, 0.5)

style choice_button is default:
    properties gui.button_properties("choice_button")
    idle_background "gui/button/choice_idle_background.png"
    hover_background "gui/button/choice_hover_background.png"
    xalign 0.5
    yalign 0.5
    anchor (0.5, 0.5)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    yalign 0.5

style choice_help_frame is empty:
    background Frame("GUI help", Borders(15, 1, 15, 0))
    anchor (1.0, 1.0)
    pos (1.0, 0.85)
    ysize 30
    xpadding 20

style choice_help_text is button_text:
    color "#3f0a38"
    size 16