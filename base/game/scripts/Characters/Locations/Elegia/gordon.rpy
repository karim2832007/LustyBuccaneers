# Version event: 1
# Version game: 0.26

default gordon_name = "Gordon"

define gordon       = createCharacter('[gordon_name]', color="#acacac", image="gordon")

layeredimage gordon:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "gordon c1 gordon_c1"