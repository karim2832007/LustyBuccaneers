# Version event: 1
# Version game: 0.1

default zala_name = "???"

define zala       = createCharacter('[zala_name]', color="#027056", image="zala")

default zala_love = 0
default zala_lust = 0

layeredimage zala:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "zala c1 zala_c1"
#
#        attribute c1_bra:
#            "zala c1 zala_c1_bra"
#    
#        attribute c1_breasts:
#            "zala c1 zala_c1_breasts"
#
#        attribute c1_underwear:
#            "zala c1 zala_c1_underwear"
#
#        attribute c1_naked:
#            "zala c1 zala_c1_naked"

#    group face:
#        attribute neutral default:
#            "none"
#        attribute happy: 
#            "zala faces zala_happy"
#        attribute anger: 
#            "zala faces zala_anger"
#        attribute shame: 
#            "zala faces zala_shame"
#        attribute tongue:
#            "zala faces zala_tongue"


label set_name_zala():

    show screen zala_wanted

    call screen s_set_girl_name(nameGirl="Zala")

    $ zala_name = _return.strip()

    hide screen zala_wanted

    return

screen zala_wanted():
    add "GUI girls_stats stats_wanted_back":
        xalign 0.5
        yalign 0.5  
    
    add "enemy_zala":
        zoom 1.45
        crop (0, 0, 512, 400)
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