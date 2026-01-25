# Version event: 2
# Version game: 0.12

default hancock_underwear = 0

label event_hancock_underwear:
    if hancock_underwear == 0:
        player "[hancock.n] lately I've noticed you don't feel ashamed anymore, and we're getting along better and better..."
        player "But I want you to free yourself even more, here you no longer have responsibilities, you have me to take care of you..."
        player "You no longer have to pretend to be tough and cold, you're truly attractive and sexy when you don't..."
        show hancock c1 shame with dissolve           
        hancock "Always saying such flattering things about me [player.n]..."
        hancock "You know it's really hard for me to show that side of myself..."
        player "It's simply the truth... But I still want more... You can't deny the world such beauty."
        player "Why don't you take off your clothes and show me your underwear..."

        $ hancock_underwear += 1
    else:
        player "Every day you're more attractive and sexy, [hancock.n]..."
        player "You know you shouldn't hide so much beauty from the world..."
        player "Why don't you undress and show me your underwear again?..."


    menu:
        "You can trust me... I want you to show me your true self...":
            call hancock_check pass (check_love = 8, check_lust = 8) from _hancock_underwear_check
            player "You can trust me, I want you to show me your true self..."
            hancock "I know exactly what you're implying, [player.n]... There's no doubt..."
            show hancock c1 neutral with dissolve
            hancock "Thanks to you [player.n], I hope I can completely free myself..."
            hancock "So, what do you think, do you like how it looks?!?"

        "Undress and show me the underwear you're wearing...":
            player "Undress and show me the underwear you're wearing..."
            show hancock c1 annoyed with dissolve
            hancock "Ordering me again [player.n]... You have such bad manners..."
            hancock "I don't think I'm in the mood to show you my true self!!"
            jump hancock_refuse

    window hide
    show hancock c1_underwear with dissolve
    pause 1
    show hancock neutral with Dissolve(0.2)
    window auto
    
    $ hancock_lust += 1
    narrador "[hancock.n] lust +1"

    show hancock c1 with dissolve

    jump hancock_goodbye