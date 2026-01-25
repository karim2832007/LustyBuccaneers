# Version event: 6
# Version game: 0.19

label event_perona_sleep:
    show screen screen_basic_black with Dissolve(0.6)

    $ ui_interface = False
    show events perona perona_sleep

    player "(Time for another nighttime visit...)"
    player "(This time to the beautiful [perona.n]!!... Supposedly, she's not one of the girls who stays up late at night...)"
    player "(She always says she sleeps most of the day... To take care of her skin or something like that...)"
    player "(I hope she's a heavy sleeper... The worst thing I could do is make her angry...)"


    window hide
    hide screen screen_basic_black with Dissolve(0.3)

    pause 1.0
    window auto

    player "(Woooow... I'm so glad I added her to the crew... She's incredibly sexy!!)"
    player "(She has an amazing body... Combined with her style and character... there must be few girls more attractive and sexy than her in these seas...)"
    player "(So many things I could do with her so helpless...)"

    menu menu_perona_sleep:
        "Look at her":
            window hide
            pause 0.5
            pause
            window auto
            

        "Look closer at her tits":
            player "(They're perfect!!...)" 
            player "(I think they might even be bigger than the rest of the girls, maybe like [yamato.n]'s or [robin.n]'s...)"
            player "(From this distance, I can't say for sure... I should see them up close...)"

            show r_perona_tits_01 with Dissolve(0.3):
                pos (900, 200)
            pause 1.0
            player "(Ugh, what beautiful breats...)"
            player "(I can't resist the urge to squeeze them...)"
            player "(But waking her up now could be the last thing I do, hahaha...)"
            player "([perona.n] just waking up and angry for spying on her while she sleeps is a death sentence...)"
            player "(Better leave for now before I get more tempted and do something stupid...)"

            hide r_perona_tits_01 with Dissolve(0.5)

        "Look closer at her pussy":
            player "(Let's see what the bottom looks like...)"

            show r_perona_pussy_01 with Dissolve(0.3):
                pos (900, 200)
            pause 1.0
            player "(What a beautiful pussy!!...)"
            player "(It looks even more amazing up close...)"
            player "(So delicate... It tottaly fit her personality...)"
            player "(Is she still a virgin?... She is so innocent with some topics... I would love it!...)"
            player "(I could stay all night looking at her, but I must go or I won't be able to contain myself much longer.)"

            hide r_perona_pussy_01 with Dissolve(0.5)

        "Jerk off":
            player "(Omfg... This little girl!!)"
            player "(She's so cute and sexy while she sleeps...)"
            player "(I don't think I can last much longer...)"
            narrador "Fap fap fap fap..."
            player "(Ohhh here comes the milk... )"

            window hide
            play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
            with flash
            show events perona perona_sleep_cum with Dissolve(0.3)
            pause 0.2
            with flash
            pause 1.5
            window auto

            player "(Wow, I've cum a lot...)"
            perona "Mmnmnm how hot it is suddenly... I'm all sticky... It's nice..."
            player "(Damn, she's about to wake up... She's only half asleep! I better get out of here now!)"

            $ ui_interface = True
            jump sleep_night

        "Leave":
            $ ui_interface = True
            jump sleep_night

    jump menu_perona_sleep
