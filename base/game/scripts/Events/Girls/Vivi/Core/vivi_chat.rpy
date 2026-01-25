# Version event: 1
# Version game: 0.23

label vivi_chat:

    show vivi c1 with dissolve

    vivi "Hello, [player.n]. Is something wrong?"

    menu vivi_chat_menu:
        "Hangout":
            jump vivi_hangout

        "Give":
            call vivi_give from _call_vivi_give_chat
            jump vivi_chat_menu

        "Dismiss Her":
            jump vivi_dismiss
    