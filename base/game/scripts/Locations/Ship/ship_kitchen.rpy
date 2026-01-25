# Version event: 7
# Version game: 0.40

label ship_kitchen():
    $ _window_hide()
    show screen screen_black with Dissolve(0.6)
    
    $ ui_interface = True
    $ game.location = "ship_kitchen"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)

    $ ambient_ship()
    $ music_time_day()
    call m_ship_kitchen from _call_ship_kitchen

label m_ship_kitchen():
    menu:
        "Cooking with..." if not game.clock.night:
            jump cooking_ship_kitchen

        "Healing":
            jump kitchen_heal

        "Back":
            jump ship_mid

label cooking_ship_kitchen():
    menu:
        "[nami.n]":
            show nami c1 with dissolve
            nami "Oh, Captain! Good to see you here! Did you come to help me in the kitchen?"
            player "That's exactly why I'm here! Let's get it done faster together!"
            nami "Your help would be greatly appreciated! Thank you, Captain!"

            $ nami_love += 2
            narrador "[nami.n] Love +2"            

        "[robin.n]":
            show robin c1 with dissolve
            robin "Captain, do you want to help me with the kitchen chores?"
            player "I came just for that! Together we'll get it done faster!"
            robin "That's very considerate of you! We'll definitely do a better job together!"

            $ robin_love += 2
            narrador "[robin.n] Love +2"

        "[yamato.n]":
            show yamato c1 with dissolve
            yamato "Captain, good to see you! I'm not very good at these tasks, can you help me?"
            player "I came just for that! Together we'll get it done faster!"
            yamato "Great! Thanks for helping me out! If we finish quickly, I'll have more time to continue training."

            $ yamato_love += 2
            narrador "[yamato.n] Love +2"

        "[perona.n]" if perona_crew:
            show perona c1 with dissolve
            player "Hello [perona.n]! Since you're here, how about helping me with today's cooking..." 
            player "I don't know who handled the meals at [ThrillerBark.n], but I'm sure you know a thing or two… and if not, I can teach you!"

            if perona_love < 5: 
                narrador "Requires [perona.n] love greater than 5"
                show perona anger with Dissolve(0.2)
                perona "Just because you're the Captain doesn't mean I'll do everything you say..."
                perona "I was never in charge of the kitchen at [ThrillerBark.n], my slaves took care of that... You don't think I'm your slave... Do you!?!"
                perona "I have better things to do... Until next time..."

            else: 
                perona "I was never in charge of the kitchen at [ThrillerBark.n], my slaves took care of that..."
                perona "But if you teach me, Captain, maybe I could learn..."
                perona "Tell me what to do, it could be fun..."

                $ perona_love += 2
                narrador "[perona.n] Love +2"

        "[hancock.n]" if hancock_crew:
            jump hancock_cook

        "[vivi.n]" if vivi_crew:
            jump vivi_cook

        "[uta.n]" if uta_crew:
            jump uta_cook

        "Back":
            jump m_ship_kitchen

    $ game.clock.next()
    jump expression game.location


label kitchen_heal():
    $ ui_hp = True
    $ missing_hp = RPGPlayer.true_hp_max() - player_hp
    $ req_food = (missing_hp + 99) // 100

    menu:
        "Healing with food{space=140}+100 HP":
            if player_hp >= RPGPlayer.true_hp_max():
                narrador "Your life is at maximum, you don't need to eat."
                jump kitchen_heal

            if food >= 1:
                narrador "The girls prepared several dishes for you to recover and rest."
                player "Kampai!"

                $ _window_hide()
                $ food -= 1
                $ RPGPlayer.heal(heal_amount = 100)
                
            else:
                narrador "You don't have enough Food!"
                
            jump kitchen_heal

        "Full healing with food{space=140}+[missing_hp] HP -[req_food] Food" if food > 0 and missing_hp > 0:
            if food >= req_food:
                narrador "The girls prepared a massive feast for you to recover and rest."
                player "Kampai!"

                $ _window_hide()
                $ food -= req_food
                $ RPGPlayer.heal(heal_amount = missing_hp)
            else:
                narrador "You don't have enough Food!"
            jump kitchen_heal

        "Back":
            $ ui_hp = False
            jump m_ship_kitchen