# Version event: 2
# Version game: 0.12

label hancock_hangout_4:
    hancock "How's it going, [player.n], how are you?" 
    hancock "It's great to see you, I'm doing really well. How about you?... You look taller today, it's pretty strange..."
    player "Hahaha, I don't think so, it's probably just your impression... Though, you flatter me..."
    hancock "How tall do you think I am?"


    menu:
        "180 cm":
            player "Mmmm... I think you're about... 180 cm, I'd say..."
            hancock "I knew you didn't have a good eye! I'm far from that..."
            hancock "Height is a synonym for beauty, you know?... 180 cm is far below my level..."

            $ hancock_love -= 1
            narrador "[hancock.n] love -1"

        "191 cm":
            
            player "Mmmm... I'd say you're just over 190 cm, but not by much!"
            show hancock c1 happy with dissolve
            hancock "That's exactly right!... 191 cm, to be exact. You must've just gotten lucky!"
            
            $ hancock_love += 1
            narrador "[hancock.n] love +1"

        "Is height really important?":
            player "Mmmm... I'm not very good at these guessing games, besides, is height really that important?"
            show hancock serious with Dissolve(0.2)
            hancock "How boring... I didn't think you were the type to care about the inside..."
            hancock "Height is a synonym for beauty, you know?... I'm exactly 191 cm, I hope you remember that..."


            $ hancock_love -= 1
            narrador "[hancock.n] love -1"


    show hancock c1 neutral with dissolve    
    hancock "And I'm not just tall, I've got a sexy figure too..." 
    player "(And you sure are sexy!!!)"
    hancock "My measurements are 111 - 61 - 91... I train constantly to stay in shape..."  
    player "You're truly a beauty, [hancock.n]..."
    hancock "Hahaha! You have to stay fit, especially when you're as young as I am..." 
    hancock "How old do you think I am?"

    menu:
        "35 years old":
            
            player "Mmmm… Maybe 35?!"
            hancock "What?!?"
            player "I mean, 30 years old…"
            show hancock c1 annoyed with dissolve
            hancock "I'm 29!!!"
            hancock "You've got a lot to learn about women..."
            hancock "I won't take up any more of your time, I've got more important matters to attend to!"

            $ hancock_love -= 1
            narrador "[hancock.n] love -1"

        "21 years old":
            
            player "Mmmm... This one's harder..."
            hancock "What are you implying?!?"
            player "I'd say around 21 years old..."
            show hancock c1 happy with dissolve
            hancock "Hahaha, you sure know how to talk to a woman... I'm 29, just so you know."
            hancock "I won't take up any more of your time, I've got things to attend to. Until next time!"
            $ hancock_love += 1
            narrador "[hancock.n] love +1"

    return