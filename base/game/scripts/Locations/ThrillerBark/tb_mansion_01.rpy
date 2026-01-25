# Version event: 3
# Version game: 0.5

label tb_mansion_01():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ game.location = "tb_mansion_01"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_thrillerbark()
    jump m_tb_mansion_01

label m_tb_mansion_01():
    if ThrillerBark.h == 5:
        window hide
        pause 1.2
        window auto
        
        nami "Ancient armor, paintings, and decorations everywhere..."
        nami "The owner must be filthy rich!!!"
        robin "Everything is in perfect condition... Let's stay alert, the owner might still be here..."

        $ ThrillerBark.h = 6

    menu:
        "Advance":
            jump tb_mansion_02

        "Enter the Room" if ThrillerBark.h >= 10:
            jump thriller_bark_dr_room

        "Back":
            jump thriller_bark_mansion
