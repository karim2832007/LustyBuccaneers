# Version event: 3
# Version game: 0.23

label vivi_hangout_4:
    player "You seem different today, [vivi.n]... As if you were taller."
    vivi "Taller? Hahaha, do you really think so?... That's not exactly one of my best features..."
    player "(I have no doubts about that!)"
    vivi "Let's play a little game... Tell me, how tall do you think I am?"


    menu:
        "169cm":
            player "I think around 1.69m."
            show vivi c1 happy with Dissolve(0.2)
            vivi "Seriously?!? You're really good at this!!"
            vivi "You have a great eye!!"
            show vivi c1 shame with Dissolve(0.2)
            vivi "I'll think about what your reward will be..."

            $ vivi_love += 2
            $ vivi_lust += 1
            narrador "[vivi.n] Love +2 and lust +1"

        "180cm":
            
            player "I think around 1.80m."
            vivi "Eh?! You just made me taller than I actually am!"
            vivi "Don't worry... I'll take it as a compliment haha!"
            vivi "But you lost... I thought you had a better eye [player.n]!"

            $ vivi_love += 1
            narrador "[vivi.n] love +1"

        "Does that matter?":
            player "Does height really matter?"
            vivi "Booo, how boring [player.n]! It was just a game..."
            vivi "I guess it doesn't really matter... but it's funny how people pay attention to those details."

            $ vivi_love -= 1
            narrador "[vivi.n] love -1"
    

    return