# Version event: 1
# Version game: 0.14

label event_nami_sleep:
    show screen screen_basic_black with Dissolve(0.6)

    $ ui_interface = False
    show events nami nami_sleep

    player "(I wonder if [nami.n] is still awake?)"

    player "(I'll take a look in her room... Hopefully she won't get mad if she sees me coming in like this...)"

    window hide
    hide screen screen_basic_black with Dissolve(0.3)

    pause 1.0
    window auto

    player "(Woooow... She's so sexy while she sleeps... And on top of that she does it completely naked...)"
    player "(Hmm, I can think of many things to do... Let's see...)"


    menu event_nami_sleep_menu:
        "Look at her":
            window hide
            pause 0.5
            pause
            window auto

        "Look closer at her tits":
            player "(They're so perfect... It's clear she constantly takes care of her body, her beauty is unmatched!!)"
            player "(I can't help but want to see those tits up close, I might not get this chance often for free! Hahahah...)"


            show r_nami_tits_01:
                pos (900, 200)

            player "(Damn, she's so sexy...)"
            player "(They look so soft, I'd love to be able to squeeze them...)"
            player "(But it's not the best time, I have to be careful not to wake her up.)"   
            player "(It's better not to take any more risks, I better go!)"


            hide r_nami_tits_01 with Dissolve(0.5)

        "Look closer at her pussy":
            player "(Well... Let's start the show...)"


            show r_nami_pussy_01 with Dissolve(0.5):
                pos (900, 200)
            pause 1.0
            player "(Niceeeee!!)"
            player "(I love redheads... They are so hot...)"
            player "(She has such a sexy pussy, with little orange touches...)"
            player "(If she found out I was watching this show... For free...)"
            player "(She's going to kill me!!... No matter how much it hurts, it would be better to stop for now... )"


            hide r_nami_pussy_01 with Dissolve(0.5)

        "Jerk off":
            player "(Sooo sexy!!)"
            player "(After having her around constantly, you can't blame me for this...)"
            player "(It's her fault for being so provocative...)"
            narrador "Fap fap fap fap..."
            player "(Take it aaaall... )"

            window hide
            play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
            with flash
            show events nami nami_sleep_cum with Dissolve(0.3)
            pause 0.2
            with flash
            pause 1.5
            window auto

            player "(Wow, I've cum a lot...)"
            nami "Mmnmnm so hot... So good..."
            player "(Damn, she's about to wake up... She's only half asleep! I better get out of here now!)"

            $ ui_interface = True
            jump sleep_night

        "Leave":
            $ ui_interface = True
            jump sleep_night

    jump event_nami_sleep_menu
