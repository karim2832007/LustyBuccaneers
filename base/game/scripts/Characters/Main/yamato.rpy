# Version event: 1
# Version game: 0.1

default yamato_name = "Yamato"

define yamato      = createCharacter('[yamato_name]', color="#fc4120", image="yamato")

default yamato_love = 0
default yamato_lust = 0

default yamato_crew = True

layeredimage yamato:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "yamato c1 yamato_c1"

        attribute c1_bra:
            "yamato c1 yamato_c1_bra"
    
        attribute c1_breasts:
            "yamato c1 yamato_c1_breasts"

        attribute c1_underwear:
            "yamato c1 yamato_c1_underwear"

        attribute c1_naked:
            "yamato c1 yamato_c1_naked"

    group face:
        attribute neutral default:
            "none"
        attribute smile: 
            "yamato faces yamato_smile"
        attribute happy: 
            "yamato faces yamato_happy"
        attribute annoyed: 
            "yamato faces yamato_annoyed"
        attribute serious: 
            "yamato faces yamato_serious"
        attribute anger: 
            "yamato faces yamato_anger"
        attribute shame: 
            "yamato faces yamato_shame"
        attribute tongue:
            "yamato faces yamato_tongue"



label set_name_yamato():
    call screen s_set_girl_name(nameGirl = "Yamato")
    
    $ yamato_name = _return.strip()

    return