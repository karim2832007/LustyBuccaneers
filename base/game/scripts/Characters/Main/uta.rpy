# Version event: 2
# Version game: 0.28

default uta_name = "Uta"

define uta      = createCharacter('[uta_name]', color="#9f5ad8", image="uta")

default uta_love = 0
default uta_lust = 0
default uta_subm = 0 # docil slave

default uta_crew = False

layeredimage uta:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "uta c1 uta_c1"

        attribute c1_bra:
            "uta c1 uta_c1_bra"
    
        attribute c1_breasts:
            "uta c1 uta_c1_breasts"

        attribute c1_underwear:
            "uta c1 uta_c1_underwear"

        attribute c1_naked:
            "uta c1 uta_c1_naked"

    group face:
        attribute neutral default:
            "none"
        attribute happy: 
            "uta faces uta_happy"
        attribute annoyed: 
            "uta faces uta_annoyed"
        attribute serious: 
            "uta faces uta_serious"
        attribute anger: 
            "uta faces uta_anger"
        attribute shame: 
            "uta faces uta_shame"
        attribute tongue:
            "uta faces uta_tongue"


label set_name_uta():
    call screen s_set_girl_name(nameGirl="Uta")
    
    $ uta_name = _return.strip()

    return