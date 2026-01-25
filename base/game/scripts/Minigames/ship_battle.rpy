# Version event: 3
# Version game: 0.5

define ships_weapon = [40]
define ships_hp_max = [200]

default ship_player_lvl = 0
default ship_player_weapon = 0
default ship_player_health = 200

default ship_enemy = None
default ship_enemy_atack = 30
default ship_enemy_health = 100
default ship_enemy_health_max = 100

default boarding_rate = 5
default boarding_rate_base = 5
default run_rate = 80
default run_rate_base = 80

default ship_enemy_destroyed = False

define rate_up = 5

label ship_battle():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ ui_interface = False
    $ game.location = "ship_battle"
    show screen s_ship_battle_ship

    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    #$ music_time_day()
    play music "battle" fadein 2.0

    call start_ship_battle from _call_ship_battle
    call screen s_ship_battle with Dissolve(0.5)
    jump ship_battle

style ship_battle:
    xpos 320
    ypos 90

label start_ship_battle():
    if Seas_Ships[choice_id] == "Small ship":
        $ ship_enemy = None
        $ ship_enemy_atack = 30
        $ ship_enemy_health = ship_enemy_health_max = 100
        $ run_rate = 80 #+up
        $ run_rate_base = 80
        $ boarding_rate = 5 + rate_up
        $ boarding_rate_base = 5
        $ ship_enemy_destroyed = False

    elif Seas_Ships[choice_id] == "Alvida ship":
        $ ship_enemy = enemy_alvida
        $ ship_enemy_atack = 30
        $ ship_enemy_health = ship_enemy_health_max = 180
        $ run_rate = 75 #+up
        $ run_rate_base = 75
        $ boarding_rate = 5 + rate_up
        $ boarding_rate_base = 5
        $ ship_enemy_destroyed = False

    elif Seas_Ships[choice_id] == "Zala ship":
        $ ship_enemy = enemy_zala
        $ ship_enemy_atack = 35
        $ ship_enemy_health = ship_enemy_health_max = 200
        $ run_rate = 80 #+up
        $ run_rate_base = 80
        $ boarding_rate = 5 + rate_up
        $ boarding_rate_base = 5
        $ ship_enemy_destroyed = False


    return
    
screen s_ship_battle_ship():
    zorder -40

    add "BG locations"

    frame:
        background None
        area (320, 90, 1280, 768)
                
        if Seas_Ships[choice_id] == "Small ship":
            if ship_enemy_destroyed:
                add "minigames ship_battle small_ship" at ship_destroyed
            else:
                add "minigames ship_battle small_ship" at ship_on
                
        elif Seas_Ships[choice_id] == "Alvida ship":
            if ship_enemy_destroyed:
                add "minigames ship_battle alvida_ship" at ship_destroyed
            else:
                add "minigames ship_battle alvida_ship" at ship_on

        elif Seas_Ships[choice_id] == "Zala ship":
            if ship_enemy_destroyed:
                add "minigames ship_battle zala_ship" at ship_destroyed
            else:
                add "minigames ship_battle zala_ship" at ship_on


    add "minigames ship_battle background_battle_ship_up" at ship_seas_on


screen s_ship_battle_hp():
    zorder -20

    frame:
        background None
        yoffset 40
        xsize 800
        ysize 100

        vbox:
            spacing 10

            #add "minigames ship_battle bar_ship_battle"
            bar value ship_player_health:
                range ships_hp_max[ship_player_lvl]
                xysize(800,100)
                left_bar "minigames ship_battle bar_ship_battle"
                right_bar "minigames ship_battle bar_ship_battle_back"

            text [player.name]:
                font gui.interface_text_font
                outlines [(7, "#231d1b", 0, 0)]
                color "#ffffff"
                xoffset 40
                xalign 0
                yalign 0.5
                size 60
        
        text "[ship_player_health]/[ships_hp_max[ship_player_lvl]]":
            font gui.interface_text_font
            color "#110f0e"
            xalign 0.5
            yalign 0.5
            size 30

    frame:
        background None
        xalign 1.0
        yoffset 40
        xsize 800
        ysize 100

        vbox:
            spacing 10

            #add "minigames ship_battle bar_ship_battle":
            #    zoom -1

            bar value ship_enemy_health at flip:
                range ship_enemy_health_max
                xysize(800,100)
                left_bar "minigames ship_battle bar_ship_battle"
                right_bar "minigames ship_battle bar_ship_battle_back"
                

            text Seas_Ships[choice_id]:
                font gui.interface_text_font
                outlines [(7, "#231d1b", 0, 0)]
                color "#ffffff"
                xoffset -40
                xalign 1.0
                yalign 0.5
                size 60

        text "[ship_enemy_health]/[ship_enemy_health_max]":
            font gui.interface_text_font
            color "#110f0e"
            xalign 0.5
            yalign 0.5
            size 30

screen s_ship_battle():
    zorder -20

    use s_ship_battle_hp

    # TEXTS
    frame:
        background None
        yoffset 350
        xoffset 10
        xsize 300
        ysize 130
        
        hbox:
            spacing 0

            add "obj_cannonball"

            text "x[cannonball]":
                font gui.interface_text_font
                outlines [(7, "#231d1b", 0, 0)]
                color "#ffffff"
                #xoffset -50
                xalign 0.0
                #text_align 0.0
                yalign 0.5
                size 60


    frame:
        background None
        xalign 1.0
        yoffset 400
        xsize 400
        ysize 130

        vbox:
            xalign 0.5
            yalign 0.5

            text "BOARDING RATE:":
                font gui.interface_text_font
                outlines [(6, "#231d1b", 0, 0)]
                color "#ffffff"
                size 35

            text "{}%".format(round(boarding_rate)):
                xalign 0.5
                yalign 0.5
                font gui.interface_text_font
                outlines [(6, "#231d1b", 0, 0)]
                color "#ffffff"
                yoffset -10
                size 50
                    
    frame:
        background None
        xalign 1.0
        yoffset 550
        xsize 400
        ysize 130

        vbox:
            xalign 0.5
            yalign 0.5

            text "RUN RATE:":
                font gui.interface_text_font
                outlines [(6, "#231d1b", 0, 0)]
                color "#ffffff"
                size 35

            text "{}%".format(round(run_rate)):
                xalign 0.5
                yalign 0.5
                font gui.interface_text_font
                outlines [(6, "#231d1b", 0, 0)]
                color "#ffffff"
                yoffset -10
                size 50
    
    # BUTTONS
    hbox:
        xoffset 85
        yoffset 910
        spacing 50

        frame:
            background None
            xsize 400
            ysize 130
            
            button:
                action Jump("ship_atack")
                xalign 0.5
                yalign 0.5
                at ship_battle_zoom

                add "minigames ship_battle buttons"
                    

                text "ATTACK":
                        font gui.interface_text_font
                        color "#6b5440"
                        xalign 0.5
                        yalign 0.5
                        size 60

        frame:
            background None
            xsize 400
            ysize 130
            
            button:
                action Jump("ship_repair")
                xalign 0.5
                yalign 0.5
                at ship_battle_zoom

                add "minigames ship_battle buttons"

                text "REPAIR":
                        font gui.interface_text_font
                        color "#6b5440"
                        xalign 0.5
                        yalign 0.5
                        size 60

        frame:
            background None
            xsize 400
            ysize 130
            
            button:
                action Jump("ship_boarding")
                xalign 0.5
                yalign 0.5
                at ship_battle_zoom

                add "minigames ship_battle buttons"

                text "BOARDING":
                        font gui.interface_text_font
                        color "#6b5440"
                        xalign 0.5
                        yalign 0.5
                        size 60

        frame:
            background None
            xsize 400
            ysize 130
            
            button:
                action Jump("ship_run")
                xalign 0.5
                yalign 0.5
                at ship_battle_zoom

                add "minigames ship_battle buttons"

                text "RUN":
                        font gui.interface_text_font
                        color "#6b5440"
                        xalign 0.5
                        yalign 0.5
                        size 60

label ship_atack():
    show screen s_ship_battle_hp

    # Determine infinite cannon cheat
    $ inf_cannon = cheat_mg_ship_inf_cannon if 'cheat_mg_ship_inf_cannon' in globals() else False

    if cannonball > 0 or inf_cannon:
        if not inf_cannon:
            $ cannonball -= 1

        $ talk_random = renpy.random.choice([
                _("Fire at will!!!"),
                _("Open fire!!!"),
                _("Fire the cannons!!"),
            ])

        player "[talk_random]"

        play sound "cannonball"

        # Determine always hit cheat
        $ always_hit = cheat_mg_ship_always_hit if 'cheat_mg_ship_always_hit' in globals() else False

        if always_hit or renpy.random.choice([True, True, True, True, False]):
            # efecto golpe
            $ ship_enemy_health -= ships_weapon[ship_player_weapon]
            

            if ship_enemy_health <= 0:
                $ ship_enemy_health = 0
                $ ship_enemy_destroyed = True

            $ talk_random = renpy.random.choice([
                    _("Right on target, Captain!!!"),
                    _("We're tearing them apart!!"),
                    _("We've hit the shot, Captain!!"),
                ])

            yamato "[talk_random]"

            if ship_enemy_destroyed:
                jump ship_battle_win

        else:
            play sound "cannonball_fail"

            $ talk_random = renpy.random.choice([
                    _("We've missed, Captain!!"),
                    _("We need to improve our aim, we missed!!"),
                    _("Adjusting the aim, Captain, we missed!"),
                ])

            yamato "[talk_random]"
    else:
        $ talk_random = renpy.random.choice([
                _("We're out of ammunition, Captain!"),
                _("We're out of cannonballs!"),
            ])

        yamato "[talk_random]"

        call screen s_ship_battle with Dissolve(0.5)
        jump ship_battle

    jump ship_next_turn

label ship_repair():
    if ship_player_health >= ships_hp_max[ship_player_lvl]:
        yamato "The ship is now in perfect condition, Captain!"
        call screen s_ship_battle with Dissolve(0.5)
        jump ship_battle

    show screen s_ship_battle_hp
    show screen screen_alpha_choice

    menu m_ship_repair:
        "Wood{space=140}+50hp":
            hide screen screen_alpha_choice
            if wood >= 1:
                $ wood -= 1
                $ talk_random = renpy.random.choice([
                        _("Repair the hull urgently!"),
                        _("Repair the ship!"),
                    ])

                player "[talk_random]"

                play sound "repair"
                $ ship_player_health += 50

                if ship_player_health > ships_hp_max[ship_player_lvl]:
                    $ ship_player_health = ships_hp_max[ship_player_lvl]
        
            else:
                $ talk_random = renpy.random.choice([
                        _("Captain, we're out of wood."),
                        _("We're out of wood reserves, Captain."),
                    ])

                yamato "[talk_random]"

                show screen screen_alpha_choice
                jump m_ship_repair

        "Back":
            hide screen screen_alpha_choice
            call screen s_ship_battle with Dissolve(0.5)
            jump ship_battle

    jump ship_next_turn

label ship_boarding():
    $ n_random = renpy.random.randint(0, 100)

    # Boarding cheat: force success
    $ boarding_cheat = cheat_mg_ship_boarding if 'cheat_mg_ship_boarding' in globals() else False

    if boarding_cheat or (boarding_rate >= n_random):
        if Seas_Ships[choice_id] in ["Alvida ship", "Zala ship"]:
            jump ship_battle_fight

        else:
            narrador "The ship surrendered without a fight."
            jump ship_battle_win

    narrador "You couldn't board successfully."
    jump ship_next_turn


label ship_run():
    $ n_random = renpy.random.randint(0, 100)
    $ print(n_random)

    # Escape cheat: force success
    $ escape_cheat = cheat_mg_ship_escape if 'cheat_mg_ship_escape' in globals() else False

    if escape_cheat or (run_rate >= n_random):
        narrador "You escaped successfully."
        $ hide_label = "ship_battle_hide"
        jump ship_captains_cabin

    narrador "You couldn't escape successfully."
    jump ship_next_turn

label ship_next_turn():
    $ talk_random = renpy.random.choice([
            _("The enemy is preparing to attack us!!"),
            _("We are under attack!!"),
            _("The enemy is targeting us, Captain!"),
        ])

    nami "[talk_random]"

    play sound "cannonball"

    # Enemy miss cheat
    $ enemy_miss_cheat = cheat_mg_ship_enemy_miss if 'cheat_mg_ship_enemy_miss' in globals() else False

    if enemy_miss_cheat:
        # Enemy forced to miss
        play sound "cannonball_fail"
        narrador "The enemy has missed the shot."
    else:
        if renpy.random.choice([True, True, True, False, False]):
            $ ship_player_health -= ship_enemy_atack

            if ship_player_health <= 0:
                jump ship_battle_gameover
            else:
                $ talk_random = renpy.random.choice([
                        _("The enemy has hit us, Captain!"),
                        _("We have leaks in the hull, Captain!"),
                        _("We've been hit!"),
                    ])

                yamato "[talk_random]"
        else:
            play sound "cannonball_fail"
            narrador "The enemy has missed the shot."
        
    # Infinite HP cheat: restore player HP after enemy attack
    $ inf_hp_cheat = cheat_mg_ship_inf_hp if 'cheat_mg_ship_inf_hp' in globals() else False

    if inf_hp_cheat:
        $ ship_player_health = ships_hp_max[ship_player_lvl]

    # update
    $ run_rate = run_rate_base - (run_rate_base* (1-(ship_player_health / ships_hp_max[ship_player_lvl])))/3
    $ boarding_rate = boarding_rate_base + rate_up + (100-boarding_rate_base) * (1-((ship_enemy_health / (ship_enemy_health_max))))/1.1

    call screen s_ship_battle with Dissolve(0.5)
    jump ship_battle

label ship_battle_win():
    narrador "[Seas_Ships[choice_id]] has been defeated."

    narrador "You pillaged the enemy ship."
    if ship_enemy_destroyed:
        narrador "Since the ship sank, we couldn't recover all the loot."

    $ rewards = []
    $ n_reward_berries = 0
    $ n_reward_cannonball = 0

    # MODIFICAR

    if Seas_Ships[choice_id] == "Small ship":
        $ n_reward_gold = renpy.random.randint(1, 3)

        if not ship_enemy_destroyed:
            $ n_reward_berries = renpy.random.randint(0, 50)
            $ n_reward_cannonball = renpy.random.randint(0, 4)

    elif Seas_Ships[choice_id] == "Alvida ship":
        $ n_reward_gold = renpy.random.randint(1, 4)

        if not ship_enemy_destroyed:
            $ n_reward_berries = renpy.random.randint(0, 80)
            $ n_reward_cannonball = renpy.random.randint(0, 4)

    elif Seas_Ships[choice_id] == "Zala ship":
        $ n_reward_gold = renpy.random.randint(2, 5)

        if not ship_enemy_destroyed:
            $ n_reward_berries = renpy.random.randint(0, 120)
            $ n_reward_cannonball = renpy.random.randint(0, 5)

    else:
        $ n_reward_gold = 4

    # Max loot cheat: override rewards to generous values
    $ max_loot_cheat = cheat_mg_ship_max_loot if 'cheat_mg_ship_max_loot' in globals() else False

    if max_loot_cheat:
        $ n_reward_gold = 5
        $ n_reward_berries = 120
        $ n_reward_cannonball = 5

    call rewards_give from _call_ship_battle_win

    $ hide_label = "ship_battle_hide"
    $ game.clock.next()
    jump ship_captains_cabin

label ship_battle_gameover():

    $ talk_random = renpy.random.choice([
            _("We're sinking, Captain!"),
            _("The enemy is boarding us!!"),
        ])

    yamato "[talk_random]"
    
    narrador "Your ship was plundered."

    $ rewards = []
    if gold > 1:
        $ n_reward = renpy.random.randint(1, int(gold/2))
        $ rewards.append((-n_reward, "gold"))
        $ gold -= n_reward
    
    if berries > 1:
        $ n_reward = renpy.random.randint(int(berries/4), int(berries/2))
        $ rewards.append((-n_reward, "berries"))
        $ berries -= n_reward

    call screen reward_window with Dissolve(0.5)
    $ hide_label = "ship_battle_hide"
    $ game.clock.next()
    jump ship_captains_cabin

label ship_battle_hide():
    hide screen s_ship_battle_ship
    hide screen s_ship_battle
    hide screen s_ship_battle_hp
    $ ui_interface = True
    return

# FIGHT
label ship_battle_fight():
    $ hide_label = "ship_battle_hide"
    call fight_start pass (enemy_pass = ship_enemy, enemy_location = "ship_battle_fight") from _fight_ship_battle

    if not fight_return:
        $ game.clock.next()
        jump ship_captains_cabin

    #pause
    jump expression enemy_figth.image.lower() + "_fight"