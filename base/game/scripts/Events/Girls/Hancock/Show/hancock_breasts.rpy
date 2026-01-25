# Version event: 2
# Version game: 0.12

default hancock_breasts = 0

label event_hancock_breasts:
    if hancock_breasts == 0:
        player "[hancock.n] With our recent encounters, your beautiful and sexy figure keeps lingering in my mind..."
        player "It might seem strange, but I can't continue with our previous games..."
        hancock "I wonder what you're going to ask of me [player.n]?..."
        player "You're so seductive… I love your beautiful figure, maybe you could show me your breast?"
        show hancock c1 shame with dissolve  
        hancock "!!!"
        hancock "Your request totally caught me by surprise… I didn't think you'd be so interested in my body..."
        $ hancock_breasts += 1
    else:
        player "You're so seductive... You know I love your beautiful figure, and since the last time, I can't stop thinking about your body..."
        player "Maybe you could show me your breasts again?"
        show hancock c1 shame with dissolve  
        hancock "You're so flattering, [player.n]… I love how direct and interested you are..."
        hancock "Maybe if you ask nicely..."


    menu:
        "Clearly, it's for a scientific topic":
            call hancock_check pass (check_love = 10, check_lust = 10) from _hancock_breasts_check
            player "Your beauty is unmatched… Let's get to know each other more, [hancock.n]. We're in a safe space, it's something that will stay between us..."
            player "With me, you don't need to pretend anymore..."
            show hancock c1 neutral with dissolve 
            hancock "With you, I'm not ashamed anymore, [player.n]... I know I can trust you."
            hancock "So, what do you think, do you like what you see?!?... You can come closer if you want..."


        "Undress and show me your breasts...":
                player "Undress and show me your breasts..."
                show hancock c1 annoyed with dissolve
                hancock "Once again, ordering me around, [player.n]... You have such bad manners..." 
                hancock "I doubt you'll ever change. I'll pretend nothing happened here!!!"
                jump hancock_refuse

    window hide
    show hancock c1_breasts with dissolve
    pause 1
    show hancock neutral with Dissolve(0.2)
    window auto
    
    $ hancock_lust += 2
    narrador "[hancock.n] lust +2"

    show hancock c1 with dissolve

    jump hancock_goodbye