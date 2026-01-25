# Version event: 1
# Version game: 0.18

default pell_name = "Pell"

define pell       = createCharacter('[pell_name]', color="#0b7c47", image="pell")

layeredimage pell:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "pell c1 pell_c1"