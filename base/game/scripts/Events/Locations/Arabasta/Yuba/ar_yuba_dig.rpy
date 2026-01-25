# Version event: 2
# Version game: 0.21

default yuba_dig = 0

label ar_yuba_dig():

    if yuba_dig == 0:
        show toto at center with dissolve

        toto "Ohhh, it's you, young one. [player.n], right?... What are you doing here?"
        
        show toto pervert with Dissolve(0.2)
        toto "Where are the rest of the girls, resting?"
        player "Hey old man, I came to help you dig..."

        
        show toto happy with Dissolve(0.2)

        toto "I won't deny that a bit of youthful energy would be useful... And you even have your own shovel..."
        toto "Help is always appreciated!"
        player "I've been watching you for a while as the girls rest..."
        player "Honestly, I'm surprised you can live like this... You barely have water, you're alone... But you keep digging."
        player "Tell me, what's the secret? What keeps you going?"

        toto "Yuba's oasis is still alive and won't be defeated by the sand, young one!"
        toto "This oasis is very important for the kingdom, that's why the king entrusted it to me!"

        player "So you're just following the king's orders?"

        toto "This isn't just about following orders!"
        toto "He entrusted this land to me, but I have my own goals to achieve!"
        toto "..."
        toto "You're a smart young man... You remind me of myself when I was younger..."

        show toto pervert with Dissolve(0.2)
        toto "Surrounded by women! Life was beautiful back then!"
        toto "That's exactly my dream... I'll make Yuba an oasis full of beautiful women!"
        toto "Women from all over Alabasta will come to visit!"
        toto "And not just from Alabasta, women from neighboring islands and all over the seas will come!"
        toto "Hahaha, a paradise on earth!!!"

        player "Wow, a city full of women from all the seas?! You're a genius!!"
        player "You have a great idea! Now I'm really motivated to dig!"
        show toto happy with Dissolve(0.2)
        toto "That's the spirit, young one!!"
        player "[toto.n], I will help you achieve your dream!"

        toto "Thank you, young one, I knew you would understand me!"
        toto "The first step is to recover the water, we must keep digging!"

    narrador "You spend time digging"
    $ yuba_dig += 1

    window hide
    show screen screen_black with Dissolve(0.3)
    hide toto with dissolve
    show toto at center with dissolve
    hide screen screen_black with Dissolve(0.1)
    window auto

    if yuba_dig == 1:
        narrador "The hole in Yuba is now bigger..."
        show toto at center with dissolve
        toto "Wow, we've made so much progress in such a short time... And most of the work was done by you, youth is incredible..."
        toto "With your help, we will surely make it!"


    elif yuba_dig < 3:
        narrador "You begin to feel the soil getting moist."
        show toto at center with dissolve
        player "Old man, there's still no water..."
        toto "You must have faith, young one... We have a great goal, we can't give up halfway."
        toto "The soil is moist and easier to dig through, that's a big step... The goal is near!"


    else:
        show toto happy with Dissolve(0.2)
        toto "It's water! We've reached the water!!!"
        toto "Look, there's so much!!!"
        toto "Look... The water is flowing!!!"
        toto "Didn't I tell you, [player.n]?"
        toto "This land is strong... Yuba is still alive!"


        window hide
        hide toto with dissolve
        show BG arabasta ar_yuba_oasis_on with Dissolve(2) 
        $ oasis_yuba = True
        pause 0.6
        window auto

        show toto happy with Dissolve(0.2)

        player "Awesome! Now what?"
        toto "Now anything I set my mind to is possible, I have to start making preparations!"
        toto "Come see me later, I have things to get ready!"
        player "Got it, see you later, old man!"



    $ game.clock.next()

    if game.clock.night:
        narrador "It got late, and you preferred to return to your cabin."
        jump ship_captains_cabin

    jump ar_yuba_oasis
