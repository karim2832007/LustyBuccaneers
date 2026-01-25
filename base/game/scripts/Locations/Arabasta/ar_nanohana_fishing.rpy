# Version event: 2
# Version game: 0.20

label ar_nanohana_coast():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True        
    $ game.location = "ar_nanohana_coast"
    $ arabasta_location = "Nanohana"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ music_arabasta()

    menu m_ar_nanohana_coast:
        "Fishing" if not game.clock.night:
            if not tool_rod:
                narrador "Fishing rod required"
                jump m_ar_nanohana_coast

            jump ar_nanohana_coast_fishing
        
        "Back":
            jump ar_nanohana

label ar_nanohana_coast_fishing():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ ui_interface = False
    $ game.location = "ar_nanohana_coast_fishing"
    scene BG locations
    #    blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_time_day()

    $ _miniGameFishing = MinigameFishing();
    call screen s_miniGameFishing
    jump ar_nanohana_coast


label m_ar_nanohana_coast_fishing():

    $ game.clock.next()
    $ ui_interface = True

    if game.clock.night:
        player "It got late. I should return to my cabin."
        jump ar_nanohana_coast
    
    menu:
        "Continue":
            $ ui_interface = False
            $ _miniGameFishing = MinigameFishing();
            call screen s_miniGameFishing
            jump ar_nanohana_coast
        "Back":
            #$ ui_interface = True
            jump ar_nanohana_coast


label ar_nanohana_coast_fishing_win:
    $ food += 5
    narrador "+5 Food"
    
    jump m_ar_nanohana_coast_fishing


label ar_nanohana_coast_fishing_gameover:
    narrador "Oh no, it got loose!"

    jump m_ar_nanohana_coast_fishing