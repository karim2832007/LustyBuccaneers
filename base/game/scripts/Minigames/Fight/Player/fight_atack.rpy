# Version event: 1
# Version game: 0.23

label fight_attack():
    # Player attack
    $ damage, criti_attack = RPGPlayer.attack()

    if criti_attack:
        narrador "A CRITICAL HIT!"

    $ talk = enemy_figth.take_damage(damage = damage)

    narrador "[talk]"

    return