# Version event: 4
# Version game: 0.6

default thrillerbark_cemetery = False

label thriller_bark_cemetery():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ game.location = "thriller_bark_cemetery"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_thrillerbark()
    jump m_thriller_bark_cemetery

label m_thriller_bark_cemetery():
    if not thrillerbark_cemetery:
        show robin at center with dissolve
        robin "What a gloomy and neglected place..." 
        robin "It seems this old cemetery has been abandoned for quite some time, but it has its charm..."

        show robin:
            linear 0.4 xalign 0.15
        pause 0.4

        show yamato at center with dissolve
            
        yamato "Let's stay alert, Captain. There's something about this place that doesn't sit right with me... it could be dangerous..."
        
        show yamato:
            linear 0.4 xalign 0.85

        pause 0.4

        show nami with dissolve:
            yalign 1.0
            xalign 0.5        
        
        #cara de berrys de nami a futuro

        nami "It could be dangerous, but these tombs must be full of treasures..." 
        nami "With a shovel, we could find many valuable things!"

        window hide
        hide nami
        hide robin
        hide yamato
        with dissolve
        window auto

        $ thrillerbark_cemetery = True   

    menu:
        "Dig a grave" if not game.clock.night:
            if not tool_shovel:
                narrador "Shovel required"
                jump m_thriller_bark_cemetery

            jump thriller_bark_cemetery_dig

        "Back":
            jump thriller_bark_mid


label thriller_bark_cemetery_dig():
    
    $ n_random = renpy.random.randint(0, 100)

    if (10 >= n_random):
        narrador "There was nothing of value."

    else:
        $ ui_interface = False
        # 16% = 85 * 100 / 90 // aprox +10%
        if (85 <= n_random):
            robin "Something is coming out of the tomb!"
            
            window hide
            show expression enemy_zombie.image with Dissolve(1.0):
                xalign 0.5
                yalign 0.5

            pause 0.8
            window auto

            nami "Ahhh! A zombieee!"

            call fight_start pass (enemy_pass = enemy_zombie) from _thrillerbark_cemetery_dig
            
            hide expression enemy_zombie.image with Dissolve(0.8)

            if not fight_return:
                $ game.clock.next()
                jump thriller_bark_mid

            $ music_thrillerbark()

            player "Return to your tomb and rest!"
            yamato "Go back to sleep hahaha!"

        $ rewards = []
        
        $ n_reward = renpy.random.randint(0, 5)
        if n_reward > 0:
            $ rewards.append((n_reward, "gold"))
            $ gold += n_reward

        $ n_reward = renpy.random.randint(1, 80)
        $ rewards.append((n_reward, "berries"))
        $ berries += n_reward

        call screen reward_window with Dissolve(0.5)
        $ ui_interface = True

    $ game.clock.next()

    if game.clock.night:
        narrador "It got late, and you preferred to return to your cabin."
        jump ship_captains_cabin

    jump thriller_bark_cemetery