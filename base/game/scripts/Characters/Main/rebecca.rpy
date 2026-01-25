# Version event: 1
# Version game: 0.17

default rebecca_name = "Rebecca"

define rebecca      = createCharacter('[rebecca_name]', color="#ff9ecf", image="rebecca")

default rebecca_love = 0
default rebecca_lust = 0
default rebecca_subm = 0 # docil slave

default rebecca_crew = False

layeredimage rebecca:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "rebecca c1 rebecca_c1"

        attribute c1_bra:
            "rebecca c1 rebecca_c1_bra"
    
        attribute c1_breasts:
            "rebecca c1 rebecca_c1_breasts"

        attribute c1_underwear:
            "rebecca c1 rebecca_c1_underwear"

        attribute c1_naked:
            "rebecca c1 rebecca_c1_naked"

        attribute c2:  
            "rebecca c2 rebecca_c2"

    group face:
        attribute neutral default:
            "none"
        attribute happy: 
            "rebecca faces rebecca_happy"
        attribute annoyed: 
            "rebecca faces rebecca_annoyed"
        attribute serious: 
            "rebecca faces rebecca_serious"
        attribute anger: 
            "rebecca faces rebecca_anger"
        attribute shame: 
            "rebecca faces rebecca_shame"
        attribute tongue:
            "rebecca faces rebecca_tongue"

    group head:
        yoffset -128
        attribute default:
            "none"
        attribute helmet:
            "rebecca head rebecca_helmet"

    group hp:
        attribute default:
            "none"
        attribute c2_wounds:
            "rebecca c2 rebecca_c2_wounds"
        


label set_name_rebecca():
    call screen s_set_girl_name(nameGirl="Rebecca")
    
    $ rebecca_name = _return.strip()

    return