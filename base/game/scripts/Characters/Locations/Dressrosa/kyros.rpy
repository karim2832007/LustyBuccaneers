# Version event: 1
# Version game: 0.32

default kyros_name = "Small Toy Soldier" # Kyros

define kyros      = createCharacter('[kyros_name]', color="#e44040", image="Kyros")

layeredimage kyros:
    zoom 1
    yoffset +1

    group cloths:
        attribute toy default:
            "kyros toy kyros_toy"

    group face:
        attribute neutral default:
            "none"