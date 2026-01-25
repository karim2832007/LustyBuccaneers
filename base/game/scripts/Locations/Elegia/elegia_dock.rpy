# Version event: 2
# Version game: 0.25

label elegia_dock():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "elegia_dock"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_elegia()
    jump m_elegia_dock

label m_elegia_dock():
    if Elegia.h == 1:
        pause 1.0

        player "Alright, here we are, let's leave the ship here for now!"
        player "Good thinking hiding the sails [robin.n], there might be a lot of World Government people on this island..."
        player "We need to be careful... Let's head into the city!"

        $ Elegia.h = 2

    menu:
        "Go to city":
            jump elegia_city

        "Back":
            jump elegia
