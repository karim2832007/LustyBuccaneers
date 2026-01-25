# Version event: 1
# Version game: 0.11

screen patreon_board():
    modal True
    zorder -20

    add "GUI board bounty_board"

    text "Patreons":
        font gui.interface_text_font
        color "#140a07"
        outlines [(1, "#926456ff", 0, 0)]  
        xalign 0.5
        yoffset 70
        size 60

    frame:
        background None
        area (0, 0, 200, 200)

        button:
            focus_mask None
            action [Hide("patreon_board"), Return()]


    frame:
        background None
        area (291, 165, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 001"
            hover "GUI board wanted patrons 001"
            action NullAction()

    frame:
        background None
        area (633, 165, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 002"
            hover "GUI board wanted patrons 002"
            action NullAction()

    frame:
        background None
        area (975, 165, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 003"
            hover "GUI board wanted patrons 003"
            action NullAction()

    frame:
        background None
        area (1317, 165, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 004"
            hover "GUI board wanted patrons 004"
            action NullAction()

    frame:
        background None
        area (291, 579, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 005"
            hover "GUI board wanted patrons 005"
            action NullAction()

    frame:
        background None
        area (633, 579, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 006"
            hover "GUI board wanted patrons 006"
            action NullAction()

    frame:
        background None
        area (975, 579, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 007"
            hover "GUI board wanted patrons 007"
            action NullAction()

    frame:
        background None
        area (1317, 579, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 008"
            hover "GUI board wanted patrons 008"
            action NullAction()

    imagebutton:
        idle "GUI board bounty_arrow"
        hover "GUI board bounty_arrow_press"
        action [Hide("patreon_board")]
        xpos 10
        yalign 0.5


    imagebutton at flip:
        idle "GUI board bounty_arrow"
        hover "GUI board bounty_arrow_press"
        action [Show("patreon_board_page_2")]
        sensitive not is_screen_active("say")
        xalign 1.0
        xoffset -10
        yalign 0.5


screen patreon_board_page_2():
    modal True
    zorder -20

    add "GUI board bounty_board"

    text "Patreons":
        font gui.interface_text_font
        color "#140a07"
        outlines [(1, "#926456ff", 0, 0)]  
        xalign 0.5
        yoffset 70
        size 60

    frame:
        background None
        area (0, 0, 200, 200)

        button:
            focus_mask None
            action [Hide("patreon_board"), Return()]


    frame:
        background None
        area (291, 165, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 009"
            hover "GUI board wanted patrons 009"
            action NullAction()


    frame:
        background None
        area (633, 165, 312, 384)

        imagebutton:
            idle "GUI board wanted patrons 010"
            hover "GUI board wanted patrons 010"
            action NullAction()

    imagebutton:
        idle "GUI board bounty_arrow"
        hover "GUI board bounty_arrow_press"
        action [Hide("patreon_board_page_2")]
        xpos 10
        yalign 0.5