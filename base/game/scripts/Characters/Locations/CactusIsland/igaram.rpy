# Version event: 1
# Version game: 0.18

default igaram_name = "???"

define igaram       = createCharacter('[igaram_name]', color="#f0e269", image="igaram")

layeredimage igaram:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "igaram c1 igaram_c1"
