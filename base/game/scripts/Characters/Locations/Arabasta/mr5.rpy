# Version event: 1
# Version game: 0.18

default mr5_name = "Mr. 5"

define mr5       = createCharacter('[mr5_name]', color="#83682e", image="mr5")

layeredimage mr5:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "mr5 c1 mr5_c1"
