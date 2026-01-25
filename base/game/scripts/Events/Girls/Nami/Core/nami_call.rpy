# Version event: 1
# Version game: 0.14

label nami_call:

    show nami c1 with dissolve

    nami "Hello, Captain. Do you need anything from me?"

    menu nami_call_menu:
        "Normal Chatting":
            jump nami_hangout

        "Lewd":
            jump nami_lewd

        "Give":
            call nami_give from _call_nami_give_call
            jump nami_call_menu

        "Dismiss Her":
            jump nami_dismiss