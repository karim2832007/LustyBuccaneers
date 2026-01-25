# Version event: 2
# Version game: 0.28

label el_castle_auditorium():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "el_castle_auditorium"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_el_castle_auditorium

label m_el_castle_auditorium():
    if Elegia.h == 6:
        jump elegia_h6

    elif Elegia.h >= 15 and not uta_crew:
        show uta c1 at center with dissolve

        uta "Hi [player.n], I'm glad to see you!"
        uta "I've been waiting for you all this time..."
        uta "I hope this time you've made up your mind... I'm eager to set sail with you!"
        uta "What do you say?!?"

        menu m_uta_crew:
            "Do you want [uta.n] to be part of the crew?"
            "Yes":
                $ uta_crew = True
                player "I like that attitude!"
                player "This time I've got everything ready! It's time to set sail!"
                player "Let's achieve everything we set out to do together!"
                show uta happy at center with dissolve
                uta "Yessssss!!! We're finally going to sea, I'm so happy!"
                uta "Thank you [player.n]! I promise you won't regret this decision!"

                window hide
                window auto
                hide uta with dissolve

            "I'm not sure yet":
                player "I'm sorry, I know you're eager but I don't have everything ready yet..."
                player "I came to check if you're doing well!... Be patient, we'll sail out in due time!"
                uta "I understand, I know you have to prepare and consider several things. I'll keep waiting here until then!"

    menu:
        "[uta.n]" if Elegia.h >= 15 and not uta_crew:
            jump m_uta_crew

        "Back":
            jump el_castle_corridor
