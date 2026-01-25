# Version event: 9
# Version game: 0.32

# vatiables
default robin_tongue = 0
default robin_bra = 0
default robin_underwear = 0
default robin_breasts = 0
default robin_naked = 0

label event_robin_lewd:
    menu:
        "Flirt":
            show robin c1 shame with dissolve
            narrador "You spend several minutes making sexually suggestive comments..."
            $ robin_lust += 1
            narrador "[robin.n] Lust +1"

        "Lusty Request":
            jump event_robin_shows

        "Services":
            jump event_robin_services

        "Sex":
            jump event_robin_sex

        "Back":
            jump event_robin_call_menu

    jump event_robin_lewd_end

label event_robin_shows:
    menu:
        "Show tongue":
            if robin_tongue == 0:
                player "How are you, [robin.n]? I always see you reading or researching, and I got curious..." 
                player "It might sound strange, but could you show me your tongue?"
                show robin c1 shame with dissolve
                robin "Captain!! I don't understand what one thing has to do with the other..."
                robin "Why do you want to see my tongue? It's quite strange"
                $ robin_tongue += 1
            else:
                player "How are you, [robin.n]? I know it might sound strange, but could you show me your tongue again?"
                robin "Captain!! you know it's quite strange what you're asking, are you continuing with your research?"


            menu:
                "It's simply for scientific purposes":
                    call lewd_robin_check pass (check_love = 1, check_lust = 1) from _lewd_robin_check_tongle

                    player "It would greatly assist me in my research... It's simply for scientific purposes"
                    robin "I didn't think you had those interests... If that's the purpose, I don't see the problem..."

                "It's just a fantasy of mine":
                    player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                    jump lewd_robin_refuse

            window hide
            show robin c1 tongue with dissolve

        "Show Bra":
            if robin_bra == 0:
                player "How are you, [robin.n]? ... It might sound strange, but could you show me your bra?"
                show robin c1 shame with dissolve
                robin "Captain!! what's the reason for this request, it's really strange..."
                $ robin_bra += 1
            else:
                player "How are you, [robin.n]? ... It might sound strange, but could you show me your bra again?"
                robin "Captain!! with this request again, it's really strange..."


            menu:
                "It's purely for scientific purposes":
                    call lewd_robin_check pass (check_love = 3, check_lust = 3) from _lewd_robin_check_bra

                    robin "It's purely for scientific purposes, You can trust me, you know there's no other motive behind it."
                    robin "I really trust you... If it's for that purpose, I suppose I don't see the problem..."

                "It's just a fantasy of mine":
                    player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                    jump lewd_robin_refuse

            window hide
            show robin c1_bra with dissolve

        "Show Underwear":
            if robin_underwear == 0:
                player "You're beautiful [robin.n]!! It might sound strange, but I'd like to capture an image of you for my next painting..." 
                player "Could you show me your underwear?"
                player "That way I'll have enough to start my work..."
                show robin c1 shame with dissolve           
                robin "I didn't know you painted, captain!! This isn't a joke of yours to see me with less clothing, is it?..."
                $ robin_underwear += 1
            else:
                player "You're beautiful, [robin.n]!!... Could you show me your underwear again?"
                player "That way I'll have enough to start my work..."
                robin "Are you still joking about painting, captain?!! This isn't a prank to see me with less clothing, is it?..."


            menu:
                "It's simply for artistic purposes":
                    call lewd_robin_check pass (check_love = 5, check_lust = 5) from _lewd_robin_check_underwear

                    robin "You can trust me, you know there's no other motive behind it... It's simply for artistic purposes"
                    robin "I really trust you... If it's for that purpose, I suppose I don't see the problem..."

                "It's just a fantasy of mine":
                        player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                        jump lewd_robin_refuse

            window hide
            show robin c1_underwear with dissolve

        "Show Breasts":
            if robin_breasts == 0:
                player "[robin.n], I was just looking for you, I need your help... I'd like you to show me your breasts as I need to take notes on an important topic!"
                show robin c1 shame with dissolve  
                robin "I imagine it must be for scientific purposes, isn't it? You're always so interested in anatomy..."
                $ robin_breasts += 1
            else:
                player "[robin.n], I was just looking for you, I need your help again... I'd like you to show me your breasts as I need to take notes on an important topic!"
                robin "I imagine it must be for scientific purposes, isn't it? You're always so interested in anatomy..."


            menu:
                "Clearly, it's for a scientific topic":
                    call lewd_robin_check pass (check_love = 10, check_lust = 10) from _lewd_robin_check_breasts

                    robin "After so many sessions, you know about my interest in various sciences. Clearly, it's for a scientific topic"
                    robin "After all this time, I know your interests, Captain... If it's for that purpose, I suppose I don't see the problem..."


                "It's just a fantasy of mine":
                        player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                        jump lewd_robin_refuse

            window hide
            show robin c1_bra with dissolve
            pause 0.2
            show robin c1_breasts with dissolve
                
        "Show Naked":
            if robin_naked == 0:
                player "[robin.n], your beauty is unparalleled and you know it..." 
                player "You could be a great inspiration for me if you pose naked for a moment! You know I have work to progress!"
                show robin c1 shame with dissolve  
                robin "After so many requests, I'm well aware of what your true job is..."
                $ robin_naked += 1
            else:
                player "[robin.n], your beauty is unparalleled and you know it... You could be a great inspiration for me if you pose naked for me again! You know I have work to progress!"
                robin "After so many requests, I'm well aware of what your true job is..."


            menu:
                "Clearly, it's not for a scientific topic...":
                    call lewd_robin_check pass (check_love = 15, check_lust = 15) from _lewd_robin_check_naked

                    player "It's just so sexy that you're so intelligent... Clearly, it's not for a scientific topic..."
                    robin "Of course, I always knew, but I enjoyed playing along with your game, captain..."
                    robin "And what do you think? Do you like what you see?..."

                "It's a fantasy of mine":
                    call lewd_robin_check pass (check_love = 15, check_lust = 15) from _lewd_robin_check_naked_r2
                
                    player "I've always wished you'd do this for me... It's just a fantasy of mine, to be honest."
                    robin "Of course, I always knew, but I enjoyed playing along with your game, captain..."
                    robin "And what do you think? Do you like what you see?..."

            window hide
            show robin c1_naked with dissolve
        
        "Back":
            jump event_robin_lewd

    pause 1
    window auto
    show robin neutral with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("Now if you'll excuse me, i'll continue with my duties..."),
        _("Now, if you'll excuse me, I'll get back to my research. I'll be here whenever you need me!"),
        _("Until next time, Captain! I'll continue with my research!"),
    ])

    robin "[talk_random]"
    
    $ robin_lust += 1
    narrador "[robin.n] lust +1"

    jump event_robin_lewd_end

label lewd_robin_check(check_love = 0, check_lust = 0):
    if robin_lust < check_lust or robin_love < check_love:
        narrador "Requires [robin.n] lust greater than [check_lust] and love greater than [check_love]"
        jump lewd_robin_refuse

    return

label lewd_robin_refuse:
    show robin anger with Dissolve(0.2)
    
    $ talk_random = renpy.random.choice([
        _("I can't believe you're telling me this.... I don't know why you think we have that much trust"),
        _("I didn't think you'd be so brazen with me, Captain..."),
        _("You have a lot of nerve asking me this... Your way of thinking is quite childish..."),
    ])

    robin "[talk_random]"
     
    robin "I'd better continue with my research... I'll pretend like nothing happened here..."

    window hide
    hide robin with moveoutright

    player "(Perhaps I should have waited a bit before moving forward with this...)"

    $ robin_love -= 1
    $ robin_lust -= 1

    narrador "[robin.n] Love -1 and Lust -1"

    $ game.clock.next()
    jump expression game.location


label event_robin_lewd_end:
    window hide
    show robin c1 with dissolve
    hide robin with moveoutright
    pause 0.5

    $ game.clock.next()
    jump expression game.location