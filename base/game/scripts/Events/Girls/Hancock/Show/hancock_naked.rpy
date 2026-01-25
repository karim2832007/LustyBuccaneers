# Version event:3
# Version game: 0.23

default hancock_naked = 0

label event_hancock_naked:
    if hancock_naked == 0:
        player "[hancock.n] Since I saw you, I can't stop thinking about your sexy and provocative figure..."
        player "How about you get naked for me and show me who you really are?"
        show hancock c1 shame with dissolve  
        hancock "You always gave me so much confidence and endlessly praised me..."
        hancock "But I don't know..."
        player "You know you can trust me, right?... I think I've given you enough trust, what do you say?"
        $ hancock_naked += 1
    else:
        player "[hancock.n] what do you think about opening up to me again and showing me how you really are..."
        hancock "You always gave me so much confidence and endlessly praised me..."


    menu:
        "I only wish to admire your beauty...":
            call hancock_check pass (check_love = 15, check_lust = 15) from _hancock_naked_check

            player "I only wish to admire your beauty... Show me who you really are!"
            show hancock c1 neutral with dissolve 
            hancock "[player.n] I always wanted to do this, to be completely free in front of you..."
            hancock "What do you think? Do you like what you see?!... You're truly privileged to see this… I don't do this for just anyone!"

        "Undress and pose naked for me...":
        
            player "Undress and pose naked for me..."
            show hancock c1 annoyed with dissolve
            hancock  "Once again, ordering me around, [player.n]... You have such bad manners..."
            hancock "I doubt you'll ever change. I'll pretend nothing happened here!!!"
            jump hancock_refuse

    window hide
    show hancock c1_naked with dissolve
    pause 1
    show hancock neutral with Dissolve(0.2)
    window auto
    
    $ hancock_lust += 2
    narrador "[hancock.n] lust +2"

    show hancock c1 with dissolve

    jump hancock_goodbye