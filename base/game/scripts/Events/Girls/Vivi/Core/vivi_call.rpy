# Version event: 1
# Version game: 0.23

label vivi_call:

    show vivi c1 with dissolve

    vivi "Hello, [player.n]. Is something wrong?"

    menu menu_vivi_call:
        "Normal Chatting":
            jump vivi_hangout

        "Lewd":
            jump vivi_lewd

        "Give":
            call vivi_give from _call_vivi_give_call
            jump menu_vivi_call

        "Dismiss Her":
            jump vivi_dismiss
    