# Version event: 3
# Version game: 0.31

default robin_name = "Robin"

define robin      = createCharacter('[robin_name]', color="#09195f", image="robin")

default robin_love = 0
default robin_lust = 0

default robin_crew = True

layeredimage robin:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "robin c1 robin_c1"

        attribute c1_bra:
            "robin c1 robin_c1_bra"
    
        attribute c1_breasts:
            "robin c1 robin_c1_breasts"

        attribute c1_underwear:
            "robin c1 robin_c1_underwear"

        attribute c1_naked:
            "robin c1 robin_c1_naked"

    group face:
        attribute neutral default:
            "robin faces robin_neutral"
        attribute happy: 
            "robin faces robin_happy"
        attribute smile:
            "none"
        attribute anger: 
            "robin faces robin_anger"
        attribute shame: 
            "robin faces robin_shame"
        attribute tongue:
            "robin faces robin_tongue"
        attribute annoyed: 
            "robin faces robin_annoyed"
            

label set_name_robin():
    call screen s_set_girl_name(nameGirl = "Robin")
    
    $ robin_name = _return.strip()

    return