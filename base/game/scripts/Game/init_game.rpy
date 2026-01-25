# Version event: 1
# Version game: 0.1

default played_version = "0.1"
default hide_label = None

label init_game:
    python:
        played_version = config.version
        game = gameObject()

    return

