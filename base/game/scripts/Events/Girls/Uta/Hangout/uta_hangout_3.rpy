# Version event: 2
# Version game: 0.28

label uta_hangout_3:
    uta "If you could create a perfect world, [player.n]... what would it be like?"
    player "Mnmnm that's an interesting question..."

    menu:
        "One where everyone is free":
            player "One where everyone is free to be themselves"
            player "A world where no one has to hide who they are or live in fear."
            uta "...That sounds wonderful. I wish I had thought more like you back then."
            $ uta_love += 2
            narrador "[uta.n] love +2"

        "Maybe, a place with endless music and laughter":
            
            player "A place with endless music and laughter"
            player "Just like your concerts... endless joy, endless rhythm!"
            player "And your sexy figure and voice on stage!"
            show uta c1 shame with Dissolve(0.2)
            uta "Haha, then I hope you'd be in charge of stage effects!"
            uta "I'd like to have you around... That's a great idea you told me about!"

            $ uta_love += 1
            $ uta_lust += 2
            narrador "[uta.n] Love +1 and lust +2"


        "I'm fine with this world as long as you're in it":
            
            player "I'm fine with this world as long as you're in it"
            player "To me, any world is perfect if you're there, [uta.n]."
            show uta c1 shame with Dissolve(0.2)
            uta "That's unfair!... Now I'm blushing."

            $ uta_love += 2
            $ uta_lust += 2
            narrador "[uta.n] Love +2 and lust +2"


    return