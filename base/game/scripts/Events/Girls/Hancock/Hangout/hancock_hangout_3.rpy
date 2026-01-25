# Version event: 2
# Version game: 0.12

label hancock_hangout_3:
    hancock "How's it going, [player.n]? I've noticed that everyone in the crew calls you Captain..."  
    hancock "And I want to make something clear to you..." 
    hancock "Even though I agreed to join your crew, it's only temporary..." 
    hancock "I'll help you for a while and participate in these adventures, but then I'll return to Amazon Lily with my people..."


    menu:
        "You will have to obey my orders from now on":
            player "I understand that you were the Empress and ruled the Kuja at your will, but now the situation is different..."
            player "On this ship, everyone follows my orders... You'll have to get used to that."
            player "You're not the exception... You'll understand that soon enough."
            show hancock c1 annoyed with dissolve
            hancock "It seems like you're very mistaken, [player.n]..."
            hancock "I won't continue this discussion... My stance is clear, and I won't accept any further argument!"
            player "(I'll have to work more with [hancock.n], I can't let this issue get out of hand)"

            $ hancock_love -= 1
            narrador "[hancock.n] love -1"

        "I understand your situation":
            
            player "I understand your hatred and fears from the past, so I'll do my best to earn your trust..."
            player "I'll make sure you realize that my intentions are good and that there's nothing harmful behind them..."
            player "Here, no one orders anyone around, but I set the course for the group because they trust me with that responsibility."
            hancock "Your intentions might not be bad, [player.n]..."
            hancock "But that remains to be seen. I hope you're really as trustworthy as you say."
            player "You'll see, that's why all the girls trust me."
            player "(It's only a matter of time before you really get to know me, [hancock.n], and fall at my feet, hahaha)"
            $ hancock_love += 1
            narrador "[hancock.n] love +1"


    return