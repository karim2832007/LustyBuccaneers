# Version event: 4
# Version game: 0.5

label thriller_bark_entrance():
    window hide
    show screen screen_black with Dissolve(0.6)

    
    $ game.location = "thriller_bark_entrance"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_thrillerbark()
    jump m_thriller_bark_entrance

label m_thriller_bark_entrance():
    if ThrillerBark.h == 1:
        show nami at center with dissolve
        nami "What is this place? It's horrible..."
        hide nami with dissolve

        window hide
        pause 1.2
        window auto

        show yamato:
            yalign 1.0
            xalign 0.5
        
        yamato "It smells like adventure!!!"

        show yamato with dissolve:
            yalign 1.0
            xalign 0.5

        show yamato:
            linear 0.4 xalign 0.15

        pause 0.4

        show robin with dissolve:
            yalign 1.0
            xalign 0.5

        robin "What a grim place... I don't entirely dislike it..."

        show robin:
            linear 0.4 xalign 0.85

        pause 0.4

        show nami with dissolve:
            yalign 1.0
            xalign 0.5

        nami "How can you say you don't dislike it?!?"

        robin "It's a narrow and quite dark corridor... Filled with bones of different animals, some human... Many seem to be recent..."

        nami "Exactly because of that!! How can you like a place like this and say all that so calmly!!"
        nami "I'm not leaving your side, Captain!!"

        hide nami with dissolve


        $ ThrillerBark.h = 2

    if ThrillerBark.h == 2:
        # sonido rama o hueso pisado rompiendoce

        show robin:
            xalign 0.85
            yalign 1.0
            linear 0.4 xalign 0.5

        pause 0.4

        robin "Mnmnm... What was that sound?..."

        show yamato:
            xalign 0.15
            yalign 1.0
            linear 0.4 xalign 0.5

        hide robin with Dissolve(0.3)

        pause 0.1

        yamato "Stay alert!! Something's coming!"

        hide yamato with dissolve

        window hide
        show expression enemy_cerberus.image with Dissolve(1.0):
            xalign 0.5
            yalign 0.5
        pause 0.8
        window auto

        nami "Ahhhhh what is that?!?!"

        call fight_start pass (enemy_pass = enemy_cerberus) from _fight_thrillerbark_h2
        
        hide expression enemy_cerberus.image with Dissolve(0.8)

        if not fight_return:
            jump thriller_bark

        $ music_thrillerbark()
        yamato "Excellent, Captain! That dog didn't stand a chance against you, you didn't leave us any fun!"
        $ ThrillerBark.h = 3

    menu:
        "Advance":
            jump thriller_bark_mid

        "Back":
            jump thriller_bark
