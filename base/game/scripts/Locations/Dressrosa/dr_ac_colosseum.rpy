# Version event: 4
# Version game: 0.34

label dr_ac_colosseum():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "dr_ac_colosseum"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto


    $ music_dressrosa()
    jump m_dr_ac_colosseum

label m_dr_ac_colosseum():
    if Dressrosa.h == 2:
        pause 1.0

        player "Here we are!!! We finally made it hahaha!!"  
        player "This is the Corrida Colosseum!!"  

        show nami with dissolve:  
            xalign 0.20  
            yalign 1.0  

        show yamato with dissolve:  
            xalign 0.80  
            yalign 1.0  

        play ambient "ring" fadein 1.0

        nami "Amazing!! Listen to the crowd... they're so excited!"  
        nami "Even though we're outside, it feels like we're right in there!!"  
        yamato "What kind of competition will it be!?!"  
        yamato "What an atmosphere!! It even makes me want to sign up!"  
        player "Really, [yamato.n]?!? Not surprising, this atmosphere is incredible!!!"  
        nami "There, Captain, quick, to the reception! We need to sign him up right away, I just heard there are barely any spots left."  
        player "Let's go!! We can't miss out!"
        
        stop ambient
        hide nami with dissolve
        hide yamato with dissolve    

        $ Dressrosa.h = 3

    if Dressrosa.h == 4:
        jump dressrosa_h4

    menu:
        "Go to Reception" if Dressrosa.h == 3:
            jump dressrosa_h3

        "Enter the Colosseum" if Dressrosa.h > 4:
            #narrador "Event not available in this version, please wait for v0.33"
            #jump m_dr_ac_colosseum
            jump dr_ac_co_fighters_preparations
            #Fighters' Preparations Room

        "Back":
            jump dr_acacia
