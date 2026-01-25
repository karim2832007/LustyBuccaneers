# Version event: 1
# Version game: 0.28

label uta_chat:

    show uta c1 with dissolve

    uta "Hello, [player.n]. Is something wrong?"

    menu uta_chat_menu:
        "Hangout":
            jump uta_hangout

        "Give":
            call uta_give from _call_uta_give_chat
            jump uta_chat_menu

        "Dismiss Her":
            jump uta_dismiss
    