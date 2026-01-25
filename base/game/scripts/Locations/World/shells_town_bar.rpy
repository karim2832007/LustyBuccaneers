# Version event: 6
# Version game: 0.3

label shells_town_bar():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ game.location = "shells_town_bar"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_time_day()
    call m_shells_town_bar from _call_shells_town_bar

label m_shells_town_bar():
    if Haki.h == 0:
        jump haki_h1

    menu:
        "Talk to Rayleigh":
            if Haki.h == 1:
                jump haki_h2
                
            elif Haki.h == 2 or Haki.h == 3:
                jump haki_h3

            elif Haki.h == 4:
                jump haki_h5

            elif Haki.h == 5:
                jump haki_h6

            elif Haki.h >= 6:
                narrador "This event is available in version 0.[version_id_next].\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
                jump m_shells_town_bar
                #jump haki_h7

            narrador "This event is in development, try again in the next version."
            jump m_shells_town_bar

        "Back":
            jump shells_town
