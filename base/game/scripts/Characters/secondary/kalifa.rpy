# Version event: 1
# Version game: 0.24

default kalifa_name = "Kalifa"

define kalifa      = createCharacter('[kalifa_name]', color="#f1ef60", image="kalifa")

default kalifa_love = 0
default kalifa_lust = 0
default kalifa_subm = 0 # docil slave

default kalifa_crew = False

layeredimage kalifa:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "kalifa c1 kalifa_c1"

#        attribute c1_bra:
#            "kalifa c1 kalifa_c1_bra"
#    
#        attribute c1_breasts:
#            "kalifa c1 kalifa_c1_breasts"
#
#        attribute c1_underwear:
#            "kalifa c1 kalifa_c1_underwear"
#
#        attribute c1_naked:
#            "kalifa c1 kalifa_c1_naked"

    group face:
        attribute neutral default:
            "none"
#        attribute happy: 
#            "kalifa faces kalifa_happy"
#        attribute annoyed: 
#            "kalifa faces kalifa_annoyed"
#        attribute serious: 
#            "kalifa faces kalifa_serious"
#        attribute anger: 
#            "kalifa faces kalifa_anger"
#        attribute shame: 
#            "kalifa faces kalifa_shame"
#        attribute tongue:
#            "kalifa faces kalifa_tongue"


label set_name_kalifa():
    call screen s_set_girl_name(nameGirl="Kalifa")
    
    $ kalifa_name = _return.strip()

    return