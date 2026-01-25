# Version event: 4
# Version game: 0.21

label ar_nanohana():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True
    $ game.location = "ar_nanohana"
    $ arabasta_location = "Nanohana"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_nanohana

label m_ar_nanohana():
    if Arabasta.h == 1:

        show vivi neutral at center with dissolve  

        vivi "Well, we finally made it! Welcome to Nanohana."

        show nami neutral at left with dissolve

        nami "Wow, it's a massive city! It's filled with all kinds of shops and goods everywhere!"
        vivi "That's right, Nanohana is the kingdom's main port city."
        vivi "In addition to the port, it's known for its abundance of bazaars, and thanks to its proximity to an oasis, it doesn't face many issues from the current drought."
        vivi "It's a bustling hub of activity and trade!"
        vivi "But we'll have time to explore it later..."

        show vivi serious at center with dissolve

        vivi "[karoo.n], come here!"

        hide nami
        pause 0.5
        show vivi:
            linear 0.4 xalign 0.85
        show karoo at left with dissolve

        vivi "You're such a fast boy... I'm confident I can entrust this important task to you."
        vivi "We'd only slow you down, and we can't afford to waste any time..."
        vivi "I want you to go to the palace in Alubarna by yourself... You know exactly where it is..."
        vivi "Deliver this letter to my father, and only to him!! It's crucial that he receives it personally."
        vivi "When they see you, they'll recognize you and let you through without any issues."
        vivi "In this letter, I explain everything I've discovered along with [igaram.n]."
        vivi "Everything related to Baroque Works, and even all the information I gathered about their leader, [crocodile.n], is detailed here."
        vivi "I also wrote about [player.n] and his crew, that I've returned with strong friends I trust, and that they will be a great help!"
        show vivi neutral with Dissolve(0.2)         
        vivi "This is a mission of vital importance, [karoo.n]!! But I know you'll do a great job..."
        vivi "Go... Thank you for everything, and take care of the water while you're in the desert!"
        player "Good luck, [karoo.n]!"
        vivi "Run, go to my father!"
        vivi "Tell him we can save the kingdom!!"

        hide karoo with moveoutleft

        show vivi:
            linear 0.4 xalign 0.50

        menu:
            "Well thought out!!":
                player "Very well thought out [vivi.n]! Stay calm [karoo.n] will take care of it..."
                player "Everything will be fine, we also have to get down to work!"
                show vivi shame with Dissolve(0.2) 
                vivi "Y-yes yes... Thanks for your kind words!"

                $ vivi_love += 2
                narrador "[vivi.n] Love +2"

            "Stay calm":
                player "Stay calm [karoo.n] will take care of it..."
                player "Everything will be fine, we also have to get down to work!"
                vivi "Thanks for your kind words!"

                $ vivi_love += 1
                narrador "[vivi.n] Love +1"

        pause 0.5
        show vivi serious with Dissolve(0.2)
        vivi "Alright, we have work to do as well..."
        vivi "First and foremost, we need to stock up on water and anything else we might need... Also, we need to get a map."
        player "A map?"
        vivi "Yes, it's vital..."
        vivi "We have to cross the desert, and lately, there have been many sandstorms, among other dangers to overcome."
        vivi "With a map, you could easily navigate and avoid getting lost."
        vivi "This way, we can save water and avoid unnecessary delays."
        player "Understood. We'll get the map, food, water, and anything else we think is important."
        player "Let's get to it!"
        show vivi neutral with Dissolve(0.2)
        vivi "Perfect, I'll give you this task. I have to keep a low profile and not make myself seen easily... I am the princess after all."
        vivi "When you have everything ready, take a look at the map, and let's head to Yuba!"

        hide vivi with dissolve

        $ Arabasta.h = 2

    $ ui_berries = False
    
    menu:
        "Shop" if not game.clock.night:
            jump shop_ar_nanohana

        "Coast" if not game.clock.night:
            jump ar_nanohana_coast
        
        "Map" if map_arabasta and not game.clock.night:
            jump map_arabasta

        "Back":
            jump arabasta


label shop_ar_nanohana():
    $ ui_berries = True

    menu:
        "Buy":
            jump buy_ar_nanohana
        "Sell":
            jump sell_ar_nanohana
        "leave":
            jump m_ar_nanohana

label buy_ar_nanohana():
    menu:
        "Buy Provisions":
            jump buy_provisions_ar_nanohana
        "Buy Items":
            jump buy_items_ar_nanohana

        "Buy Clothes" if Arabasta.h >= 14:
            jump buy_clothes_ar_nanohana

        "Back":
            jump shop_ar_nanohana

label buy_provisions_ar_nanohana():
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
            jump buy_ar_nanohana

    jump buy_provisions_ar_nanohana

label buy_items_ar_nanohana:
    menu:
        "Cannon ball{space=140}-30 Berries":
            if berries >= 30:
                $ cannonball += 1
                $ berries -= 30
                narrador "-30 [Berries.n] | +1 Cannon ball"
            else:
                player "I have [berries] [Berries.n], but I need 30."

        "Map of Arabasta{space=140}-400 Berries" if not map_arabasta:
            if berries >= 400:
                $ map_arabasta = True
                $ berries -= 400
                narrador "-400 [Berries.n] | +1 Map of Arabasta"
            else:
                player "I have [berries] [Berries.n], but I need 400."

        "Beer{space=140}-40 Berries":
            if berries >= 40:
                $ beer += 1
                $ berries -= 40
                narrador "-40 [Berries.n] | +1 Beer"
            else:
                player "I have [berries] [Berries.n], but I need 40."

        "Back":
            jump buy_ar_nanohana

    jump buy_items_ar_nanohana


label buy_clothes_ar_nanohana:
    menu:
        "Nami: Desert Dancer Outfit{space=140}-500 Berries" if not nami_c2 and Arabasta.h >= 14:
            if berries >= 500:
                $ nami_c2 = True
                $ berries -= 500
                narrador "-500 [Berries.n] | +1 Desert Dancer Outfit"
                call nami_c2_outfit from _call_nami_c2_outfit

            else:
                player "I have [berries] [Berries.n], but I need 500."

            #narrador "This event is in development, try again in the next version."

        "Back":
            jump buy_ar_nanohana

    jump buy_clothes_ar_nanohana


label sell_ar_nanohana():
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
            jump shop_ar_nanohana

    jump sell_ar_nanohana


