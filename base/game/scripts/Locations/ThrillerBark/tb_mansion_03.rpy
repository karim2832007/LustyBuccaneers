# Version event: 4
# Version game: 0.5

label tb_mansion_03():
    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ game.location = "tb_mansion_03"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_thrillerbark()
    jump m_tb_mansion_03

label m_tb_mansion_03():
    if ThrillerBark.h == 7:
        window hide
        pause 1.2
        window auto

        show nami at center with dissolve

        nami "This place is gigantic... It seems endless..."

        show nami:
            yalign 1.0
            xalign 0.5
            linear 0.4 xalign 0.8

        pause 0.3

        show yamato with dissolve:
            yalign 1.0
            xalign 0.2

        yamato "Captain, look over there, someone is approaching!"

        hide nami 
        hide yamato
        with dissolve

        $ ThrillerBark.h = 8

    if ThrillerBark.h == 8:
        window hide
        show expression enemy_ryuma.image with Dissolve(1.0):
            xalign 0.5
            yalign 0.5

        pause 0.8
        window auto

        robin "And it doesn't look friendly... It's some kind of... samurai?!?"
        yamato "Yes!... He's carrying a katana!... unlike the ones we've encountered here before, he could be dangerous!"

        unknown "You are not welcome here... I'm surprised you have come this far!"
        unknown "But this is where it ends. You've seen too much! This will be your end."

        call fight_start pass (enemy_pass = enemy_ryuma) from _fight_thrillerbark_h8

        hide expression enemy_ryuma.image with Dissolve(0.8)
        
        if not fight_return:
            jump tb_mansion_02

        $ music_thrillerbark()

        show nami at center with dissolve

        nami "For a moment, I thought we wouldn't make it out of this alive!"

        show nami:
            yalign 1.0
            linear 0.4 xalign 0.15

        pause 0.3

        show robin with dissolve:
            yalign 1.0
            xalign 0.85

        robin "Now we can uncover the mystery at the end of this room..."
        robin "It seems we're not far from the final chamber..."
        $ ThrillerBark.h = 9

    menu:
        "Advance":
            jump perona_room

        "Back":
            jump tb_mansion_02
