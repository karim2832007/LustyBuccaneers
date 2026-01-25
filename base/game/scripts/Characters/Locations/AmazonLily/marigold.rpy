# Version event: 1
# Version game: 0.1

default marigold_name = "Marigold"

define marigold      = createCharacter('[marigold_name]', color="#f3f58b", image="marigold")

default marigold_love = 0
default marigold_lust = 0
default marigold_subm = 0 # docil slave

default marigold_crew = False

#layeredimage marigold:
#    zoom 1
#    yoffset +1
#
#    group cloths:
#        attribute c1 default:
#            "marigold c1 marigold_c1"
#
#        attribute c1_stone:
#            "marigold c1 marigold_c1_stone"
#
#        attribute c1_bra:
#            "marigold c1 marigold_c1_bra"
#    
#        attribute c1_breasts:
#            "marigold c1 marigold_c1_breasts"
#
#        attribute c1_underwear:
#            "marigold c1 marigold_c1_underwear"
#
#        attribute c1_naked:
#            "marigold c1 marigold_c1_naked"
#
#    group face:
#        attribute neutral default:
#            "none"
#        attribute happy: 
#            "marigold faces marigold_happy"
#        attribute anger: 
#            "marigold faces marigold_anger"
#        attribute shame: 
#            "marigold faces marigold_shame"
#        attribute tongue:
#            "marigold faces marigold_tongue"



label set_name_marigold():
    call screen s_set_girl_name( nameGirl = "Marigold")
    
    $ marigold_name = _return.strip()

    return

