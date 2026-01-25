# Version event: 1
# Version game: 0.23

label fight_died():
    if event_gameover:
        $ hide_label = "fight_hide"
        jump expression event_gameover
    
    narrador "The enemy is too strong..."
    narrador "After a tough battle, you feel too weak to keep fighting."
    narrador "[enemy_figth.n] has defeated you!!!"

    narrador "Your crew manages to rescue you and take you back to your ship."

    $ hide_label = "fight_hide_die"
    $ game.clock.next()
    jump ship_captains_cabin