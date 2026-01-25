# Version event: 1
# Version game: 0.23

label fight_hide():
    hide screen s_fight_nohide
    
    if not no_interface:
        $ ui_interface = True

    return


label fight_hide_die():
    hide screen s_fight_nohide
    
    if not no_interface:
        $ ui_interface = True

    if clock_rain:
        $ hide_rain()

    return