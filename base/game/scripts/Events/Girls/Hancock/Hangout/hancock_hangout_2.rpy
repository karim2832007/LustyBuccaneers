# Version event: 2
# Version game: 0.12

label hancock_hangout_2:
    player "How are you doing, [hancock.n]? You seem to be in a great mood today!"
    hancock "What's up, [player.n]? Do I really look like I'm in a good mood?! Are you implying that I'm not usually in a good mood?"   
    player "Not at all! I didn't mean it like that! Don't misunderstand me..."
    show hancock c1 happy with dissolve
    hancock "Hahaha!!... I'm just joking, [player.n]!!"
    pause 0.5
    show hancock c1 neutral with dissolve
    hancock "During my travels outside of Amazon Lily, I used to hear people's comments about me..."
    hancock "Most people say I have an arrogant gaze, that I'm selfish, cruel, spoiled, and beautiful..."
    player "(Especially the last part!)"
    hancock "But the truth is, everyone is wrong!"    
    player "!!!"  
    hancock "The reality is that I don't want to show weakness, you understand..." 
    hancock "Being in charge of the Kuja island, being a woman in this great pirate era, and considering my past..."
    hancock "It was a huge responsibility on my shoulders..."
    hancock "But now that I'm on this ship... Everything has changed, it's an opportunity for me to be who I really want to be!!"  
    show hancock c1 shame with dissolve
    hancock "The truth is that I'm a loyal, loving, sensitive, and vulnerable woman..."
    hancock "I don't know why I'm telling you all this!!..."
    hancock "It always happens when I'm with you, [player.n], I just can't stop talking about my feelings without any guard up!!"
    hancock "Sorry for bothering you with these things!"


    menu:
        "I had no idea you really felt that way!":
            player "I had no idea you really felt that way!"
            player "I really appreciate you telling me all of that..."
            player "But you should know that what people say is wrong!"
            player "I always knew that's how you really are!"
            show hancock c1 shame with dissolve
            hancock "Do you really mean it?!?"
            player "Yes, there are small details that don't escape my notice... And not just that..."
            player "People didn't get everything wrong..."
            show hancock c1 neutral with dissolve
            hancock "Oh no?!?... What didn't they get wrong?"
            player "That you're truly gorgeous, [hancock.n]!, and not just physically. Your attitude, even though it's an act, fits you perfectly..."
            player "It adds a touch of seduction and charm that's even greater! And I'm sure the side of you no one knows is even better!"
            show hancock c1 shame with dissolve
            hancock "I never thought you had those thoughts about me, [player.n]…"
            hancock "I'm really flattered and surprised!"
            show hancock c1 neutral with dissolve            
            hancock "I hope we can continue having these conversations in the future…"
            $ hancock_love += 1
            $ hancock_lust += 1
            narrador "[hancock.n] lust and love +1"

        "The people are right in a way!":
            
            player "Anyway, the people are right in a way, hahahaha!"
            player "My first impression was that you were a selfish, cruel, and spoiled woman, with a pretty bad temper!"
            show hancock c1 annoyed with dissolve
            hancock "..."
            hancock "One opens up and expresses her feelings, and this is what she gets... You don't know how to deal with women, [player.n]!"
            player "Wait, don't take it the wrong way, it was a joke!!"

            $ hancock_love -= 1
            narrador "[hancock.n] love -1"

   

    return