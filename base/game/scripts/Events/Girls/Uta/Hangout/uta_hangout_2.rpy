# Version event: 2
# Version game: 0.28

label uta_hangout_2:

    player "Hi [uta.n]!"
    uta "Hi [player.n], I can't get this melody out of my head... but I forgot the lyrics I wrote for it."
    player "Maybe I can help? Sing it for me?"
    show uta c1 happy with Dissolve(0.2)
    uta "Haha, are you sure you want to hear my humming for hours?"

    menu:
        "Absolutely":
            player "Absolutely. I want to hear every note until you remember"
            player "I want to hear it all, [uta.n]. Until you remember... Or until you invent something better."
            show uta c1 neutral with Dissolve(0.2)
            uta "You're strange, but I like that about you..."

            $ uta_love += 1
            narrador "[uta.n] love +1"

        "What you feel is enough":
            
            player "Maybe the lyrics don't matter, what you feel is enough"
            player "The melody alone is already full of emotion."
            show uta c1 neutral with Dissolve(0.2)
            uta "You might be right... sometimes emotions speak louder than words."


            $ uta_love += 2
            narrador "[uta.n] love +2"

   

    return