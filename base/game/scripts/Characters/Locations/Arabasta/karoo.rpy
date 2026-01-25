# Version event: 1
# Version game: 0.18

default karoo_name = "Karoo"

define karoo       = createCharacter('[karoo_name]', color="#027056", image="karoo")

layeredimage karoo:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "karoo c1 karoo_c1"
