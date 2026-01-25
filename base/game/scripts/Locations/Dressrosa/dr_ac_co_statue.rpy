# Version event: 2
# Version game: 0.39

#Fighters' Preparations Room
label dr_ac_co_statue():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "dr_ac_co_statue"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto


    $ music_dressrosa()
    jump m_dr_ac_co_statue

label m_dr_ac_co_statue():

    if Dressrosa.h == 7:
        jump dressrosa_h7

    elif Dressrosa.h == 9:
        jump dressrosa_h9

    elif Dressrosa.h == 11:
        jump dressrosa_h11

    menu:
        "Go to Store Room" if Dressrosa.h >= 12:
            #if Dressrosa.h == 16:
            #    narrador "Event not available in this version, please wait for v0.[version_id_next]"
            #    jump m_dr_ac_co_statue

            jump dr_ac_co_store_room

        "Back":
            jump dr_ac_co_fighters_preparations
