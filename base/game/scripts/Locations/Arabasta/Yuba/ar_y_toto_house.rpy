# Version event: 2
# Version game: 0.24

label ar_y_toto_house():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True        
    $ game.location = "ar_y_toto_house"
    scene BG locations:
        blur 3
    
    show toto at center
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_y_toto_house


label m_ar_y_toto_house():
    menu:
        "Talk":
            if Arabasta.h < 14:
                player "(I don't have time to talk to [toto.n] right now... Defeating [crocodile.n] has to be my priority!)"            

            elif Toto.h == 0:
                jump ar_y_toto_h1

            else:
                player "(I have nothing to say to [toto.n])"

            jump m_ar_y_toto_house

        "Back":
            pass

    #hide toto
    jump ar_yuba_oasis

