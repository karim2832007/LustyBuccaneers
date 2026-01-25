# Version event: 3
# Version game: 0.21

label event_hancock_sleep:
    show screen screen_basic_black with Dissolve(0.6)

    $ ui_interface = False
    show events hancock sleep hancock_sleep

    player "(It's already quite late… I hope Hancock is sleeping, I don't want to offend her...)"
    player "(I think she's sleeping... A quick glance won't hurt anyone...)"

    window hide
    hide screen screen_basic_black with Dissolve(0.3)

    pause 1.0
    window auto

    player "(Wow!! How bold she is, she's sleeping completely naked...)"
    player "(I never thought a princess could sleep naked so carelessly on a pirate ship.)"
    player "(I suppose that in her life on Amazon Lily, this was something normal...)" 
    player "(She has an incredible body!!! She's like an angel...)"
    player "(It's unbelievable that this girl is interested in me...)"   

    menu menu_hancock_sleep:
        "Look at her":
            player "(She's truly an angel... I could stay here all night watching her...)"
            player "(She's not a princess for nothing!)"
            player "(So many things come to mind...)"

            window hide
            pause 0.5
            pause
            window auto

        "Look closer at her tits":

            player "(A little peek won't hurt.)"
        
            show cut_s_hancock_tits with Dissolve(0.3):
                pos (900, 200)
            pause 1.0

            player "(They're even better than I imagined!!...)"
            player "(She has huge breasts!! She must be among the biggest in the crew)"
            player "(I guess, after all, every princess must be at this level...)"
            player "(How lucky I am...I should enjoy them better when I have the chance...)"
            player "(I can think of so many things to do with tits like these!)"

            hide cut_s_hancock_tits with Dissolve(0.5)

        "Look closer at her pussy":

            player "(Let's see what we have down here...)"

            show cut_s_hancock_pussy with Dissolve(0.3):
                pos (900, 200)
            pause 1.0

            player "(Niceee pussy...)"
            player "(Having the snake princess so close, naked on my ship, must be the dream of many at sea...)"
            player "(So this is a royal pussy...)"
            player "(I can't resist much longer...)"
            player "(It must be like being in heaven in there!!)"

            hide cut_s_hancock_pussy with Dissolve(0.5)

        "Look closer at her feet":
            player "(Let's see what we have here...)"

            show cut_s_hancock_feet with Dissolve(0.3):
                pos (900, 200)
            pause 1.0

            player "(Niceee!)"
            player "(So these are the feet of royalty... They're perfect!! So delicate... They're really sexy as well.)"
            player "(I would love to suck them all, while I play with her)"
            player "(Will she like me to play with them, or will she be one of the shy ones?)"

            hide cut_s_hancock_feet with Dissolve(0.5)

        "Jerk off":

            player "(I can't resist anymore!!)"

            #zipper sound
                     
            player "(She is so sexy!!)"
            player "(I would do so many things if I had her in my hands...)"
            player "(I'm sure we would have such a good time... It's just a matter of time...)"
            player "(I'm going to enjoy your body soo sooo much when you're mine [hancock.n]!)"             
            player "(I don't think I can last much longer...)"            
            narrador "Fap fap fap fap..."
            player "(Ohhh...Take it snake princess!!!)"

            menu:
                "cum on tits":
                    window hide
                    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
                    show cut_s_hancock_tits_cum with flash:
                        pos (900, 200)

                "cum on pussy":
                    window hide
                    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
                    show cut_s_hancock_pussy_cum with flash:
                        pos (900, 200)

                "cum on feet":
                    window hide
                    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
                    show cut_s_hancock_feet_cum with flash:
                        pos (900, 200)

            pause 0.2
            with flash
            pause 1.5
            window auto

            player "I better get out of here before he wakes up and sees me..."
            player "I came too much, she deserves it for being so sexy!"

            $ ui_interface = True
            jump sleep_night

        "Leave":
            $ ui_interface = True
            jump sleep_night

    jump menu_hancock_sleep
