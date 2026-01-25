# Version event: 2
# Version game: 0.23

label ar_alubarna_palace_room():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True
    $ game.location = "ar_alubarna_palace_room"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_alubarna_palace_room

label m_ar_alubarna_palace_room():
    if not vivi_crew:

        show vivi neutral at center with dissolve

        vivi "Hello [player.n], were you looking for me?"
        vivi "Could it be that you want me to join your crew?"

        menu:
            "Do you want [vivi.n] to be part of the crew?"
            "Yes":
                $ vivi_crew = True
                player "Yes, come with us, [vivi.n], you were already part of the crew before you even said it!!"
                player "Everyone will be happy to have you in the crew, especially me!"
                vivi "Thank you for everything, [player.n]"

            "I need to think about it":
                player "I need to think about it"
                vivi "I understand, if you change your mind, I'll be here waiting."
    
    
    menu:

        "Back":
            jump ar_alubarna_palace

