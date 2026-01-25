# Version event: 2
# Version game: 0.23

default vivi_naked = 0

label event_vivi_naked:
    if vivi_naked == 0:
        player "[vivi.n] since I saw you, I can't stop thinking about your sexy and provocative figure..."
        player "How about you get naked for me and show me who you really are?"
        player "You are so beautiful, I can't wait to get to know you more and more..."
        show vivi c1 shame with dissolve  
        vivi "You always gave me so much confidence and endlessly praised me..."
        vivi "But I don't know... It might be a little fast for me."
        player "I have no double intentions... I just want our relationship to become more and more intimate."
        player "You know you can trust me, right?... I think I've given you enough trust, what do you say?"
        $ vivi_naked += 1
    else:
        player "[vivi.n] what do you think about opening up to me again and showing me how you really are..."
        vivi "You always gave me so much confidence and endlessly praised me..."


    menu:
        "I only wish to admire your beauty...":
            call vivi_check pass (check_love = 15, check_lust = 15) from _vivi_naked_check

            player "I only wish to admire your beauty... Show me who you really are!"
            show vivi c1 neutral with dissolve 
            vivi "[player.n] I always wanted to do this, to be completely free in front of you..."
            vivi "What do you think? Do you like what you see?!... You're truly privileged to see this..."
            vivi "I don't do this for just anyone!..."
            show vivi c1 shame with dissolve
            vivi "But you are special to me..." 

        "Undress and pose naked for me...":
        
            player "Undress and pose naked for me..."
            show vivi c1 annoyed with dissolve
            vivi  "Once again, ordering me around, [player.n]... You have such bad manners..."
            vivi "I doubt you'll ever change. I'll pretend nothing happened here!!!"
            jump vivi_refuse


    window hide
    show vivi c1_naked with dissolve
    pause 1
    show vivi neutral with Dissolve(0.2)
    window auto
    
    $ vivi_lust += 3
    narrador "[vivi.n] lust +3"

    show vivi c1 with dissolve

    jump vivi_goodbye