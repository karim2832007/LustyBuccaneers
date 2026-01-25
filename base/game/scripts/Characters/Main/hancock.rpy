# Version event: 1
# Version game: 0.1

default hancock_name = "Hancock"

define hancock      = createCharacter('[hancock_name]', color="#8b3879", image="hancock")

default hancock_love = 0
default hancock_lust = 0
default hancock_subm = 0 # docil slave

default hancock_crew = False

layeredimage hancock:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "hancock c1 hancock_c1"

        attribute c1_bra:
            "hancock c1 hancock_c1_bra"
    
        attribute c1_breasts:
            "hancock c1 hancock_c1_breasts"

        attribute c1_underwear:
            "hancock c1 hancock_c1_underwear"

        attribute c1_naked:
            "hancock c1 hancock_c1_naked"

    group face:
        attribute neutral default:
            "none"
        attribute happy: 
            "hancock faces hancock_happy"
        attribute annoyed: 
            "hancock faces hancock_annoyed"
        attribute serious: 
            "hancock faces hancock_serious"
        attribute anger: 
            "hancock faces hancock_anger"
        attribute shame: 
            "hancock faces hancock_shame"
        attribute tongue:
            "hancock faces hancock_tongue"


label set_name_hancock():
    call screen s_set_girl_name( nameGirl = "Hancock" )
    
    $ hancock_name = _return.strip()

    return