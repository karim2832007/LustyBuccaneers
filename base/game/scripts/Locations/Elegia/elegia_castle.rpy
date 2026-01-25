# Version event: 2
# Version game: 0.25

label elegia_castle():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "elegia_castle"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_elegia_castle

label m_elegia_castle():
    if Elegia.h == 4:
        pause 1.0

        player "(Now this is more like it!!! I can hear thousands of voices in the distance)"
        nami "Wow this is incredible!! Everything is so well maintained..."
        robin "This castle has a really impressive architectural style!"
        yamato "It sounds like there are thousands of voices coming from its outer gardens and from inside..."
        player "That's right [yamato.n]... On the left there seems to be a slightly hidden path, let's enter through there!"
        nami "Alright! Remember to keep a low profile, Captain..."

        $ Elegia.h = 5

    menu:
        "Enter the castle":
            jump el_castle_corridor

        "Back":
            jump elegia_road
