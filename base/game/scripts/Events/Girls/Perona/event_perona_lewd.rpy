# Version event: 10
# Version game: 0.39

default perona_tongue = 0
default perona_bra = 0
default perona_underwear = 0
default perona_breasts = 0
default perona_naked = 0

label event_perona_lewd:
    menu:
        "Flirt":
            show perona c1 shame with dissolve
            narrador "You spend several minutes making sexually suggestive comments..."
            $ perona_lust += 1
            narrador "[perona.n] Lust +1"

        "Lusty Request":
            jump event_perona_shows

        "Services":
            jump event_perona_services

        "Sex":
            jump event_perona_sex

        "Back":
            jump event_perona_call_menu

    jump event_perona_lewd_end

label event_perona_shows:
    menu:
        "Show tongue":
            if perona_tongue == 0:
                player "How are you doing, [perona.n]? ... You know, when I was a kid, before becoming a pirate, I was a pretty cheerful and nostalgic boy..."
                player "I had a friend I spent all my time with—we'd have fun, pull pranks, and just enjoy life to the fullest..."
                perona "That sounds kinda cute, [player.n]... what happened to your friend?"
                player "She died at the hands of a pirate... or maybe a marine. I'm not even sure anymore..."
                perona "Pff... that's just another everyday story out at sea. Nothing special."
                player "Yeah, I know... but what I was trying to say is that as kids, we were always sticking our tongues out at each other to annoy one another..."
                player "That girl reminds me a lot of you... maybe you could... stick your tongue out at me, for old times' sake?"

                show perona c1 shame with Dissolve(0.2)
                perona "Eeeeh?! But we're not kids anymore! That sounds super weird and embarrassing, horo horo horo...!"
                player "It would bring back some really good memories for me... just once, it'll be our little secret."
                $ perona_tongue += 1
            else:
                player "How are you, [perona.n]? ... maybe you could... stick your tongue out at me again, for old times' sake?"
                show perona c1 shame with Dissolve(0.2)                
                perona "You're asking for that weird thing again, [player.n]...! Do you really enjoy watching me make a fool of myself that much?"
                player "You look incredibly adorable when you do it... what do you say?"



            menu:
                "It would bring back good memories for me...":
                    call lewd_perona_check pass (check_love = 1, check_lust = 1) from _lewd_perona_check_tongle

                    player "It'd just be once... and it'll stay our silly little secret."
                    perona "Hmph... I'll only do it because the story you told was kinda touching..."
                    perona "But don't get used to it, okay! I feel like a little kid doing this, horo horo..."
                    player "Don't worry, no one else will ever know..."

                "It's an order. You should do it for your captain...":
                    player "You have to do it... I'm your captain—it's an order!"
                    show perona c1 anger with Dissolve(0.2)
                    perona "Hmph! Don't you dare pull that 'captain' nonsense on me for something this stupid!"
                    perona "I'm not one of your brainless zombies, horo horo horo...!"
                    perona "If you think you can order me around for your childish games, you're sorely mistaken!"
                    perona "Try that tone again and you'll see... got it?!"

                    jump lewd_perona_refuse


            $ _window_hide()
            show perona c1 tongue with Dissolve(0.2)
            pause 1.0
            perona "Bleeeeh~!"
            player "Hahaha... thanks, [perona.n]. For a second, you turned back into that mischievous girl I loved remembering."
            pause 0.5
            show perona c1 shame with Dissolve(0.2)
            perona "Sh-shut up already! This is so embarrassing...! Don't stare at my face like that, you pervert...!"

        "Show Bra":
                    if perona_bra == 0:
                        player "Hey, [perona.n], how's everything going? ... Every time I see you, I can't help but admire your style."
                        player "That gothic lolita look... the elegance, the dark charm, the way you carry yourself—it's perfect."
                        show perona c1 shame with Dissolve(0.2)
                        perona "Heh... it flatters me that you notice, [player.n]. I do put a lot of effort into looking cute and spooky at the same time, horo horo..."
                        player "You're definitely succeeding. Everything about you screams refined taste."
                        player "Even the little details... like what kind of bra you wear under all that. Does it match your gothic vibe?"
                        perona "H-HUH?!? Did you just seriously ask about my BRA?!? That's way too forward, you pervert...!"

                        $ perona_bra += 1
                    else:
                        player "How's my favorite ghost princess doing today, [perona.n]? Still rocking that unbeatable style, I see..."
                        player "You've been carrying yourself with even more confidence lately. It's hot."
                        show perona c1 shame with Dissolve(0.2)
                        perona "Hmph... I guess I have you to thank for some of that, [player.n]. Not that I'll admit it out loud too often, horo horo."
                        player "Good. Now, about that little secret of yours... what bra are you wearing today? You know you can trust me with it."

                    menu:
                        "It's just for fashion purposes...":
                            call lewd_perona_check pass (check_love = 3, check_lust = 3) from _lewd_perona_check_bra

                            player "Don't get the wrong idea—I'm only asking because I genuinely love your fashion sense. I promise I won't make it weird."                   
                            perona "You're such a smooth talker... Fine, I do trust you. But I'm still super embarrassed about this!"
                            player "No need to be. You're stunning from head to toe. Own it. Let me see how the whole look comes together."
                            perona "Ugh... you're impossible. But... maybe you're right. I should be prouder of myself."
                            perona "Okay, fine! Take a good look, but don't stare too much, horo horo...!"

                        "It must look incredibly sexy on you...":
                            player "Come on, it must look incredibly sexy on you. Just show me what you're wearing today..."

                            show perona c1 anger with Dissolve(0.2)
                            perona "Excuse me?! You think you can just demand to see my underwear like that?!"
                            perona "I'm not some toy for your amusement, [player.n]! Try ordering me around again and you'll see!"
                            perona "Hmph! Pervert captain..."

                            jump lewd_perona_refuse

                    $ _window_hide()
                    show perona c1_bra with dissolve
                    pause 1.0
                    player "Wow... it suits you perfectly... Pure gothic elegance."
                    show perona c1 shame with Dissolve(0.2)
                    perona "S-Stop analyzing it like that! You're making my face burn...!"
                    perona "But... I'm glad you like it. Just don't tell anyone, okay? This stays between us, horo horo..."


        "Show Underwear":
                    if perona_underwear == 0:
                        player "Hey, [perona.n]... lately I've noticed you're carrying yourself differently. No more hiding, no doubts, no unnecessary shame."
                        player "It suits you. Makes you look even more attractive... dangerously sexy, actually."
                        show perona c1 shame with Dissolve(0.2)           
                        perona "Hmph... you always say the sweetest, most embarrassing things, [player.n]. My face is getting hot again, horo horo..."
                        player "Because it's true. You're beautiful, and the world deserves to see it... or at least I do."
                        player "Why don't you take off that dress and let me see your underwear? Just for me."

                        $ perona_underwear += 1
                    else:
                        player "Every time I look at you, [perona.n], you're more breathtaking than the day before."
                        player "That confidence of yours... it's intoxicating. You really shouldn't hide so much perfection under all those layers."
                        show perona c1 shame with Dissolve(0.2)
                        perona "You're impossible, you know that? Saying stuff like that so casually..."
                        player "Come on, indulge me again. Undress and show me what pretty underwear you're wearing today?"

                    menu:
                        "You can trust me... I just want to admire your beauty...":
                            call lewd_perona_check pass (check_love = 5, check_lust = 5) from _lewd_perona_check_underwear

                            player "I promise it's only to appreciate you—every curve, every detail. Nothing more than that."
                            show perona c1 shame with Dissolve(0.2)
                            perona "I... I do trust you, Captain. More than I'd like to admit sometimes."
                            perona "Fine... but don't stare too hard, okay? You're making me nervous, horo horo..."
                            perona "So...? What do you think? Does it look good on me?"

                        "Undress right now and show me your underwear...":
                            player "Undress right now and show me what underwear you're wearing. Don't make me wait."

                            show perona c1 anger with Dissolve(0.2)
                            perona "Excuse me?! You think you can just bark orders at me like I'm some obedient doll?!"
                            perona "I'm not here for you to command around whenever you feel like it, [player.n]!"
                            perona "Try talking to me like that again and you'll regret it, horo horo...!"
                            perona "Hmph! Perverted captain..."

                            jump lewd_perona_refuse

                    $ _window_hide()
                    show perona c1_underwear with dissolve
                    pause 1.0
                    player "God... you're absolutely stunning. The way it hugs your body, the colors, everything—perfect."
                    perona "S-stop saying things like that so intensely! You're making me all flustered...!"
                    perona "But... I'm happy you like it. Just keep it our secret, okay? No one else gets to see this."

        "Show Breasts":
                    if perona_breasts == 0:
                        player "[perona.n]... I haven't been able to get your figure out of my head for days now."
                        player "You're beautiful, seductive... everything about you drives me crazy."
                        show perona c1 shame with Dissolve(0.2)
                        perona "Y-you're saying such bold things all of a sudden, [player.n]... My heart's racing, horo horo..."
                        player "I can't keep pretending. We've come this far together... I need to see more of you."
                        player "Would you... show me your breasts? Just for me."
                        perona "!!!"
                        perona "Th-that's... incredibly direct! I didn't expect you'd want to see that much of me..."
                        perona "My face is burning... you're making me all nervous, you idiot!"

                        $ perona_breasts += 1
                    else:
                        player "Hey, [perona.n]... I still can't stop thinking about your body since last time."
                        player "You're so perfectly seductive. Every curve, every detail... it's addictive."
                        show perona c1 shame with Dissolve(0.2)
                        perona "Hmph... you really know how to make a girl flustered, Captain. Saying things like that so casually, horo horo..."
                        player "Then indulge me again? Please... let me see your breasts once more."

                    menu:
                        "Your beauty is unparalleled...":
                            call lewd_perona_check pass (check_love = 10, check_lust = 10) from _lewd_perona_check_breasts

                            player "No one compares to you. This is just between us—our little secret. I only want to admire you."
                            show perona c1 shame with Dissolve(0.2)
                            perona "I... I'm not embarrassed in front of you anymore. Not really."
                            perona "You've earned my trust, [player.n]. More than anyone else."
                            perona "So... here. What do you think? Do you like them...? You can come closer if you want, horo..."

                        "Undress right now and show me your breasts...":
                            player "Undress right now and show me your breasts. I want to see them."

                            show perona c1 anger with Dissolve(0.2)
                            perona "What did you just say?! You think you can order me to strip like some common servant?!"
                            perona "I'm a princess, not your personal toy to command whenever you please!"
                            perona "You're lucky I even like you, you insensitive pervert! Hmph!"
                            perona "Ask like that again and you'll never get anything from me, horo horo...!"

                            jump lewd_perona_refuse

                    $ _window_hide()
                    pause 0.2
                    show perona c1_underwear with dissolve
                    pause 0.5
                    show perona c1_breasts with dissolve
                    pause 1.0
                    player "They're... perfect. So beautiful. You take my breath away, [perona.n]."
                    perona "S-stop staring so much! You're making me way too self-conscious...!"
                    perona "But... I'm glad you like them. Just don't tell a soul about this, okay? It's embarrassing enough already..."
                
        "Show Naked":
                    if perona_naked == 0:
                        player "[perona.n]... ever since I first saw you, your figure has been living rent-free in my head."
                        player "The way you move, that provocative elegance... it's driving me insane."
                        show perona c1 shame with Dissolve(0.2)  
                        perona "Y-you're being way too intense again, [player.n]... My heart can't take it when you talk like that, horo horo..."
                        player "You've given me so much trust already. You've let me see parts of you no one else has."
                        player "Now... I want to see all of you. Completely naked. Just for me."
                        perona "All of me...? You mean... everything?"
                        perona "That's... that's a huge step!"

                        $ perona_naked += 1
                    else:
                        player "Hey, [perona.n]... I've been daydreaming about you again. About how perfect you looked last time."
                        player "Would you open up to me once more? Let me see the real you, completely bare?"
                        show perona c1 shame with Dissolve(0.2)
                        perona "You never stop, do you? Always finding new ways to make me blush, Captain... horo horo."
                        perona "But... I can't say no when you look at me like that."

                    menu:
                        "I just want to admire your true beauty...":
                            call lewd_perona_check pass (check_love = 15, check_lust = 15) from _lewd_perona_check_naked

                            player "You're the most beautiful thing I've ever seen. I only want to admire you—every inch, exactly as you are."
                            show perona c1 shame with Dissolve(0.2)
                            perona "You always know exactly what to say to melt me... No one's ever made me feel this wanted."
                            perona "Fine... I'll do it. But only because it's you."
                            perona "So... what do you think? Do I... live up to your fantasies, Captain...? Don't just stare silently like that!"

                        "Get undressed right now and pose naked for me...":
                            player "Get undressed right now and pose naked for me. I want to see everything."
                            show perona c1 anger with Dissolve(0.2)
                            perona "How dare you talk to me like that?! You think you can just demand I strip on command?!"
                            perona "I'm not some mindless doll you get to order around whenever you're in the mood!"
                            perona "You're incredibly lucky I even like you this much, you rude, perverted captain!"
                            perona "Ask like that again and you'll be sleeping alone for a very long time, horo horo...!"

                            jump lewd_perona_refuse

                    $ _window_hide()
                    show perona c1_underwear with dissolve
                    pause 0.5
                    show perona c1_naked with dissolve
                    pause 1.0
                    player "You're... breathtaking. Absolutely perfect. I can't take my eyes off you, [perona.n]."
                    perona "D-don't say it so seriously! You're making me want to cover up again...!"
                    perona "But... thank you. I'm really happy you think so. Just... keep this moment between us forever, okay?"
        
        "Back":
            jump event_perona_lewd

    pause 1
    show perona neutral with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("Now if you'll excuse me, I'm leaving..."),
        _("Now, if you'll excuse me, I'll get back to my woork. I'll be here whenever you need me!"),
        _("Until next time, Captain!"),
    ])

    perona "[talk_random]"

    $ perona_lust += 1
    narrador "[perona.n] lust +1"

    jump event_perona_lewd_end

label lewd_perona_check(check_love = 0, check_lust = 0):
    if perona_lust < check_lust or perona_love < check_love:
        narrador "Requires [perona.n] lust greater than [check_lust] and love greater than [check_love]"
        jump lewd_perona_refuse

    return

label lewd_perona_refuse:
    show perona anger with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("You have a lot of confidence, considering we've known each other for such a short time, Captain..."),
        _("I didn't think you'd be so brazen with me, Captain..."),
        _("Once again, ordering me around... You have such bad manners..."),
    ])

    perona "[talk_random]"
    perona "I doubt you'll ever change. I'll pretend nothing happened here!!!"

    window hide
    hide perona with moveoutright

    player "(Fuck... Perhaps I should have waited a bit before moving forward with this...)"

    $ perona_love -= 1
    $ perona_lust -= 1

    narrador "[perona.n] Love -1 and Lust -1"

    $ game.clock.next()
    jump expression game.location


label event_perona_lewd_end:
    window hide
    pause 0.2
    show perona c1 with dissolve
    hide perona with moveoutright
    pause 0.5

    $ game.clock.next()
    jump expression game.location