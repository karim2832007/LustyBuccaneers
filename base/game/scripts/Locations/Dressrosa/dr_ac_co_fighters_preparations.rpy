# Version event: 2
# Version game: 0.34

#Fighters' Preparations Room
label dr_ac_co_fighters_preparations():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "dr_ac_co_fighters_preparations"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ music_dressrosa()
    jump m_dr_ac_co_fighters_preparations

label m_dr_ac_co_fighters_preparations():
    if Dressrosa.h == 5:
        jump dressrosa_h5

    menu:
        "Administration Room" if Dressrosa.h == 18:
            #narrador "This event is available in version 0.[version_id_next].\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
            narrador "Event not available in this version, please wait for v0.[version_id_next]"
            jump m_dr_ac_co_fighters_preparations

        "Go to the Arena" if Dressrosa.h >= 6 and Dressrosa.h < 18:
            #narrador "Event not available in this version, please wait for v0.34"

            if Dressrosa.h == 6:
                jump dressrosa_h6

            if Dressrosa.h == 8:
                jump dressrosa_h8

            if Dressrosa.h == 10:
                jump dressrosa_h10

            if Dressrosa.h == 12:
                player "(I have to look for and see how [rebecca.n] is before fighting...)"
                jump m_dr_ac_co_fighters_preparations

            if Dressrosa.h == 13:
                jump dressrosa_h13

            if Dressrosa.h == 15:
                jump dressrosa_h15

            #if Dressrosa.h == 17:
            #    jump dressrosa_h17_if

            elif Dressrosa.h == 16:
                narrador "This event is available in version 0.[version_id_next].\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
                jump m_dr_ac_co_fighters_preparations

            else:
                player "(It's not my turn to fight yet, I might as well kill some time walking around here)"
                player "(I've got time to check out the fighters, when it's my turn, they'll call me)"

                jump m_dr_ac_co_fighters_preparations     

        "Go to Statue" if Dressrosa.h >= 6:
            jump dr_ac_co_statue

        "Back":
            jump dr_ac_colosseum
