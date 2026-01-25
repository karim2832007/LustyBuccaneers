# Version event: 3
# Version game: 0.23

label vivi_hangout_1:
    player "How about you, tell me something about your past [vivi.n], something important that has marked you..."
    player "I like to know the history of the people I share this journey with..."
    show vivi serious with Dissolve(0.2)
    vivi "Well, [player.n], my past is no secret, but there are things I prefer not to remember..."
    vivi "Alabasta has suffered too much. I have seen my home on the brink of destruction, I have seen my people suffer injustices..."
    vivi "But I have sworn to do everything in my power to protect them..."
    vivi "Thanks to you and all the girls, I was able to do it last time... But what about the future?"
    vivi "Sometimes I wonder if I will ever truly be able to guarantee peace in my kingdom..."
    

    menu:
        "You won't be alone in this":
            player "You don't have to carry all this alone, Vivi..."
            player "You will always have my support and that of everyone who cares about you."
            player "Together, we will find a way to guarantee peace for [Arabasta.n]."
            show vivi neutral with Dissolve(0.2)     
            vivi "Thank you, [player.n]... Your words really mean a lot to me."
            vivi "It's good to know that I don't have to face all this alone."
                        
            $ vivi_love += 2
            narrador "[vivi.n] love +2"

        "Your determination is admirable, but...":     
            player "Your dedication is admirable, but you also need to think about yourself, Vivi."
            player "If you don't take care of yourself, how will you take care of others?"
            show vivi neutral with Dissolve(0.2)   
            vivi "Maybe you're right... Sometimes I forget to think about myself."
            vivi "I promise I'll try... but it won't be easy."

            $ vivi_love += 1
            narrador "[vivi.n] love +1"


    return