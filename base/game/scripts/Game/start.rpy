# Version event: 1
# Version game: 0.1

label start:

    # Iniciar Variables
    call init_game from _call_init_game

    call backstory from _call_backstory

    # menu rapido on (quizas mejor off y despues del backstory)
    $ quick_menu = True

    # Inicia el juego
    call new_game from _call_new_game

    # Termina el juego
    "ending"
    
    return