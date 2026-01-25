# Version event: 1
# Version game: 0.1

default marguerite_name = "Marguerite"

define marguerite      = createCharacter('[marguerite_name]', color="#f3f58b", image="marguerite")

default marguerite_love = 0
default marguerite_lust = 0
default marguerite_subm = 0 # docil slave

default marguerite_crew = False

layeredimage marguerite:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "marguerite c1 marguerite_c1"

        attribute c1_stone:
            "marguerite c1 marguerite_c1_stone"

#        attribute c1_bra:
#            "marguerite c1 marguerite_c1_bra"
#    
#        attribute c1_breasts:
#            "marguerite c1 marguerite_c1_breasts"
#
#        attribute c1_underwear:
#            "marguerite c1 marguerite_c1_underwear"
#
#        attribute c1_naked:
#            "marguerite c1 marguerite_c1_naked"
#
#    group face:
#        attribute neutral default:
#            "none"
#        attribute happy: 
#            "marguerite faces marguerite_happy"
#        attribute anger: 
#            "marguerite faces marguerite_anger"
#        attribute shame: 
#            "marguerite faces marguerite_shame"
#        attribute tongue:
#            "marguerite faces marguerite_tongue"



label set_name_marguerite():
    call screen s_set_girl_name( nameGirl = "Marguerite" )
    
    $ marguerite_name = _return.strip()

    return