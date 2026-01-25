# Version event: 1
# Version game: 0.1

default toto_name = "???"

define toto       = createCharacter('[toto_name]', color="#ffefc4", image="toto")

default toto_love = 0
default toto_lust = 0

layeredimage toto:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "toto c1 toto_c1"

    group face:
        attribute neutral default:
            "none"
        attribute pervert: 
            "toto faces toto_pervert"
        attribute happy: 
            "toto faces toto_happy"



label set_name_toto():
    call screen s_set_girl_name(nameGirl = "Toto")
    
    $ toto_name = _return.strip()

    return