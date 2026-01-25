# Version event: 1
# Version game: 0.12

label hancock_call:

    show hancock c1 with dissolve

    hancock "Hello, [player.n]. Is something wrong?"

    menu menu_hancock_call:
        "Normal Chatting":
            jump hancock_hangout

        "Lewd":
            jump hancock_lewd

        "Give":
            call hancock_give from _call_hancock_give_call
            jump menu_hancock_call

        "Dismiss Her":
            jump hancock_dismiss
    