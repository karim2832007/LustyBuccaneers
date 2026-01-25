# Version event: 2
# Version game: 0.28

label uta_hangout_5:
    uta "Do you think... I could write a song just for one person?"
    player "Why not? Songs made from real feelings are the strongest."
    uta "I wonder what kind of song I'd write... if it were for you..."

    menu:
        "I'd love to be your inspiration":
            player "I'd be honored if my presence made its way into your music."
            player "I hope the song you write for me has a little spice too... Hahaha!"
            show uta shame with Dissolve(0.2)     
            uta "...You're kind of dangerous with words, [player.n]..."
            uta "Hehe... I'll keep that in mind!"

            $ uta_love += 2
            $ uta_lust += 1
            narrador "[uta.n] Love +2 and lust +1"

        "It would be a beautiful song, I'm sure of it":     
            player "Anything from your heart would be beautiful."
            player "I would love to hear it someday!"
            show uta happy with Dissolve(0.2)   
            uta "Thank you... You always know what to say."

            $ uta_love += 1
            narrador "[uta.n] love +1"

    uta "Would you... listen if I sang only for you?"
    player "Always!"
    show uta c1 happy with Dissolve(0.2)
    uta "Well, how about I improvise something right now?!"
    player "I would love to, I'm sure I'll enjoy it"
    uta "I've sung so many times... but with you, I get nervous..."
    show uta shame with Dissolve(0.2)    
    uta "Close your eyes... Please"
    player "Hahahha you are so beautiful... I'm sure I'll enjoy it more this way"

    narrador "She sings a soft melody, just for you. It's raw and imperfect... And beautiful."

    $ uta_love += 2
    narrador "[uta.n] love +2"

    return