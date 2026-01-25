# Version event: 2
# Version game: 0.39

label dr_ac_co_store_room():
    $ _window_hide()
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "dr_ac_co_store_room"
    scene BG locations:
        blur 3
    
    if Dressrosa.h >= 18 and not rebecca_crew:
        show rebecca c2 at center   

    hide screen screen_black with Dissolve(0.3)


    $ music_dressrosa()
    jump m_dr_ac_co_store_room

label m_dr_ac_co_store_room():
    if Dressrosa.h == 12:
        jump dressrosa_h12
    elif Dressrosa.h == 14:
        jump dressrosa_h14
    elif Dressrosa.h == 16:
        narrador "This event is available in version 0.[version_id_next].\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
        #jump m_dr_ac_co_store_room
        #jump dressrosa_h16

    menu:
        "Talk to Rebecca" if Dressrosa.h >= 18 and not rebecca_crew:
            narrador "This event is in development, try again in the next version."
            jump m_dr_ac_co_store_room
            #jump rebecca_join_the_crew

        "Back":
            jump dr_ac_co_statue
