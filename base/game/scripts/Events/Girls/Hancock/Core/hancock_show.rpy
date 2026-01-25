# Version event: 1
# Version game: 0.12

label hancock_show:
    menu:
        "Show tongue":
            call event_hancock_tongue from _call_event_hancock_tongue

        "Show Bra":
            call event_hancock_bra from _call_event_hancock_bra

        "Show Underwear":
            call event_hancock_underwear from _call_event_hancock_underwear

        "Show Breasts":
            call event_hancock_breasts from _call_event_hancock_breasts
                
        "Show Naked":
            call event_hancock_naked from _call_event_hancock_naked
                    
        "Back":
            jump hancock_lewd

    pause 1
    window auto
    show hancock neutral with Dissolve(0.2)

    $ hancock_lust += 1
    narrador "[hancock.n] lust +1"

    jump hancock_bye






