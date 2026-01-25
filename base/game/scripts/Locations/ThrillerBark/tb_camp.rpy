# Version event: 5
# Version game: 0.10

default tb_camp_hancock = True

label tb_camp():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ game.location = "thriller_bark_camp"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_thrillerbark()
    jump m_tb_camp

label m_tb_camp():
    if tb_camp_hancock:
        narrador "While advancing through the dense forest, you hear two women talking in the distance..."

        unknown "I'm sorry, I can't help you with what you need."

        window hide
        show hancock serious at center with dissolve
        pause 1.0
        window auto

        call set_name_hancock from _call_set_name_hancock

        show hancock with dissolve:
            yalign 1.0
            xalign 0.5
            linear 0.4 xalign 0.1

        pause 0.4

        show hancock:
            yalign 1.0
            xalign 0.1

        show victoria with dissolve:
            yalign 1.0
            xalign 0.9

        unknown "I'm sorry to tell you [hancock.n] that the doctor is not on this island at the moment."

        unknown "He is traveling and it's impossible to know when he will return..."

        show hancock annoyed with dissolve

        hancock "How is this possible! Tell me where the doctor is right now!... I have no time to lose..."

        hancock "Don't test my patience!... You must have a way to contact him..."

        unknown "All I know is that he had a very important job to do, I don't even know his whereabouts... And I have no way to contact him."

        hancock "I need a [SakuraFlower.n] to heal my sister, this is an emergency!"

        hancock "You are his secretary or butler, or whatever... But I know you're close to him... How can you not contact him?!"

        unknown "As I said, I can't help you."

        hancock "Don't make me repeat it one more time!... You leave me no choice but to use force if you keep insisting on this position..."

        unknown "You won't gain anything by force..."

        unknown "I know how strong you are, and that I'm no match for you, but it's in vain... Because I don't have the information you're looking for..."

        hancock "Uffff..."

        hancock "What a waste of time... I'm leaving."


        hide victoria with dissolve

        show hancock with dissolve:
            yalign 1.0
            xalign 0.1
            linear 0.4 xalign 0.5

        pause 0.4

        player "(Woooow... who the hell is this woman?!)"
        player "(She must be one of the most beautiful women of all the seas... She should be part of my crew...)"
        player "(She doesn't look like a friendly person... She's really angry...)"
        player "(She seems to be looking for some kind of flower, better not get in her way... For now...)"

        hancock "..."


        hide hancock with dissolve

        pause 0.2


        player "(It seems she's gone... What a bad mood she was in... her attitude only makes her sexier!!)"

        player "[robin.n]!!"


        pause 0.2

        show robin at center with dissolve

        robin "Yes, Captain!"

        player "Did you hear the same thing I did?... They were talking about a strange plant or herb, do you have any idea which one they were referring to?"

        robin "Captain, yes, the [SakuraFlower.n] are quite a strange medicinal flower, but I've read about it."

        robin "It can be very difficult to obtain as it has very specific growth conditions."

        robin "It's a very useful flower for making medicines if used correctly."

        robin "For this reason, it could be useful on our journeys, maybe it's a good time to fix the ship's library..."

        robin "In the library, I could read many books and acquire knowledge that helps us on our journey."

        robin "It's an ideal place to carry out my research, with enough time I could find out about this herb or any other topic."

        player "I understand, I'll consider the library..."

        player "It might be useful to inform ourselves and learn more about this flower... but first, let's talk to this other girl."

        $ ship_library_unlocked = True
        hide robin with dissolve

        player "Hello, what was all that about?"

        show victoria at center with dissolve

        unknown "I'm sorry you had to hear that conversation, it's just a client who couldn't get what she wanted..."

        call set_name_victoria from _call_set_name_victoria

        victoria "I'm [victoria.n], and this is my humble shop, I sell all kinds of items... Maybe something could interest you..."

        victoria "If you're interested, I can show you what I have to offer."

        player "Great, my name is [player.n] and it'll be a pleasure doing business with you."


        window hide
        window auto
        $ tb_camp_hancock = False

    show victoria with dissolve:
        yalign 1.0
        xalign 0.5

    menu:
        "Shop":
            jump shop_thriller_bark

        "Back":
            hide victoria with dissolve
            $ ui_interface = False
            call tb_forest_call pass (bg = 5) from _call_tb_forest_05_camp
            call screen forest_arrows() with Dissolve(1.0)

            if _return == 1:
                jump tb_camp
            else:
                jump tb_forest



label shop_thriller_bark():
    $ ui_berries = True

    menu:
        "Buy":
            jump buy_thriller_bark
        "Leave":
            $ ui_berries = False
            jump m_tb_camp


label buy_thriller_bark():
    menu:
        #"Buy Items":
        #    jump buy_items_thriller_bark
        #"Buy Gifts":
        #    jump buy_gifts_thriller_bark
        "Buy Tools":
            jump buy_tools_thriller_bark
        "Back":
            jump shop_thriller_bark


label buy_tools_thriller_bark():
    menu:
        "Eternal Pose: Amazon Lily{space=140}-300 Berries" if not epose_amazon_lily:
            if berries >= 300:
                $ epose_amazon_lily = True
                $ berries -= 300
                narrador "-300 [Berries.n] | +1 Eternal Pose: Amazon Lily"
            else:
                player "I have [berries] [Berries.n], but I need 300."

        "Back":
            jump buy_thriller_bark

    jump buy_tools_thriller_bark