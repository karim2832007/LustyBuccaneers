# Version event: 6
# Version game: 0.3

label shells_town():
    window hide
    show screen screen_black with Dissolve(0.6)


    $ game.location = "shells_town"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    play ambient "market" fadein 1.0
    $ music_time_day()
    call m_shells_town from _call_shells_town

label m_shells_town():
    $ ui_berries = False

    menu:
        "Shop":
            jump shop_shells_town
        "Go for a walk with" if not game.clock.night:
            jump take_walk_with
        "Bounty board":
            jump bounty_board
        "Newspapers":
            jump newspapers
        "Go to bar" if not game.clock.night and game.clock.getDay >= 15:
            jump shells_town_bar
        "Back":
            jump ship_mid


label shop_shells_town():
    $ ui_berries = True

    menu:
        "Buy":
            jump buy_shells_town
        "Sell":
            jump sell_shells_town
        "leave":
            jump m_shells_town

label buy_shells_town():
    menu:
        "Buy Materials":
            jump buy_materials_shells_town
        "Buy Items":
            jump buy_items_shells_town
        "Buy Gifts":
            jump buy_gifts_shells_town
        "Buy Tools":
            jump buy_tools_shells_town
        "Buy Eternal Poses":
            jump buy_eternal_poses_shells_town
        "Back":
            jump shop_shells_town

label buy_gifts_shells_town():
    menu:
        "Bracelet{space=140}-100 Berries":
            if berries >= 100:
                $ bracelet_nami += 1
                $ berries -= 100
                narrador "-100 [Berries.n] | +1 Bacelet"
            else:
                player "I have [berries] [Berries.n], but I need 100."

        "Book{space=190}-100 Berries":
            if berries >= 100:
                $ book_robin += 1
                $ berries -= 100
                narrador "-100 [Berries.n] | +1 Book"
            else:
                player "I have [berries] [Berries.n], but I need 100."

        "Earrings{space=160}-100 Berries":
            if berries >= 100:
                $ earrings_yamato += 1
                $ berries -= 100
                narrador "-100 [Berries.n] | +1 Earrings"
            else:
                player "I have [berries] [Berries.n], but I need 100."

        "Bento{space=190}-150 Berries":
            if berries >= 150:
                $ bento_yamato += 1
                $ berries -= 150
                narrador "-150 [Berries.n] | +1 Bento"
            else:
                player "I have [berries] [Berries.n], but I need 150."

        "Tangerine{space=140}-150 Berries":
            if berries >= 150:
                $ tangerine_nami += 1
                $ berries -= 150
                narrador "-150 [Berries.n] | +1 Tangerine"
            else:
                player "I have [berries] [Berries.n], but I need 150."

        "Totem{space=180}-150 Berries":
            if berries >= 150:
                $ totem_robin += 1
                $ berries -= 150
                narrador "-150 [Berries.n] | +1 Totem"
            else:
                player "I have [berries] [Berries.n], but I need 150."

        ">>>":
            menu buy_gifts_shells_town_2:
                "Flowers{space=140}-100 Berries":
                    if berries >= 100:
                        $ flowers += 1
                        $ berries -= 100
                        narrador "-100 [Berries.n] | +1 Flowers"
                    else:
                        player "I have [berries] [Berries.n], but I need 100."

                "Chocolate{space=140}-150 Berries":
                    if berries >= 150:
                        $ chocolate += 1
                        $ berries -= 150
                        narrador "-150 [Berries.n] | +1 Chocolate"
                    else:
                        player "I have [berries] [Berries.n], but I need 150."

                "Perfume{space=140}-200 Berries":
                    if berries >= 200:
                        $ perfume += 1
                        $ berries -= 200
                        narrador "-200 [Berries.n] | +1 Perfume"
                    else:
                        player "I have [berries] [Berries.n], but I need 200."

                "<<<":
                    jump buy_gifts_shells_town

                "Back":
                    jump buy_shells_town
            
            jump buy_gifts_shells_town_2

        "Back":
            jump buy_shells_town

    jump buy_gifts_shells_town


label buy_materials_shells_town():
    menu:
        "Gold{space=140}-60 Berries":
            if berries >= 60:
                $ gold += 1
                $ berries -= 60
                narrador "-60 [Berries.n] | +1 Gold"
            else:
                player "I have [berries] [Berries.n], but I need 60."

        "iron{space=140}-30 Berries":
            if berries >= 30:
                $ iron += 1
                $ berries -= 30
                narrador "-30 [Berries.n] | +1 iron"
            else:
                player "I have [berries] [Berries.n], but I need 30."

        "Wood{space=140}-15 Berries":
            if berries >= 15:
                $ wood += 1
                $ berries -= 15
                narrador "-15 [Berries.n] | +1 Wood"
            else:
                player "I have [berries] [Berries.n], but I need 15."

        "Food{space=140}-15 Berries":
            if berries >= 15:
                $ food += 1
                $ berries -= 15
                narrador "-15 [Berries.n] | +1 Food"
            else:
                player "I have [berries] [Berries.n], but I need 15."

        "Paper{space=140}-15 Berries":
            if berries >= 15:
                $ paper += 1
                $ berries -= 15
                narrador "-15 [Berries.n] | +1 Paper"
            else:
                player "I have [berries] [Berries.n], but I need 15."

        "Fabric{space=140}-15 Berries":
            if berries >= 15:
                $ fabric += 1
                $ berries -= 15
                narrador "-15 [Berries.n] | +1 Fabric"
            else:
                player "I have [berries] [Berries.n], but I need 15."

        "Back":
            jump buy_shells_town

    jump buy_materials_shells_town

label buy_items_shells_town:
    menu:
        "Cannon ball{space=140}-25 Berries":
            if berries >= 25:
                $ cannonball += 1
                $ berries -= 25
                narrador "-25 [Berries.n] | +1 Cannon ball"
            else:
                player "I have [berries] [Berries.n], but I need 25."
        
        "Water{space=140}-20 Berries":
            if berries >= 20:
                $ water += 1
                $ berries -= 20
                narrador "-20 [Berries.n] | +1 Water"
            else:
                player "I have [berries] [Berries.n], but I need 20."            

        "Back":
            jump buy_shells_town

    jump buy_items_shells_town

label sell_shells_town():
    menu:
        "Gold{space=140}+40 Berries" if gold > 0:
            $ gold -= 1
            $ berries += 40
            narrador "-1 gold | +40 [Berries.n]"

        "iron{space=140}+20 Berries" if iron > 0:
            $ iron -= 1
            $ berries += 20
            narrador "-1 iron | +20 [Berries.n]"

        "Wood{space=140}+10 Berries" if wood > 0:
            $ wood -= 1
            $ berries += 10
            narrador "-1 wood | +10 [Berries.n]"

        "Food{space=140}+10 Berries" if food > 0:
            $ food -= 1
            $ berries += 10
            narrador "-1 food | +10 [Berries.n]"

        "5xFood{space=140}+50 Berries" if food >= 5:
            $ food -= 5
            $ berries += 50
            narrador "-5 food | +50 [Berries.n]"

        "Paper{space=140}+10 Berries" if paper > 0:
            $ paper -= 1
            $ berries += 10
            narrador "-1 paper | +10 [Berries.n]"

        "Fabric{space=140}+10 Berries" if fabric > 0:
            $ fabric -= 1
            $ berries += 10
            narrador "-1 fabric | +10 [Berries.n]"

        "Back":
            jump shop_shells_town

    jump sell_shells_town

label take_walk_with:
    menu:
        "[nami.n]":
            jump event_nami_walk

        "[robin.n]":
            jump event_robin_walk
            
        "[yamato.n]":
            jump event_yamato_walk

        "Back":
            jump m_shells_town


label buy_tools_shells_town():
    menu:
        "Rod{space=140}-300 Berries" if not tool_rod:
            if berries >= 300:
                $ tool_rod = True
                $ berries -= 300
                narrador "-300 [Berries.n] | +1 Rod"
            else:
                player "I have [berries] [Berries.n], but I need 300."

        "Shovel{space=140}-300 Berries" if not tool_shovel:
            if berries >= 300:
                $ tool_shovel = True
                $ berries -= 300
                narrador "-300 [Berries.n] | +1 Shovel"
            else:
                player "I have [berries] [Berries.n], but I need 300."

        "Back":
            jump buy_shells_town

    jump buy_tools_shells_town


label buy_eternal_poses_shells_town():
    menu:
        "Eternal Pose: Thriller Bark{space=140}-200 Berries" if not epose_thriller_bark:
            if berries >= 200:
                $ epose_thriller_bark = True
                $ berries -= 200
                narrador "-200 [Berries.n] | +1 Eternal Pose: Thriller Bark"
            else:
                player "I have [berries] [Berries.n], but I need 200."

        "Eternal Pose: Elegia{space=140}-300 Berries" if not epose_elegia and obj_newcoo_1:
            if berries >= 300:
                $ epose_elegia = True
                $ berries -= 300
                narrador "-300 [Berries.n] | +1 Eternal Pose: Elegia"
            else:
                player "I have [berries] [Berries.n], but I need 300."

        "Eternal Pose: Dressrosa{space=140}-400 Berries" if not epose_dressrosa and obj_newcoo_2:
            if berries >= 400:
                $ epose_dressrosa = True
                $ berries -= 400
                narrador "-400 [Berries.n] | +1 Eternal Pose: Dressrosa"
            else:
                player "I have [berries] [Berries.n], but I need 400."

        "Back":
            jump buy_shells_town

    jump buy_eternal_poses_shells_town