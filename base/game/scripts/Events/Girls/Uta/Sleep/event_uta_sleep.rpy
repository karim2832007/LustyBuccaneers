# Version event: 2
# Version game: 0.19

label event_uta_sleep:
    show screen screen_basic_black with Dissolve(0.6)

    $ ui_interface = False
    show events uta sleep uta_sleep

    player "(Hopefully [uta.n] isn't still awake... Offending the princess would be the last thing a good knight would do... Hehehe!"
    player "(I think she's sleeping... A quick glance won't hurt anyone...)"

    window hide
    hide screen screen_basic_black with Dissolve(0.3)

    pause 1.0
    window auto

    player "(Wow, she's wonderful!... She's so cute while she sleeps, and incredibly sexy... And on top of that she does it completely naked...)"
    player "(I never thought a princess could sleep naked so carelessly on a pirate ship.)"

    menu menu_uta_sleep:
        "Look at her":
            player "(She's truly an angel... I could stay here all night watching her...)"
            player "(She seems to be dreaming something funny)"
            player "(So many things come to mind...)"

            window hide
            pause 0.5
            pause
            window auto

        "Look closer at her tits":

            player "(A little peek won't hurt.)"
        
            show cut_s_uta_tits with Dissolve(0.3):
                pos (900, 150)
            pause 1.0

            player "(They're even better than I imagined!! She had everything so well hidden...)"
            player "(I guess, after all, every princess must be at this level...)"
            player "(How lucky I am...)"
            player "(I can think of so many things to do with tits like these!)"

            hide cut_s_uta_tits with Dissolve(0.5)

        "Look closer at her pussy":

            player "(Let's see what we have down here...)"

            show cut_s_uta_pussy with Dissolve(0.3):
                pos (900, 150)
            pause 1.0

            player "(Niceee pussy...)"
            player "(So this is royal pussy...)"
            player "(I can't resist much longer...)"
            player "(It must be like being in heaven in there!!)"

            hide cut_s_uta_pussy with Dissolve(0.5)

        "Look closer at her feet":
            player "(Let's see what we have here...)"

            show cut_s_uta_feet with Dissolve(0.3):
                pos (900, 150)
            pause 1.0

            player "(Niceee!)"
            player "(So these are the feet of royalty... They're perfect!! So delicate... They're really sexy as well.)"
            player "(I would love to suck them all, while I play with her)"
            player "(Will she like me to play with them, or will she be one of the shy ones?)"

            hide cut_s_uta_feet with Dissolve(0.5)

        "Jerk off":

            player "(I can't resist anymore!!)"

            #zipper sound
                     
            player "(Niceee body!!)"
            player "(I would do so many things if I had her in my hands...)"
            player "(I'm sure we would have such a good time.)"
            player "(I'm going to enjoy your body soo sooo much when you're mine [uta.n]!)"             
            player "(I don't think I can last much longer...)"            
            narrador "Fap fap fap fap..."
            player "(Ohhh...Take it bitch!!!)"

            menu:
                "cum on tits":
                    window hide
                    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
                    show cut_s_uta_tits_cum with flash:
                        pos (900, 150)

                "cum on pussy":
                    window hide
                    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
                    show cut_s_uta_pussy_cum with flash:
                        pos (900, 150)

                "cum on feet":
                    window hide
                    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
                    show cut_s_uta_feet_cum with flash:
                        pos (900, 150)

            pause 0.2
            with flash
            pause 1.5
            window auto

            player "I hope she think it's one of her expensive creams that she probably use..."
            player "I came too much, I better go before he wakes up!"

            $ ui_interface = True
            jump sleep_night

        "Leave":
            $ ui_interface = True
            jump sleep_night

    jump menu_uta_sleep
