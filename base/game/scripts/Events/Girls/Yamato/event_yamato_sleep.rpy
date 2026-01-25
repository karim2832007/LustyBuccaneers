# Version event: 4
# Version game: 0.8

label event_yamato_sleep:
    show screen screen_basic_black with Dissolve(0.6)

    $ ui_interface = False
    show events yamato yamato_sleep

    player "(Hopefully [yamato.n] isn't still awake... If she is and sees me coming in, she'll probably give me a beating...)"

    player "(I hope I'm lucky... A quick glance won't hurt anyone...)"

    window hide
    hide screen screen_basic_black with Dissolve(0.3)

    pause 1.0
    window auto

    player "(Woooow... She's so sexy while she sleeps... And on top of that she does it completely naked...)"
    player "(Hmm, I can think of many things to do... Let's see...)"



    menu menu_yamato_sleep:
        "Look at her":
            window hide
            pause 0.5
            pause
            window auto

        "Look closer at her tits":
            player "(They're so perfect... It's clear this girl isn't just pure training, she has great natural beauty...)"
            player "(I can't help wanting to see those tits up close...)"


            show r_yamato_tits_01:
                pos (900, 200)

            player "(Damn, she's so sexy...)"
            player "(They look so soft, I'd love to be able to squeeze them...)"
            player "(But it's not the best time, I have to be careful not to wake her up.)"   
            player "(It's better not to take any more risks, I better go!)"


            hide r_yamato_tits_01 with Dissolve(0.5)

        "Look closer at her pussy":
            
            player "(Let's see what we have here…)"

            show r_yamato_pussy_01 with Dissolve(0.5):
                pos (900, 200)
            pause 1.0
            player "(Niceee pussy...)"
            player "(It looks even more amazing up close…)"
            player "( So fragile and delicate... It doesn't fit her personality …)"
            player "( I would like to continue contemplating her, but I must go or I won't be able to contain myself much longer. )"


            hide r_yamato_pussy_01 with Dissolve(0.5)

        "Jerk off":
            player "(Niceee body!!)"
            player "(She trains so much... No wonder she has such a figure...)"
            player "(I don't think I can last much longer...)"
            narrador "Fap fap fap fap..."
            player "(Ohhh...Take it bitch!!!)"

            window hide
            play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
            with flash
            show events yamato yamato_sleep_cum with Dissolve(0.3)
            pause 0.2
            with flash
            pause 1.5
            window auto

            player "(Wow, I've cum a lot...)"
            yamato "What a strange feeling... What is this smell!?!"
            player "(Damn, she's about to wake up... She's only half asleep! I better get out of here now!)"

            $ ui_interface = True
            jump sleep_night

        "Leave":
            $ ui_interface = True
            jump sleep_night

    jump menu_yamato_sleep
