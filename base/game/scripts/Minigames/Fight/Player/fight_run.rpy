# Version event: 1
# Version game: 0.23

default player_run = False

label fight_run():
    narrador "The enemy is too strong..."
    narrador "You decided to escape..."
    narrador "[enemy_figth.n] has defeated you!!!"

    $ player_run = True
    $ fight_return = False
    return