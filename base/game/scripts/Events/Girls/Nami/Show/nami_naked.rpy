# Version event: 1
# Version game: 0.14

default nami_naked = 0

label event_nami_naked:
    if nami_naked == 0:            
        player "You're so beautiful, [nami.n]!!... Would you honor me with your beauty and undress for me?"
        show nami c1 shame with dissolve  
        nami "I didn't think my body attracted you so much, Captain!... Don't think it's so easy to get what you want..."
        show nami neutral with dissolve
        nami "How about a deal?! For a certain amount of [Berries.n], I wouldn't mind doing it for you:"
        $ nami_naked += 1
    else:
        player "How are you, [nami.n]? I would love to see you naked again, Could you undress for me?"
        nami "Captain!! My body is desired by countless pirates at sea, so don't think this request will come for free:"


    menu:
        "20 [Berries.n]" if berries >= 20:
            call nami_check pass (check_love = 12, check_lust = 12, check_berries = 20) from _nami_check_naked_20
            show nami happy with dissolve

            $ talk_random = renpy.random.choice([
                _("Excellent!! a pleasure doing business with you captain... all yours..."),
                _("It's always a pleasure doing business with you, Captain!!"),
            ])

        "Bargain, 10 [Berries.n]" if berries >= 10:
            call nami_check pass (check_love = 13, check_lust = 13, check_berries = 10) from _nami_check_naked_10
            show nami happy with dissolve

            $ talk_random = renpy.random.choice([
                _("well!! just for you, captain... i hope you enjoy it..."),
                _("You're a good negotiator, Captain. I'll only accept because it's you!"),
            ])

        "No payment":
            call nami_check pass (check_love = 15, check_lust = 15, check_berries = 0) from _nami_check_naked_0
            show nami neutral with dissolve

            $ talk_random = renpy.random.choice([
                _("Consider it a favor just for you, captain! Don't think I'm that easy..."), 
                _("You caught me on a good day, Captain... Don't think I'm an easy girl!"),
            ])

    nami "[talk_random]"

    window hide
    show nami c1_naked with dissolve
    pause 1
    show nami neutral with Dissolve(0.2)
    window auto
    
    $ nami_lust += 2
    narrador "[nami.n] lust +2"

    show nami c1 with dissolve

    jump nami_goodbye