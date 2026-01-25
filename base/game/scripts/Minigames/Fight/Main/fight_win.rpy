# Version event: 1
# Version game: 0.23

label fight_win():
    narrador "[enemy_figth.n] has been defeated!!!"
    $ fight_return = True
    # EXP

    if enemy_figth.exp > 0:
        $ talk = RPGPlayer.add_exp(enemy_figth.exp)
        narrador "+[enemy_figth.exp] EXP"
        narrador "[talk]"

    return