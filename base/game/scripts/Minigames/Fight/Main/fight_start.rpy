# Version event: 1
# Version game: 0.23

default event_gameover = None
default no_run = False
default fight_return = False
default no_interface = False
default fight_music = "battle"

label fight_start(enemy_pass = None, event_gameover = None, no_run = False, no_interface = False, enemy_location = None, hp_porcent = 1, enemy_music = "battle"):
    # Configuración de la batalla
    $ enemy_figth = enemy_pass
    $ event_gameover = event_gameover
    $ no_run = no_run
    $ no_interface = no_interface
    $ fight_music = enemy_music

    # Se termina la curacion en background
    $ finish_background_animations()

    if enemy_pass is None:
        $ fight_return = True
        return

    # Resetear batalla
    $ fight_return = False
    $ enemy_figth.reset(hp_porcent)
    

    # SCREENS
    call l_fight_screen from _call_l_fight_screen
    window hide
    # ROUND
    call fight_round from _call_fight_round
    window auto
    # RUN
    call fight_end from _call_fight_end


    return