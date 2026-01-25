# Version event: 1
# Version game: 0.12

label hancock_chat:

    show hancock c1 with dissolve

    hancock "Hello, [player.n]. Is something wrong?"

    menu hancock_chat_menu:
        "Hangout":
            jump hancock_hangout

        "Give":
            call hancock_give from _call_hancock_give_chat
            jump hancock_chat_menu

        "Dismiss Her":
            jump hancock_dismiss
    