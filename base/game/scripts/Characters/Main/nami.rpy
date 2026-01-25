# Version event: 2
# Version game: 0.24

default nami_name = "Nami"

define nami      = createCharacter('[nami_name]', color="#ff9100", image="nami")

default nami_love = 0
default nami_lust = 0

default nami_crew = True

# outfits
default nami_c2 = False

# Nami
layeredimage nami:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "nami c1 nami_c1"
        attribute c1_bra:
            "nami c1 nami_c1_bra"
        attribute c1_breasts:
            "nami c1 nami_c1_breasts"
        attribute c1_underwear:
            "nami c1 nami_c1_underwear"
        attribute c1_naked:
            "nami c1 nami_c1_naked"

        attribute c2:
            "nami c2 nami_c2"


    group face:
        attribute neutral default:
            "none"
        attribute happy: 
            "nami faces nami_happy"
        attribute anger: 
            "nami faces nami_anger"
        attribute shame: 
            "nami faces nami_shame"
        attribute tongue:
            "nami faces nami_tongue"
        attribute serious: 
            "nami faces nami_serious"
        attribute joke: 
            "nami faces nami_joke"
        attribute berries: 
            "nami faces nami_berries"
        attribute annoyed: 
            "nami faces nami_annoyed"


label set_name_nami():
    call screen s_set_girl_name(nameGirl = "Nami")

    $ nami_name = _return.strip()

    return