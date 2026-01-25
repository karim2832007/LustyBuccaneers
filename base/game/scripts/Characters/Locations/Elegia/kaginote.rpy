# Version event: 1
# Version game: 0.26

default kaginote_name = "Kaginote"

define kaginote       = createCharacter('[kaginote_name]', color="#a76cc9", image="kaginote")

layeredimage kaginote:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "kaginote c1 kaginote_c1"