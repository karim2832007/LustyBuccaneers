# Version event: 3
# Version game: 0.24

default yuba_bar = 0
default dance_berries = 50
default risk_incident = False

label ar_y_bar():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True        
    $ game.location = "ar_y_bar"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    if yuba_bar == 0:
        jump m_ar_y_bar_repair
    else:
        jump m_ar_y_bar

label m_ar_y_bar_repair():
    menu:
        "Repair the bar" if not game.clock.night:
            menu:
                narrador "Requires: 20 wood, 10 beer and 200 [Berries.n]"
                "Yes":
                    if wood >= 20 and beer >= 10 and berries >= 200:
                        $ wood -= 20
                        $ beer -= 10
                        $ berries -= 200

                        play sound "repair"
                        
                        window hide
                        window auto

                        show screen screen_black with Dissolve(0.6)
                        $ yuba_bar = 1
                        $ game.clock.next()
                        hide screen screen_black with Dissolve(0.3)


                        pause 0.5
                        show toto at center with dissolve
                        
                        toto "[player.n]! We did it!"
                        toto "Just look at this place, it's a paradise!"

                        player "It turned out better than I expected. If this oasis was missing something, it was a bar like this!"

                        toto "And to think that not long ago it was just sand and dreams... but now we have a real bar!"
                        toto "If we get a good dancer, this place will be packed..."
                        toto "And this will only be the first step, young man..."
                        toto "Whenever you want, you can stop by and drink at half price!"
                        show toto pervert with Dissolve(0.2)
                        toto "And if any girl wants to put on a show... well, you know where the stage is. Hehehe."

                        player "Looks like this oasis is going to be livelier than I imagined!"

                        toto "Do you know someone who can move their hips well?"

                        player "I have a few ideas..."

                        hide toto with dissolve
                        jump m_ar_y_bar 

                    else:
                        narrador "Insufficient resources"
                "No":
                    pass
            
            jump m_ar_y_bar_repair

        "Back":
            jump ar_yuba_oasis


label m_ar_y_bar():
    menu:
        "Drinks" if not game.clock.night:
            jump ar_y_bar_buy

        "Dancer job" if not game.clock.night:
            menu m_ar_y_bar_dance:
                "[nami.n]":
                    if not nami_c2:
                        player "([nami.n] doesn't have the right outfit for the job)"
                        player "([toto.n] mentioned that someone in Nanohana might sell the right clothes, I should take a look)"
                        jump m_ar_y_bar_dance

                    menu m_ar_y_bar_dance_nami:
                        "Sensual dance":
                            call dance_event("nami_dance_1", 50, 100, 0) from _call_nami_dance_1
                            #jump nami_dance_1

                        "Erotic Dance":
                            if yuba_bar_nami > 0:
                                if nami_lust > 15:
                                    call dance_event("nami_dance_2", 100, 200, 0) from _call_nami_dance_2
                                else:
                                    narrador "Requires [nami.n] lust greater than 15"
                            else:
                                narrador "[nami.n] wouldn't be willing to do this so quickly. It's better to move forward with something more relaxed first"

                        "Hot Dance":
                            narrador "This event is in development, try again in the next version."

                        #"Sexual dance":
                        
                        "Back":
                            jump m_ar_y_bar_dance

                    jump m_ar_y_bar_dance_nami

                "Back":
                    jump m_ar_y_bar

        "Back":
            jump ar_yuba_oasis


label dance_event(label_dance, min_berries, max_berries, risk_of_incident):

    $ dance_berries = renpy.random.randint(min_berries, max_berries)
    $ risk_incident = renpy.random.randint(0, 100) < risk_of_incident

    menu:
        narrador "Do you want to continue with this dance?\nMinimum earnings: [min_berries] - Maximum earnings: [max_berries]\n Risk of incident: [risk_of_incident]\%"
        "Yes":
            call expression label_dance from _call_label_dance
        "No":
            pass

    return


label ar_y_bar_buy():
    $ ui_berries = True

    menu:
        "Beer{space=140}-20 Berries":
            if berries >= 20:
                $ beer += 1
                $ berries -= 20
                narrador "-20 [Berries.n] | +1 Beer"
            else:
                player "I have [berries] [Berries.n], but I need 20."

        "Back":
            $ ui_berries = False
            jump m_ar_y_bar

    jump ar_y_bar_buy