# Version event: 2
# Version game: 0.35

#default spartan_name = "Spartan"
define spartan      = createCharacter('Spartan', color="#e44040", image="spartan")

layeredimage spartan:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "spartan c1 spartan_c1"