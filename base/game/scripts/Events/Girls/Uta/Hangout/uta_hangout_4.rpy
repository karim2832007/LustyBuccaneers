# Version event: 2
# Version game: 0.28

label uta_hangout_4:
    player "You seem different today, [uta.n]... As if you were taller."
    uta "Taller? Hahaha, do you really think so?... That's not exactly one of my best features..."
    player "(I have no doubts about that!)"
    uta "Let's play a little game... Tell me, how tall do you think I am?"

    menu:
        "169cm":
            player "I think around 1.69m."
            show uta c1 happy with Dissolve(0.2)
            uta "Seriously?!? You're really good at this!!"
            uta "You have a great eye!!"
            show uta c1 shame with Dissolve(0.2)
            uta "I'll think about what your reward will be..."

            $ uta_love += 2
            $ uta_lust += 1
            narrador "[uta.n] Love +2 and lust +1"

        "180cm":
            
            player "I think around 1.80m."
            uta "Eh?! You just made me taller than I actually am!"
            uta "Don't worry... I'll take it as a compliment haha!"
            uta "But you lost... I thought you had a better eye [player.n]!"

            $ uta_love += 1
            narrador "[uta.n] love +1"

        "Does that matter?":
            player "Does height really matter?"
            uta "Booo, how boring [player.n]! It was just a game..."
            uta "I guess it doesn't really matter... but it's funny how people pay attention to those details."

            $ uta_love -= 1
            narrador "[uta.n] love -1"

    

    uta "Let's change the subject..."
    player "Great!"
    uta "Okay! Important question time! What do you think my favorite food is?"

    menu:
        "Seafood noodles!":
            player "Mnmnmnm..."
            player "Definitely seafood noodles. You look like someone who enjoys the ocean's flavor."
            show uta c1 happy with Dissolve(0.2)

            uta "Wrong! But that's a good guess!"
            uta "Haha! I'll give you half a point."


            $ uta_love += 1
            narrador "[uta.n] Love +1"

        "Sweet bread":
            
            player "Sweet bread? You seem like the sweet type"
            show uta c1 happy with Dissolve(0.2)
            uta "Bingo! You got it!"
            uta "But how did you know...? You're suspiciously good at this..."

            $ uta_love += 2
            narrador "[uta.n] love +2"

        "I didn't know we were playing a game":
            player "I didn't know we were playing a game"
            uta "Ugh, boring! You totally ruined the moment."

            $ uta_love -= 1
            narrador "[uta.n] love -1"

    

    return