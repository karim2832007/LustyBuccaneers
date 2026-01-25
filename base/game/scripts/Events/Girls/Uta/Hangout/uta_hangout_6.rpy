# Version event: 2
# Version game: 0.28

label uta_hangout_6:
    player "How about you, tell me something about you or your past [uta.n], something important that has marked you..."
    player "I like to know the history of the people..."
    show uta serious with Dissolve(0.2)
    uta "Well, [player.n], I have something interesting to tell you."
    uta "When I was a kid, I used to sing to myself when I was scared."
    uta "Now that I think of it... I still do."
    player "That's beautiful. Your voice has always been your shield."
    uta "...And my prison too, sometimes."  

    menu:
        "Let it be your wings instead":
            player "Your voice shouldn't hold you back, it should let you fly."
            player "You will always have my support and that of everyone who cares about you."
            show uta happy with Dissolve(0.2)     
            uta "Thank you, [player.n]... Your words really mean a lot to me."
            uta "I'll remember that... next time I feel caged."
                        
            $ uta_love += 2
            narrador "[uta.n] love +2"

        "Maybe someday, you'll sing just for fun again":     
            player "No pressure, no expectations. Just joy."
            player "If you don't take care of yourself, how will you take care of others?"
            show uta neutral with Dissolve(0.2)   
            uta "...I hope so. I really do."

            $ uta_love += 1
            narrador "[uta.n] love +1"


    return