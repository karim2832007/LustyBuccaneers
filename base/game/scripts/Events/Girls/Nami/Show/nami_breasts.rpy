# Version event: 1
# Version game: 0.14

default nami_breasts = 0

label event_nami_breasts:
    if nami_breasts == 0:
        player "How are you, [nami.n]? After spending so many days surrounded by your beauty, I can't resist anymore..." 
        player "It might sound strange, but could you show me your breasts?"
        show nami c1 shame with dissolve              
        nami "Captain!! How bold you are... I didn't think you'd be so direct. You know that with me, we can always come to an agreement."
        show nami neutral with dissolve
        nami "How about a deal?! For a certain amount of [Berries.n], I wouldn't mind doing it:"
        $ nami_breasts += 1
    else:
        player "How are you, [nami.n]? Could you show me your breasts again?"
        nami "Captain!! you love my breasts?, I'd love to show you again, but first, we need to come to an agreement..."


    menu:
        "20 [Berries.n]" if berries >= 20:
            call nami_check pass (check_love = 8, check_lust = 8, check_berries = 20) from _nami_check_breasts_20
            show nami happy with dissolve

            $ talk_random = renpy.random.choice([
                _("Excellent!! a pleasure doing business with you captain... all yours..."),
                _("It's always a pleasure doing business with you, Captain!!"),
            ])

        "Bargain, 10 [Berries.n]" if berries >= 10:
            call nami_check pass (check_love = 9, check_lust = 9, check_berries = 10) from _nami_check_breasts_10
            show nami happy with dissolve

            $ talk_random = renpy.random.choice([
                _("well!! just for you, captain... i hope you enjoy it..."),
                _("You're a good negotiator, Captain. I'll only accept because it's you!"),
            ])

        "No payment":
            call nami_check pass (check_love = 10, check_lust = 10, check_berries = 0) from _nami_check_breasts_0
            show nami neutral with dissolve

            $ talk_random = renpy.random.choice([
                _("Consider it a favor just for you, captain! Don't think I'm that easy..."),
                _("You caught me on a good day, Captain... Don't think I'm an easy girl!"),
            ])

    nami "[talk_random]"

    window hide
    show nami c1_breasts with dissolve
    pause 1
    show nami neutral with Dissolve(0.2)
    window auto
    
    $ nami_lust += 2
    narrador "[nami.n] lust +2"

    show nami c1 with dissolve

    jump nami_goodbye