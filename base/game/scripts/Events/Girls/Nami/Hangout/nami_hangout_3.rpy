# Version event: 1
# Version game: 0.14

label nami_hangout_3:
    nami "I notice you often stare at me, Captain..."
    player "(You're so sexy, [nami.n]... The only thing I can think about is having you in my bed...)"
    player "Of course, I admire your beauty, [nami.n]..."
    nami "Hahaha, you're so flattering, Captain... Since you stare at me so much, how about we make a little bet..."
    nami "How tall do you think I am? If you guess right, you'll get a prize, otherwise, you owe me:"

    menu:
        "180 cm":
            player "Hmm... I think you should be around... 180 cm, I'd say..."
            nami "I knew you wouldn't guess right!! I'm 170 cm tall, Captain!"

            show nami c1 happy with dissolve
            nami "You owe me now! I'll collect later!"

        "170 cm":
            player "Hmm... I would say about 170 cm!"
            nami "That's exactly my height! It must have been pure luck!" 

            show nami c1 happy with dissolve
            nami "But we never closed the bet! You'll have to pay more attention next time! Hahahaa!"
            nami "I'll get back to my work!"

            $ nami_love += 2
            narrador "[nami.n] Love +2"

    return