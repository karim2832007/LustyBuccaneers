# Version event: 1
# Version game: 0.23

label fight_end():
    if player_run:
        $ hide_label = "fight_hide"
        $ player_run = False

    else:
        window hide
        call fight_hide from _call_fight_hide
        with t_black
        window auto
    
    return
