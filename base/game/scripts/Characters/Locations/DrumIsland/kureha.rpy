# Version event: 1
# Version game: 0.1

default kureha_name = "Kureha"

define kureha      = createCharacter('[kureha_name]', color="#f58bde", image="kureha")

default kureha_love = 0
default kureha_lust = 0
default kureha_subm = 0 # docil slave

default kureha_crew = False

layeredimage kureha:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "kureha c1 kureha_c1"

#        attribute c1_bra:
#            "kureha c1 kureha_c1_bra"
#    
#        attribute c1_breasts:
#            "kureha c1 kureha_c1_breasts"
#
#        attribute c1_underwear:
#            "kureha c1 kureha_c1_underwear"
#
#        attribute c1_naked:
#            "kureha c1 kureha_c1_naked"
#
#    group face:
#        attribute neutral default:
#            "none"
#        attribute happy: 
#            "kureha faces kureha_happy"
#        attribute anger: 
#            "kureha faces kureha_anger"
#        attribute shame: 
#            "kureha faces kureha_shame"
#        attribute tongue:
#            "kureha faces kureha_tongue"



label set_name_kureha():
    call screen s_set_girl_name( nameGirl = "Kureha" )
    
    $ kureha_name = _return.strip()

    return