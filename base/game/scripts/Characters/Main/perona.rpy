# Version event: 1
# Version game: 0.1

default perona_name = "Perona"

define perona      = createCharacter('[perona_name]', color="#ff51a2", image="perona")

default perona_love = 0
default perona_lust = 0
default perona_subm = 0 # docil slave

default perona_crew = False

layeredimage perona:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "perona c1 perona_c1"

        attribute c1_bra:
            "perona c1 perona_c1_bra"
    
        attribute c1_breasts:
            "perona c1 perona_c1_breasts"

        attribute c1_underwear:
            "perona c1 perona_c1_underwear"

        attribute c1_naked:
            "perona c1 perona_c1_naked"

    group face:
        attribute neutral default:
            "none"
        attribute happy: 
            "perona faces perona_happy"
        attribute anger: 
            "perona faces perona_anger"
        attribute shame: 
            "perona faces perona_shame"
        attribute tongue:
            "perona faces perona_tongue"
        attribute serious:
            "perona faces perona_serious"
        attribute annoyed:
            "perona faces perona_annoyed"


label set_name_perona():
    call screen s_set_girl_name(nameGirl = "Perona")
    
    $ perona_name = _return.strip()

    return