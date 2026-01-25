# Version event: 1
# Version game: 0.28

label uta_show:
    menu:
        "Show tongue":
            call event_uta_tongue from _call_event_uta_tongue

        "Show Bra":
            call event_uta_bra from _call_event_uta_bra

        "Show Underwear":
            call event_uta_underwear from _call_event_uta_underwear

        "Show Breasts":
            call event_uta_breasts from _call_event_uta_breasts
                
        "Show Naked":
            call event_uta_naked from _call_event_uta_naked
                    
        "Back":
            jump uta_lewd

    pause 1
    window auto
    show uta neutral with Dissolve(0.2)

    $ uta_lust += 1
    narrador "[uta.n] lust +1"

    jump uta_bye






