# Version event: 2
# Version game: 0.17

label event_dream:
    if hancock_crew:
        jump event_dream_nrh

    jump sleep

label sleep_dream:
    $ player_sp = RPGPlayer.true_mana_max()
    $ game.clock.sleep()

    player "What??"
    #player "Where did they all go?!?!"    
    player "Damn... Don't tell me that..."
    player "It was all just a dream!!... Fuck I can't believe it!!!"
    player "This has to come true at some point... I have to do it!"

    jump ship_captains_cabin