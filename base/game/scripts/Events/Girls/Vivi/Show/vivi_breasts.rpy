# Version event: 2
# Version game: 0.23

default vivi_breasts = 0

label event_vivi_breasts:
    if vivi_breasts == 0:
        player "[vivi.n] with our recent encounters, your beautiful and sexy figure keeps lingering in my mind..."
        player "It might seem strange, but I can't continue with our previous games..."
        show vivi c1 shame with dissolve  
        vivi "What do you mean?... I wonder what you're going to ask of me [player.n]?..."
        player "You're so seductive... I love your beautiful figure, maybe you could show me your breast?"
        vivi "!!!"
        vivi " I didn't think you'd be so interested in my body... You're so flattering, [player.n]!"
        $ vivi_breasts += 1
    else:
        player "You're so seductive... You know I love your beautiful figure, and since the last time, I can't stop thinking about your body..."
        player "Maybe you could show me your breasts again?"
        show vivi c1 shame with dissolve  
        vivi "You're so flattering, [player.n]... I love how direct and interested you are..."
        vivi "Maybe if you ask nicely..."


    menu:
        "You are really beautiful, I don't want to hide it anymore!":
            call vivi_check pass (check_love = 10, check_lust = 10) from _vivi_breasts_check
            player "Your beauty is unmatched... Let's get to know each other more, [vivi.n]. We're in a safe space, it's something that will stay between us..."
            player "With me, you don't need to pretend anymore... I don't want to hide it anymore!"
            show vivi c1 neutral with dissolve 
            vivi "With you, I'm not ashamed anymore, [player.n]... I know I can trust you, and I love that it is that way!"
            vivi "So, what do you think, do you like what you see?!?... You can come closer if you want..."


        "Undress and show me your breasts...":
                player "Undress and show me your breasts..."
                show vivi c1 annoyed with dissolve
                vivi "Once again, ordering me around, [player.n]... You have such bad manners..." 
                vivi "I doubt you'll ever change. I'll pretend nothing happened here!!!"
                jump vivi_refuse

    window hide
    show vivi c1_breasts with dissolve
    pause 1
    show vivi neutral with Dissolve(0.2)
    window auto
    
    $ vivi_lust += 3
    narrador "[vivi.n] lust +3"

    show vivi c1 with dissolve

    jump vivi_goodbye