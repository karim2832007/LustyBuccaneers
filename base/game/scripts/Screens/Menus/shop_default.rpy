# Version event: 1
# Version game: 0.30

label shop_default():
    $ ui_berries = True

    menu:
        "Buy":
            jump buy_shop_default
        "Sell":
            jump sell_shop_default
        "leave":
            $ ui_berries = False
            return

label buy_shop_default():
    menu:
        "Buy Provisions":
            jump buy_provisions_shop_default

        "Buy Items":
            jump buy_items_shop_default

        "Back":
            jump shop_default

label buy_provisions_shop_default():
    menu:
        "Food{space=140}-15 Berries":
            if berries >= 15:
                $ food += 1
                $ berries -= 15
                narrador "-15 [Berries.n] | +1 Food"
            else:
                player "I have [berries] [Berries.n], but I need 15."

        "Water{space=140}-60 Berries":
            if berries >= 60:
                $ water += 1
                $ berries -= 60
                narrador "-60 [Berries.n] | +1 Water"
            else:
                player "I have [berries] [Berries.n], but I need 60."

        "Back":
            jump buy_shop_default

    jump buy_provisions_shop_default

label buy_items_shop_default:
    menu:
        "Cannon ball{space=140}-30 Berries":
            if berries >= 30:
                $ cannonball += 1
                $ berries -= 30
                narrador "-30 [Berries.n] | +1 Cannon ball"
            else:
                player "I have [berries] [Berries.n], but I need 30."

        #"Beer{space=140}-40 Berries":
        #    if berries >= 40:
        #        $ beer += 1
        #        $ berries -= 40
        #        narrador "-40 [Berries.n] | +1 Beer"
        #    else:
        #        player "I have [berries] [Berries.n], but I need 40."

        "Back":
            jump buy_shop_default

    jump buy_items_shop_default


label sell_shop_default():
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
            jump shop_default

    jump sell_shop_default


