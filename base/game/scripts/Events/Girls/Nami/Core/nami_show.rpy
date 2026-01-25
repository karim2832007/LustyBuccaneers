# Version event: 1
# Version game: 0.14

label nami_show:
    menu:
        "Show tongue":
            call event_nami_tongue from _call_event_nami_tongue

        "Show Bra":
            call event_nami_bra from _call_event_nami_bra

        "Show Underwear":
            call event_nami_underwear from _call_event_nami_underwear

        "Show Breasts":
            call event_nami_breasts from _call_event_nami_breasts
                
        "Show Naked":
            call event_nami_naked from _call_event_nami_naked
                    
        "Back":
            jump nami_lewd

    pause 1
    window auto
    show nami neutral with Dissolve(0.2)

    $ nami_lust += 1
    narrador "[nami.n] lust +1"

    jump nami_bye






