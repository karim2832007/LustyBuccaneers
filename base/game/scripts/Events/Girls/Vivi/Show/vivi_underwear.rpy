# Version event: 2
# Version game: 0.23

default vivi_underwear = 0

label event_vivi_underwear:
    if vivi_underwear == 0:
        player "[vivi.n] lately I've noticed you don't feel ashamed anymore, and we're getting along better and better..."
        player "But I want you to free yourself even more, here you no longer have responsibilities, you have me to take care of you..."
        show vivi c1 shame with dissolve
        vivi "I love that you cares about me and wants to take care of me."           
        vivi "Always saying such flattering things about me [player.n]..."
        player "It's simply the truth... But I still want more... You can't deny the world such beauty."
        player "Why don't you take off your clothes and show me your underwear..."

        $ vivi_underwear += 1
    else:
        player "Every day you're more attractive and sexy, [vivi.n]..."
        player "You know you shouldn't hide so much beauty from the world..."
        player "Why don't you undress and show me your underwear again?..."


    menu:
        "You can trust me... I want you to show me your true self too...":
            call vivi_check pass (check_love = 8, check_lust = 8) from _vivi_underwear_check
            player "You can trust me, I want you to show me your true self too..."
            vivi "I know exactly what you're implying, [player.n]... There's no doubt..."
            show vivi c1 neutral with dissolve
            vivi "Thanks to you [player.n], I hope I can completely free myself..."
            vivi "So, what do you think, do you like how it looks?!?"

        "Undress and show me the underwear you're wearing...":
            player "Undress and show me the underwear you're wearing..."
            show vivi c1 annoyed with dissolve
            vivi "Ordering me again [player.n]... You have such bad manners..."
            vivi "I don't think I'm in the mood to show you my true self!!"
            jump vivi_refuse

    window hide
    show vivi c1_underwear with dissolve
    pause 1
    show vivi neutral with Dissolve(0.2)
    window auto
    
    $ vivi_lust += 2
    narrador "[vivi.n] lust +2"

    show vivi c1 with dissolve

    jump vivi_goodbye