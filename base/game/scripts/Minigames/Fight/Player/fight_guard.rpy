# Version event: 1
# Version game: 0.23

label fight_guard():
    $ player_guard = True

    $ talk_random = renpy.random.choice([
            _("You assume a defensive stance"),
            _("You prepare to block!"),
        ])

    narrador "[talk_random]"

    return