# Version event: 1
# Version game: 0.34

default rayleigh_name = "Old man"
#The old man

define rayleigh       = createCharacter('[rayleigh_name]', color="#ffffff", image="rayleigh")

layeredimage rayleigh:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "rayleigh c1 rayleigh_c1"