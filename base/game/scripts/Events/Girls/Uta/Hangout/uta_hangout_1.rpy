# Version event: 2
# Version game: 0.28

label uta_hangout_1:

    uta "[player.n], can I ask you something a bit personal?"
    player "Of course. What's on your mind?"

    show uta c1 serious with Dissolve(0.2)

    uta "...Have you ever spent years chasing someone, just to hear them say they care about you?"
    uta "For me, that person was my adopted father. He raised me. Protected me. But one day, he just... left."
    uta "I know he had reasons, but all I wanted was to hear him say I mattered..."
    uta "So I sang. I created. I want to made the whole world listen... hoping maybe he would."


    menu:
        "You matter, [uta.n]...":
            player "You matter, [uta.n]. Even if he never says it, you always did."
            player "Your adopted father may not have said it enough, but I'm sure you mattered deeply to him."
            player "And you matter now. Not because of your voice, but because of who you are."
            show uta c1 shame with Dissolve(0.2)
            uta "...That means more to me than I can say, [player.n]..."
            uta "Maybe I needed to hear that more than anything."

            $ uta_love += 2
            
            narrador "[uta.n] Love +2"

        "You don't need his approval. You're stronger than that.":
            player "You don't need his approval. You're stronger than that."          
            player "You built yourself. Your music, your world—it's yours. Not his."
            uta "...I want to believe that. Maybe I can let go... a little."

            $ uta_love += 1
            narrador "[uta.n] love +1"

        "Maybe he never deserved to be called your father":
            player "Maybe he never deserved to be called your father"          
            player "If he left you like that, maybe he doesn't deserve the title of 'dad'."
            show uta c1 annoyed with Dissolve(0.2)
            uta "Don't say that..."
            uta "I know he made mistakes, but... he was there for me. At least once."
            uta "I can't erase that part of my heart, even if I tried..."

            $ uta_love -= 1
            narrador "[uta.n] love -1"


            #more with more progrese story


    return