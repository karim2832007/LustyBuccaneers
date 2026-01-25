# Version event: 1
# Version game: 0.18

default koza_name = "Koza"

define koza       = createCharacter('[koza_name]', color="#b12e0e", image="koza")

layeredimage koza:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "koza c1 koza_c1"
        
        attribute c1_hurt:
            "koza c1 koza_c1_hurt"