# Version event: 8
# Version game: 0.7

# vatiables
default yamato_tongue = 0
default yamato_bra = 0
default yamato_underwear = 0
default yamato_breasts = 0
default yamato_naked = 0

label event_yamato_lewd:
    menu:
        "Flirt":
            show yamato c1 shame with dissolve
            narrador "You spend several minutes making sexually suggestive comments..."
            $ yamato_lust += 1
            narrador "[yamato.n] lust +1" 

        "Lusty Request":
            jump event_yamato_shows
            
        "Services":
            jump event_yamato_services

        "Sex":
            jump event_yamato_sex

        "Back":
            jump event_yamato_call_menu

    jump event_yamato_lewd_end

label event_yamato_shows:
    menu:
        "Show tongue":
            if yamato_tongue == 0:
                player "How are you, [yamato.n]? I often see you training, and I got curious..."
                player "It might sound strange, but could you show me your tongue?"
                show yamato c1 shame with dissolve
                yamato "Captain!! I don't understand what one thing has to do with the other..."
                yamato "Why do you want to see my tongue? It's quite strange."
                $ yamato_tongue += 1
            else:
                player "How are you, [yamato.n]? I know it's strange, but could you show me your tongue again?"
                yamato "Captain! Again with this..."
                yamato "Why do you want to see my tongue? It's quite strange."


            menu:
                "It's something that motivates me in my training":
                    call lewd_yamato_check pass (check_love = 1, check_lust = 1) from _lewd_yamato_check_tongue

                    player "Strangely, it's something that motivates me in my training, it will help me a lot"
                    yamato "I didn't think those things could motivate you... I suppose it won't hurt if I show you."

                "It's just a fantasy of mine":
                    player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                    jump lewd_yamato_refuse


            window hide
            show yamato c1 tongue with dissolve

        "Show Bra":
            if yamato_bra == 0:
                player "How are you, [yamato.n]? ... You have such a sexy and well-trained body..." 
                player "I was wondering what kind of bra you wear? Maybe you could show me..."
                show yamato c1 shame with dissolve 
                yamato "This request is a bit strange... Isn't your question too direct...?"
                $ yamato_bra += 1
            else:
                player "How are you, [yamato.n]? ... Could you show me your bra again?"
                yamato "Captain!! What's with this request? Once again, you're being very direct with your requests..."


            menu:
                "It's simply to admire your shoulders and torso.":
                    call lewd_yamato_check pass (check_love = 3, check_lust = 3) from _lewd_yamato_check_bra

                    player "The bra thing was just an excuse. I don't know if you wear a sports bra or just a regular one when you train.."               
                    player "It's simply to admire your hard-trained shoulders, you can trust me"
                    yamato "I really trust you... If it's just out of curiosity, I suppose there's no harm in showing you."

                "It's just a fantasy of mine":
                    player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                    jump lewd_yamato_refuse


            window hide
            show yamato c1_bra with dissolve

        "Show Underwear":
            if yamato_underwear == 0:
                player "How are you, [yamato.n]? ... To be honest, I'm fascinated by your physique, I always enjoy watching you train..." 
                player "I was wondering what kind of underwear you have? Maybe you could show me..."
                show yamato c1 shame with dissolve 
                yamato "Captain!! Again with these very direct requests, I'm a bit embarrassed, to be honest..."
                $ yamato_underwear += 1
            else:
                player "How are you, [yamato.n]? ... I was wondering what kind of underwear you have? Maybe you could show me again..."
                yamato "Captain!! Again with these very direct requests, I'm a bit embarrassed, to be honest..."


            menu:
                "I simply want to know how to train your muscles.":
                    call lewd_yamato_check pass (check_love = 5, check_lust = 5) from _lewd_yamato_check_underwear

                    player "It's simply to admire your hard-trained muscles, I want to learn one or two things about how you tone certain areas..." 
                    player "You can trust me [yamato.n]"               
                    yamato "I really trust you... If it's just out of curiosity, and to learn one or two things, I suppose there's no harm in showing you."

                "It's just a fantasy of mine":
                    player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                    jump lewd_yamato_refuse


            window hide
            show yamato c1_underwear with dissolve

        "Show Breasts":
            if yamato_breasts == 0:
                player "How are you [yamato.n]?... I spend hours watching you train every day, you're so sexy when you do it..." 
                player "What I like the most is your breasts... Could you maybe show them to me?..."
                show yamato c1 shame with dissolve             
                yamato "Captain!! You don't seem to tire of insisting with these questions... You're quite direct..." 
                yamato "I didn't think you'd be so interested in seeing me like that. I'm a bit embarrassed by what you're asking, to be honest..."
                $ yamato_breasts += 1
            else:
                player "How are you, [yamato.n]? ... I was wondering if you could show me again your breasts??..."
                yamato "Captain!! Again with these very direct requests, I didn't think you'd be so interested in seeing me like that." 
                yamato "I'm a bit embarrassed by what you're asking, to be honest..."


            menu:
                "You have nothing to be ashamed of...":
                    call lewd_yamato_check pass (check_love = 10, check_lust = 10) from _lewd_yamato_check_breasts

                    player "You have an exceptional physique [yamato.n], you have nothing to be ashamed of..."                   
                    yamato "You continue to flatter me, Captain... I didn't think you were so interested in my physique." 
                    yamato "Would you really like to see them that much? I don't think there would be a problem... Look, what do you think?"


                "It's just a fantasy of mine":
                    player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                    jump lewd_yamato_refuse


            window hide
            show yamato c1_breasts with dissolve

        "Show Naked":
            if yamato_naked == 0:
                player "How are you, [yamato.n]? ... I spend hours watching you train every day, you're so sexy when you do it..." 
                player "I feel like it's very hot today... How about we have a training sesión, but naked...?"
                show yamato c1 shame with dissolve
                yamato "Captain!! You're not beating around the bush... I won't deny that I like your attitude but..."
                $ yamato_naked += 1
            else:
                player "Hey [yamato.n], how are you? Your sweaty and toned body after so much training is something I can't forget..."
                player "You're sooo sexy, could you get naked for me one more time?"
                yamato "Captain!! Again with these very direct requests, I didn't think you'd be so interested in seeing me like that." 
                yamato "I'm a bit embarrassed by what you're asking, to be honest..."


            menu:
                "It's just a training session":

                    call lewd_yamato_check pass (check_love = 15, check_lust = 16) from _lewd_yamato_check_naked

                    player "With a well-trained body like yours, you have nothing to be ashamed of..."    
                    player "You're sooo sexy [yamato.n]. It's just a training session, what do you think?"
                    yamato "You continue to flatter me, Captain... We can postpone the training for another occasion. I hope you like what you see..."


                "It's just a fantasy of mine":
                    call lewd_yamato_check pass (check_love = 15, check_lust = 15) from _lewd_yamato_check_naked_r2            
                    
                    
                    player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                    player "You're sooo sexy [yamato.n]. It's just a training session, what do you think?"
                    yamato "You continue to flatter me, Captain... We can postpone the training for another occasion. I hope you like what you see..."


            window hide
            show yamato c1_naked with dissolve

        "Back":
            jump event_yamato_lewd

    pause 1
    window auto
    show yamato neutral with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("Now if you'll excuse me, I'll continue with my training..."),
        _("Now, if you'll excuse me, I'll get back to my training. I'll be here whenever you need me!"),
        _("Until next time, Captain! I'll continue with my training!"),
    ])

    yamato "[talk_random]"

    $ yamato_lust += 1
    narrador "[yamato.n] lust +1"
    jump event_yamato_lewd_end


label lewd_yamato_check(check_love = 0, check_lust = 0):
    if yamato_lust < check_lust or yamato_love < check_love:
        narrador "Requires [yamato.n] lust greater than [check_lust] and love greater than [check_love]"
        jump lewd_yamato_refuse
    return

label lewd_yamato_refuse:
    show yamato anger with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("I can't believe you're telling me this.... I don't know why you think we have that much trust."),
        _("I hope I heard you wrong, Captain... I don't think you want to see me angry..."),
        _("I'm warning you... You don't want to make me angry, Captain..."),
    ])

    yamato "[talk_random]"

    yamato "I'd better continue with my training... I'll pretend like nothing happened here..."

    window hide
    hide yamato with moveoutright

    player "(Perhaps I should have waited a bit before moving forward with this...)"

    $ yamato_love -= 1
    $ yamato_lust -= 1
    narrador "[yamato.n] Lust -1 and Love -1"

    $ game.clock.next()
    jump expression game.location


label event_yamato_lewd_end:
    window hide
    show yamato c1 with dissolve
    hide yamato with moveoutright
    pause 0.5

    $ game.clock.next()
    jump expression game.location