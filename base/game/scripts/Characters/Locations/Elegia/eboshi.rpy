# Version event: 1
# Version game: 0.25

default eboshi_name = "Eboshi"

define eboshi       = createCharacter('[eboshi_name]', color="#d865bb", image="eboshi")

layeredimage eboshi:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "eboshi c1 eboshi_c1"