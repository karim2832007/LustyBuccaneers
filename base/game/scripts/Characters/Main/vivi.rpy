# Version event: 1
# Version game: 0.17

default vivi_name = "Vivi"

define vivi      = createCharacter('[vivi_name]', color="#75d3ff", image="vivi")

default vivi_love = 0
default vivi_lust = 0
default vivi_subm = 0 # docil slave

default vivi_crew = False

layeredimage vivi:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "vivi c1 vivi_c1"

        attribute c1_bra:
            "vivi c1 vivi_c1_bra"
    
        attribute c1_breasts:
            "vivi c1 vivi_c1_breasts"

        attribute c1_underwear:
            "vivi c1 vivi_c1_underwear"

        attribute c1_naked:
            "vivi c1 vivi_c1_naked"

    group face:
        attribute neutral default:
            "none"
        attribute happy: 
            "vivi faces vivi_happy"
        attribute annoyed: 
            "vivi faces vivi_annoyed"
        attribute serious: 
            "vivi faces vivi_serious"
        attribute anger: 
            "vivi faces vivi_anger"
        attribute shame: 
            "vivi faces vivi_shame"
        attribute tongue:
            "vivi faces vivi_tongue"


label set_name_vivi():
    call screen s_set_girl_name(nameGirl="Vivi")
    
    $ vivi_name = _return.strip()

    return