# Version event: 1
# Version game: 0.23

label vivi_show:
    menu:
        "Show tongue":
            call event_vivi_tongue from _call_event_vivi_tongue

        "Show Bra":
            call event_vivi_bra from _call_event_vivi_bra

        "Show Underwear":
            call event_vivi_underwear from _call_event_vivi_underwear

        "Show Breasts":
            call event_vivi_breasts from _call_event_vivi_breasts
                
        "Show Naked":
            call event_vivi_naked from _call_event_vivi_naked
                    
        "Back":
            jump vivi_lewd

    pause 1
    window auto
    show vivi neutral with Dissolve(0.2)

    $ vivi_lust += 1
    narrador "[vivi.n] lust +1"

    jump vivi_bye






