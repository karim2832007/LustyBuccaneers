# Version event: 2
# Version game: 0.28

default uta_underwear = 0

label event_uta_underwear:
    if uta_underwear == 0:
        player "[uta.n] lately I've noticed you don't feel ashamed anymore, and we're getting along better and better..."
        player "But I want you to free yourself even more, here you no longer have responsibilities, you have me to take care of you..."
        player "I want you to stop playing the Idol, be truly free with me, just as you are..."
        player "You're really sexy and attractive when you let go, without restraints..."
        
        show uta c1 shame with dissolve
        
        uta "I love that you cares about me and wants to take care of me."           
        uta "Always saying such flattering things about me [player.n]..."
        uta "You know it's really hard for me to show that side of myself..."
        player "It's simply the truth... But I still want more... You can't deny the world such beauty."
        player "Why don't you take off your clothes and show me your underwear..."

        $ uta_underwear += 1
    else:
        player "Every day you're more attractive and sexy, [uta.n]..."
        player "You know you shouldn't hide so much beauty from the world..."
        player "Why don't you undress and show me your underwear again?..."


    menu:
        "You can trust me... I want you to show me your true self...":
            call uta_check pass (check_love = 8, check_lust = 8) from _uta_underwear_check
            player "You can trust me, I want you to show me your true self..."
            uta "I know exactly what you're implying, [player.n]... There's no doubt..."
            show uta c1 shame with dissolve
            uta "Thanks to you [player.n], I hope I can completely free myself..."
            uta "So, what do you think, do you like how it looks?!?"

        "Undress and show me the underwear you're wearing...":
            player "Undress and show me the underwear you're wearing..."
            show uta c1 annoyed with dissolve
            uta "Ordering me again [player.n]... You have such bad manners..."
            uta "I don't think I'm in the mood to show you my true self!!"
            jump uta_refuse

    window hide
    show uta c1_underwear with dissolve
    pause 1
    show uta neutral with Dissolve(0.2)
    window auto
    
    $ uta_lust += 2
    narrador "[uta.n] lust +2"

    show uta c1 with dissolve

    jump uta_goodbye