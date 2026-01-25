# Version event: 1
# Version game: 0.5

label enemy_alvida_fight:
    narrador "You pillaged the enemy ship."
    
    $ n_reward_gold = renpy.random.randint(1, 4)
    $ n_reward_berries = renpy.random.randint(0, 80)
    $ n_reward_cannonball = renpy.random.randint(0, 4)

    call rewards_give from _call_enemy_alvida_fight

    if alvida_wanted:
        $ alvida_wanted = False
        narrador "Mision complete: Reward 300 Berries"
        $ n_reward_berries = 300
        call rewards_give from _call_enemy_alvida_fight_wanted

    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None

    $ game.location = "ship_captains_cabin"
    scene BG locations:
        blur 3

    show alvida c1 anger with dissolve
    $ music_time_day()
    hide screen screen_black with Dissolve(0.3)
    window auto

    alvida "And now what do you want!?!... you've already taken all my loot!"
    alvida "Don't think this will be the end of it! You've only won this time..." 
    alvida "What more do you want from me?"

    jump m_alvida_call