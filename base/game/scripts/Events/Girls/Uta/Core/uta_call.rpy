# Version event: 1
# Version game: 0.28

label uta_call:

    show uta c1 with dissolve

    uta "Hello, [player.n]. Is something wrong?"

    menu menu_uta_call:
        "Normal Chatting":
            jump uta_hangout

        "Lewd":
            jump uta_lewd

        "Give":
            call uta_give from _call_uta_give_call
            jump menu_uta_call

        "Dismiss Her":
            jump uta_dismiss
    