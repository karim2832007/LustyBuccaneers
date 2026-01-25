# Version event: 2
# Version game: 0.25

label elegia():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "elegia"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_elegia()
    jump m_elegia

label m_elegia():
    if Elegia.h == 0:
        pause 1.0

        nami "We've arrived, Captain! The island is in sight!"
        robin "Elegia, the Island of Music... What a beauty during the night..."
        nami "Yes, it's incredible, like something out of a fairy tale..."
        robin "What mysteries will this beautiful island be hiding, I'm so eager to discover them!"
        robin "Great castles, huge structures... A beautiful city that holds many architectural and cultural treasures!"

        player "(And most important of all!... Beautiful women!)"
        player "Alright!, [nami.n] let's get closer to the coast, we'll make it by sunrise."

        $ Elegia.h = 1

    menu:
        "Go to coast":
            jump elegia_dock

        "Back":
            jump ship_mid
