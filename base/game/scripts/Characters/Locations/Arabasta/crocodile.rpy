# Version event: 1
# Version game: 0.18

default crocodile_name = "Crocodile"

define crocodile       = createCharacter('[crocodile_name]', color="#0b7c47", image="crocodile")

layeredimage crocodile:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "crocodile c1 crocodile_c1"