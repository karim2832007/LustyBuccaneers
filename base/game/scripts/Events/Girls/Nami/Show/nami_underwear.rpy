# Version event: 1
# Version game: 0.14

default nami_underwear = 0

label event_nami_underwear:
    if nami_underwear == 0:
        player "How are you, [nami.n]? after seeing you often sunbathing, I would like to admire your beauty again..." 
        player "It might sound strange, but could you show me your underwear?"
        show nami c1 shame with dissolve              
        nami "Captain!! Getting more direct each time... But you know that we can always reach an agreement..."
        show nami neutral with dissolve
        nami "How about a deal?! for a certain amount of [Berries.n], I wouldn't mind..."
        $ nami_underwear += 1
    else:
        player "Hey [nami.n]! Your sexy figure is unforgettable. Could you perhaps show me your underwear again?"
        nami "Captain!! Do you really like seeing me in my underwear that much?... I'd love to show you again, but first, we need to come to an agreement..."

    menu:
        "20 [Berries.n]" if berries >= 20:
            call nami_check pass (check_love = 5, check_lust = 5, check_berries = 20) from _nami_check_underwear_20
            show nami happy with dissolve

            $ talk_random = renpy.random.choice([
                _("Excellent!! a pleasure doing business with you captain... all yours..."),
                _("It's always a pleasure doing business with you, Captain!!"),
            ])

        "Bargain, 10 [Berries.n]" if berries >= 10:
            call nami_check pass (check_love = 6, check_lust = 6, check_berries = 10) from _nami_check_underwear_10
            show nami happy with dissolve

            $ talk_random = renpy.random.choice([
                _("well!! just for you, captain... i hope you enjoy it..."),
                _("You're a good negotiator, Captain. I'll only accept because it's you!"),
            ])

        "No payment":
            call nami_check pass (check_love = 7, check_lust = 7, check_berries = 0) from _nami_check_underwear_0
            show nami neutral with dissolve

            $ talk_random = renpy.random.choice([
                _("Consider it a favor just for you, captain! Don't think I'm that easy..."),
                _("You caught me on a good day, Captain... Don't think I'm an easy girl!"),
            ])


    nami "[talk_random]"

    window hide
    show nami c1_underwear with dissolve
    pause 1
    show nami neutral with Dissolve(0.2)
    window auto
    
    $ nami_lust += 1
    narrador "[nami.n] lust +1"

    show nami c1 with dissolve

    jump nami_goodbye