# Version event: 1
# Version game: 0.1

default alvida_name = "???"

define alvida       = createCharacter('[alvida_name]', color="#027056", image="alvida")



default alvida_love = 0
default alvida_lust = 0

layeredimage alvida:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "alvida c1 alvida_c1"

#        attribute c1_bra:
#            "alvida c1 alvida_c1_bra"
#    
#        attribute c1_breasts:
#            "alvida c1 alvida_c1_breasts"
#
#        attribute c1_underwear:
#            "alvida c1 alvida_c1_underwear"
#
        attribute c1_naked:
            "alvida c1 alvida_c1_naked"

    group face:
        attribute neutral default:
            "none"
#        attribute happy: 
#            "alvida faces alvida_happy"
        attribute anger: 
            "alvida faces alvida_anger"
#        attribute shame: 
#            "alvida faces alvida_shame"
#        attribute tongue:
#            "alvida faces alvida_tongue"


label set_name_alvida():

    show screen alvida_wanted

    call screen s_set_girl_name(nameGirl = "Alvida")

    $ alvida_name = _return.strip()

    hide screen alvida_wanted

    return

screen alvida_wanted():
    add "GUI girls_stats stats_wanted_back":
        xalign 0.5
        yalign 0.5  
    
    add "alvida":
        zoom 0.6
        xalign 0.5
        yalign 0.45

    add "GUI girls_stats stats_wanted":
        xalign 0.5
        yalign 0.5

    text "WANTED":
        font gui.wanted_text_font
        color "#6b5440"
        xalign 0.5
        #yalign 0.30
        yoffset 108
        size 130