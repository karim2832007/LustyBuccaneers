# Version event: 1
# Version game: 0.26

default koby_name = "Koby"

define koby       = createCharacter('[koby_name]', color="#d1fc8b", image="koby")

default koby_debut = False

layeredimage koby:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "koby c1 koby_c1"

    group face:
        attribute neutral default:
            "none"
        attribute serious: 
            "koby faces koby_serious"
