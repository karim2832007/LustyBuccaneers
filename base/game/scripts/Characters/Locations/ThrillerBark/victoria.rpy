# Version event: 1
# Version game: 0.1

default victoria_name = "victoria"

define victoria      = createCharacter('[victoria_name]', color="#e3e64c", image="victoria")

default victoria_love = 0
default victoria_lust = 0
default victoria_subm = 0 # docil slave

default victoria_crew = False

layeredimage victoria:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "victoria c1 victoria_c1"

#        attribute c1_bra:
#            "victoria c1 victoria_c1_bra"
#    
#        attribute c1_breasts:
#            "victoria c1 victoria_c1_breasts"
#
#        attribute c1_underwear:
#            "victoria c1 victoria_c1_underwear"
#
#        attribute c1_naked:
#            "victoria c1 victoria_c1_naked"
#
#    group face:
#        attribute neutral default:
#            "none"
#        attribute happy: 
#            "victoria faces victoria_happy"
#        attribute anger: 
#            "victoria faces victoria_anger"
#        attribute shame: 
#            "victoria faces victoria_shame"
#        attribute tongue:
#            "victoria faces victoria_tongue"


label set_name_victoria():
    call screen s_set_girl_name( nameGirl = "Cindry" )
    
    $ victoria_name = _return.strip()

    return