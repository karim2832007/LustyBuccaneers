# Version event: 2
# Version game: 0.16

label enemy_zala_fight:
    narrador "You pillaged the enemy ship."
    
    $ n_reward_gold = renpy.random.randint(1, 4)
    $ n_reward_berries = renpy.random.randint(0, 80)
    $ n_reward_cannonball = renpy.random.randint(0, 4)

    call rewards_give from _call_enemy_zala_fight

    if zala_wanted:
        $ zala_wanted = False
        narrador "Mision complete: Reward 600 Berries"
        $ n_reward_berries = 600
        call rewards_give from _call_enemy_zala_fight_wanted

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

    show zala c1 with dissolve
    $ music_time_day()
    hide screen screen_black with Dissolve(0.3)
    window auto

    zala "You're tough for a nobody..."
    zala "But I don't think you understand what you're getting yourself into..."
    player "Shut up!!! I'm thinking what to do with you..."
    zala "Have you already gotten everything from me, what else do you want?"
    player "(Haha I can think of one or two things...)"

    show nami c1 with dissolve:
        xalign 0.85
        yalign 1.0

    if not epose_cactus_island:

        nami "Look, Captain, we found this while searching through their belongings!"
        player "(Always interrupting...)"
        nami "What is it? An Eternal Pose?"

        $ epose_cactus_island = True
        narrador "Eternal Pose: Cactus Island"

        nami "Yes, Captain. From the name engraved on it, it will lead us to..."
        nami "[CactusIsland.n]"
        player "Sounds good! We'll see what this island has for us..."
        player "This is an opportunity that doesn't come often... I'll keep it."

    else:
        player "(But not now...)"


    player "Get her out of my sight, I'm not in the mood anymore..."
    zala "Hahaha, you have no idea what you're getting yourself into, nobody... When MY GROUP finds out about this..."
    player "Take her away and set her free... I have no interest in this anymore, and I fear it even less..."
    nami "Yes, Captain!"
    zala "You'll regret this!... See you soon..."


    window hide
    window auto
    
    show nami:
        xoffset 0
        linear 0.5 xoffset 1000

    show zala:
        xoffset 0
        linear 0.8 xoffset 1500

    pause 0.8

    hide nami
    hide zala

    $ game.clock.next()
    jump expression game.location
    #jump m_zala_call