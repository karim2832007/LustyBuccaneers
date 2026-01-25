# Version event: 1
# Version game: 0.14

label nami_chat:

    show nami c1 with dissolve

    nami "Hello, Captain. Do you need anything from me?"

    menu nami_chat_menu:
        "Hangout":
            jump nami_hangout

        "Give":
            call nami_give from _call_nami_give_chat
            jump nami_chat_menu

        "Dismiss Her":
            jump nami_dismiss
    