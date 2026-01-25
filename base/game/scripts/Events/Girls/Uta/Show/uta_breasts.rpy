# Version event: 3
# Version game: 0.28

default uta_breasts = 0

label event_uta_breasts:
    if uta_breasts == 0:
        player "[uta.n] with our recent encounters, your beautiful and sexy figure keeps lingering in my mind..."
        player "It may seem strange, but I can't stop thinking about continuing our previous games..."
        show uta c1 shame with dissolve  
        uta "I wonder what you're going to ask of me [player.n]?..."
        player "You're so seductive... I love your beautiful figure, maybe you could show me your breast?"
        uta "!!!"
        uta "Your request totally caught me by surprise..."
        uta "Always so interested in my body!... Do I attract you that much, Captain?"
        $ uta_breasts += 1
    else:
        player "You're so seductive... You know I love your beautiful figure, and since the last time, I can't stop thinking about your body..."
        player "Maybe you could show me your breasts again?"
        show uta c1 shame with dissolve  
        uta "You're so flattering, [player.n]... I love how direct and interested you are..."
        uta "Maybe if you ask nicely..."


    menu:
        "Your beauty is unmatched...":
            call uta_check pass (check_love = 10, check_lust = 10) from _uta_breasts_check
            player "Your beauty is unmatched... Let's get to know each other more, [uta.n]. We're in a safe space, it's something that will stay between us..."
            player "With me, you don't need to pretend anymore..."
            show uta c1 neutral with dissolve 
            uta "With you, I'm not ashamed anymore, [player.n]... I know I can trust you, and I love that it is that way!"
            uta "So, what do you think, do you like what you see?!?... You can come closer if you want..."


        "Undress and show me your breasts...":
                player "Undress and show me your breasts..."
                show uta c1 annoyed with dissolve
                uta "Once again, ordering me around, [player.n]... You have such bad manners..." 
                uta "I doubt you'll ever change. I'll pretend nothing happened here!!!"
                jump uta_refuse

    window hide
    show uta c1_breasts with dissolve
    pause 1
    show uta neutral with Dissolve(0.2)
    window auto
    
    $ uta_lust += 3
    narrador "[uta.n] lust +3"

    show uta c1 with dissolve

    jump uta_goodbye