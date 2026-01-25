# Version event: 2
# Version game: 0.28

default uta_naked = 0

label event_uta_naked:
    if uta_naked == 0:
        player "[uta.n] since I saw you, I can't stop thinking about your sexy and provocative figure..."
        player "The idea of having a sexy musical idol on my crew... I have so many things in mind!"
        player "How about you get naked for me and show me who you really are..."
        show uta c1 shame with dissolve  
        uta "You always gave me so much confidence and endlessly praised me..."
        uta "But I don't know... It might be a little fast for me."
        player "You know you can trust me, right?... I think I've given you enough trust, what do you say?"
        $ uta_naked += 1
    else:
        player "[uta.n] what do you think about opening up to me again and showing me how you really are..."
        uta "You always gave me so much confidence and endlessly praised me..."


    menu:
        "I just want to admire your beauty...":
            call uta_check pass (check_love = 15, check_lust = 15) from _uta_naked_check

            player "Your beauty is unmatched... I want to see you as you are, I just want to admire your beauty..."
            show uta c1 shame with dissolve
            uta "You give me so much confidence, Captain... You never stop charming me with your words."
            uta "What do you think, do you like what you see?!?... I hope I meet your expectations..."


        "Undress and pose naked for me...":
        
            player "Undress and pose naked for me..."
            show uta c1 annoyed with dissolve
            uta  "Once again, ordering me around, [player.n]... You have such bad manners..."
            uta "I doubt you'll ever change. I'll pretend nothing happened here!!!"
            jump uta_refuse


    window hide
    show uta c1_naked with dissolve
    pause 1
    show uta neutral with Dissolve(0.2)
    window auto
    
    $ uta_lust += 3
    narrador "[uta.n] lust +3"

    show uta c1 with dissolve

    jump uta_goodbye