# Version event: 1
# Version game: 0.3

label ship_fishing():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ ui_interface = False
    $ game.location = "ship_fishing"
    scene BG locations
    #    blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_time_day()

    $ _miniGameFishing = MinigameFishing();
    call screen s_miniGameFishing
    jump ship_mid


label m_ship_fishing():

    $ game.clock.next()
    $ ui_interface = True

    if game.clock.night:
        narrador "It got late, and you preferred to return to your cabin."
        jump ship_captains_cabin
    
    menu:
        "Continue":
            $ ui_interface = False
            $ _miniGameFishing = MinigameFishing();
            call screen s_miniGameFishing
            jump ship_mid
        "Back":
            #$ ui_interface = True
            jump ship_mid


label ship_fishing_win:
    $ food += 5
    narrador "+5 Food"
    
    jump m_ship_fishing


label ship_fishing_gameover:
    narrador "Oh no, it got loose!"

    jump m_ship_fishing