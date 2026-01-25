# Version event: 1
# Version game: 0.35

default sarquiss_name = "Thug"

define sarquiss      = createCharacter('[sarquiss_name]', color="#97f3ff", image="sarquiss")

layeredimage sarquiss:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "sarquiss sarquiss_c1"