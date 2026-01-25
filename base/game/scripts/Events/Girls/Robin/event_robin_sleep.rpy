# Version event: 5
# Version game: 0.8

label event_robin_sleep:
    show screen screen_basic_black with Dissolve(0.6)

    $ ui_interface = False
    show events robin robin_sleep

    player "(Is [robin.n] still awake?)"

    player "(I hope she didn't stay up reading a book or something... or she might take my intrusion the wrong way.)"

    window hide
    hide screen screen_basic_black with Dissolve(0.3)

    pause 1.0
    window auto

    player "(Woooow... She's so sexy while she sleeps... And on top of that she does it completely naked...)"
    player "(Hmm, I can think of many things to do... Let's see...)"


    menu menu_robin_sleep:
        "Look at her":
            window hide
            pause 0.5
            pause
            window auto

        "Look closer at her tits":
            player "(They're so perfect... Not only is she seductive and intellectual, she has great natural beauty...)"
            player "(I can't help but want to see those tits up close, purely for scientific reasons, of course...)"


            show r_robin_tits_01:
                pos (900, 200)

            player "(Damn, she's so sexy...)"
            player "(They look so soft, I'd love to be able to squeeze them...)"
            player "(But it's not the best time, I have to be careful not to wake her up.)"   
            player "(It's better not to take any more risks, I better go!)"


            hide r_robin_tits_01 with Dissolve(0.5)

        "Look closer at her pussy":
            player "(Well... Let's see how it goes down here.…)"


            show r_robin_pussy_01 with Dissolve(0.5):
                pos (900, 200)
            pause 1.0
            player "(Soo sexy...)"
            player "(It looks even more amazing up close...)"
            player "(So incredibly lewd with a beautiful pink color...)"
            player "(I'm sure it must be so warm inside... and slippery...)"
            player "(How I would like to study her anatomy right now... But I must go or I won't be able to contain myself much longer.)"


            hide r_robin_pussy_01 with Dissolve(0.5)

        "Jerk off":
            player "(Soo perfect!!)"
            player "(She's so attractive while she sleeps...)"
            player "(I don't think I can last much longer...)"
            narrador "Fap fap fap fap..."
            player "(Here are your vitamins [robin.n]...)"

            window hide
            play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
            with flash
            show events robin robin_sleep_cum with Dissolve(0.3)
            pause 0.2
            with flash
            pause 1.5
            window auto

            player "(Wow, I've cum a lot...)"
            robin "What a strange feeling... It's so hot!"
            player "(Damn, she's about to wake up... She's only half asleep! I better get out of here now!)"

            $ ui_interface = True
            jump sleep_night

        "Leave":
            $ ui_interface = True
            jump sleep_night

    jump menu_robin_sleep