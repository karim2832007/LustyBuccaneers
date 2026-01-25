# Version event: 1
# Version game: 0.26

default hanagasa_name = "Hanagasa"

define hanagasa       = createCharacter('[hanagasa_name]', color="#9339c7", image="hanagasa")

layeredimage hanagasa:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "hanagasa c1 hanagasa_c1"