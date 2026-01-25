# Version event: 4
# Version game: 0.11

default tutorial_bounty = True

label bounty_board:
    $ ui_interface = False
    call screen ui_bounty_board()
    $ ui_interface = True
    hide s_bounty_board_nohide

    jump m_shells_town


screen ui_bounty_board():
    modal True
    zorder -20

    add "GUI board bounty_board"

    text "Bounty Board":
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
            action Return()
            sensitive not is_screen_active("say")


    if not alvida_wanted: 
        frame:
            background None
            area (291, 165, 312, 384)

            imagebutton:
                idle "GUI board wanted alvida_wanted"
                hover "GUI board wanted alvida_wanted"
                action [Call("bounty_board_alvida")]
                sensitive not is_screen_active("say")

    if not zala_wanted: 
        frame:
            background None
            area (633, 165, 312, 384)

            imagebutton:
                idle "GUI board wanted zala_wanted"
                hover "GUI board wanted zala_wanted"
                action [Call("bounty_board_zala")]
                sensitive not is_screen_active("say")

    imagebutton at flip:
        idle "GUI board bounty_arrow"
        hover "GUI board bounty_arrow_press"
        action [Show("patreon_board")]
        sensitive not is_screen_active("say")
        xalign 1.0
        xoffset -10
        yalign 0.5
    
screen s_bounty_board_nohide():
    use ui_bounty_board
    
    button:
        focus_mask None
        action Return()
        sensitive not is_screen_active("say")
        area (0, 0, 1920, 1080)