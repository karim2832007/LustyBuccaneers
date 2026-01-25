# Version event: 1
# Version game: 0.32

define police1      = createCharacter('Police 1', color="#1b2134", image="police_1")

layeredimage police1:
    zoom 1
    yoffset +1

    always:
        "police police_1"

define police2      = createCharacter('Police 2', color="#1b2134", image="police_2")

layeredimage police2:
    zoom 1
    yoffset +1

    always:
        "police police_2"