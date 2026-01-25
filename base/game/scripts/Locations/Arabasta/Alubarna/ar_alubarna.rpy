# Version event: 3
# Version game: 0.23

#label ar_alubarna():
#    $ renpy.show_screen("s_map_arabasta_nohide", _layer="master")
#    narrador "Event not available in this version, please wait for v0.23"
#    #. narrador "This event is available in version 0.22.\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
#    jump map_arabasta

label ar_alubarna():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True
    $ game.location = "ar_alubarna"
    $ arabasta_location = "Alubarna"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    #. sound casino
    $ music_arabasta()
    jump m_ar_alubarna

label m_ar_alubarna():

    if Arabasta.h == 13:
        jump ar_alubarna_h

    menu:
        "Go to Palace" if not game.clock.night:
            jump ar_alubarna_palace

        "Map" if map_arabasta and not game.clock.night:
            jump map_arabasta

        "Back":
            jump arabasta

