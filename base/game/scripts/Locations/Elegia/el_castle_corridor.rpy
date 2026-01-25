# Version event: 4
# Version game: 0.28

label el_castle_corridor():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "el_castle_corridor"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_el_castle_corridor

label m_el_castle_corridor():
    if Elegia.h == 5:
        pause 1.0

        show nami with dissolve:
            xalign 0.15
            yalign 1.0

        nami "So many people!! We've already run into hundreds of students..."
        player "(Yes, and all kinds of young beauties!! It was totally worth crossing this long path!)"

        show robin with dissolve:
            xalign 0.85
            yalign 1.0
        
        robin "Yes... And even many reporters and people who clearly belong to high classes..."
        nami "We must be careful, maybe the best thing would be..."
        player "Wait a second... Don't you hear that?... What is that?"
        nami "What is it, Captain? There are sounds coming from everywhere!"
        player "What is that singing?!?"
        player "Do you hear that voice? It's coming from here! Follow me!"

        $ Elegia.h = 6
    
    menu:
        "Follow the voice" if Elegia.h < 7:
            jump el_castle_auditorium

        "Enter the Auditorium" if Elegia.h >= 15 and not uta_crew: 
            jump el_castle_auditorium

        "Go to the Room":
            if Elegia.h == 7:
                robin "According to the students we passed earlier, this should be the principal's office... The king here..."
                nami "But they told us to talk to his secretary first..."
                nami "We shouldn't just barge in... Right, Captain?"
                player "There's no time to waste... This is an emergency situation..."
                player "(I can't let that guy take such a beauty just like that!)"
                yamato "That's the spirit, Captain! If this so-called principal or king has a problem, leave him to me!"
                player "Let's go in!"
                jump el_castle_room

            elif Elegia.h > 7:
                jump el_castle_room

            else:
                narrador "The voice doesn't come from this room"
                jump m_el_castle_corridor

        "Back":
            jump elegia_castle
