# Version event: 1
# Version game: 0.14

default nami_bra = 0

label event_nami_bra:
    if nami_bra == 0:
        player "How are you, [nami.n]? You are so attractive while leading us through the seas, I would like to admire your beauty again..." 
        player "It might sound strange, but could you show me your bra?"
        show nami c1 shame with dissolve            
        nami "Captain!! your request totally caught me off guard... I didn't know you were interested in those kinds of proposals..."

        show nami neutral with dissolve
        nami "How about a deal?! for a certain amount of [Berries.n], i wouldn't mind..."
        $ nami_bra += 1
    else:
        player "How are you, [nami.n]? I know it might sound strange, but could you show me your bra again?"
        nami "Captain!! Again with these strange requests... But as you know, we can come to an agreement..."


    menu:
        "20 [Berries.n]" if berries >= 20:
            call nami_check pass (check_love = 2, check_lust = 2, check_berries = 20) from _nami_check_bra_20

            show nami happy with dissolve
            $ talk_random = renpy.random.choice([
                _("Excellent!! a pleasure doing business with you captain... all yours..."),
                _("It's always a pleasure doing business with you, Captain!!"),
            ])

        "Bargain, 10 [Berries.n]" if berries >= 10:
            call nami_check pass (check_love = 3, check_lust = 3, check_berries = 10) from _nami_check_bra_10

            show nami happy with dissolve
            $ talk_random = renpy.random.choice([
                _("well!! just for you, captain... i hope you enjoy it..."),
                _("You're a good negotiator, Captain. I'll only accept because it's you!"), 
            ])

        "No payment":
            call nami_check pass (check_love = 4, check_lust = 4, check_berries = 0) from _nami_check_bra_0
            
            show nami neutral with dissolve
            $ talk_random = renpy.random.choice([
                _("Consider it a favor just for you, captain! Don't think I'm that easy..."),
                _("You caught me on a good day, Captain... Don't think I'm an easy girl!"),
            ])

    nami "[talk_random]"

    window hide
    show nami c1_bra with dissolve
    pause 1
    show nami neutral with Dissolve(0.2)
    window auto

    $ nami_lust += 1
    narrador "[nami.n] lust +1"

    show nami c1 with dissolve

    jump nami_goodbye
