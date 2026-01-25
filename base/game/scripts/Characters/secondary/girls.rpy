# Version event: 1
# Version game: 0.32

define girl_1      = createCharacter('Blonde Girl', color="#fffb00", image="police_1")

layeredimage girl_1:
    zoom 1
    yoffset +1

    always:
        "random girl_1"

define girl_2      = createCharacter('Brunette Girl', color="#cf5d00", image="police_2")

layeredimage girl_2:
    zoom 1
    yoffset +1

    always:
        "random girl_2"