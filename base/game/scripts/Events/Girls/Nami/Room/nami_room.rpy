# Version event: 2
# Version game: 0.14

label event_nami_room:
    
    nami "Who is it?!?"
    player "[nami.n]? It's me, may I come in?..."
    nami "Yes, give me a second..."
    nami "You may enter, Captain!"

    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ game.location = "ship_girls_room"
    scene BG locations:
        blur 3

    show nami c1 with dissolve
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    nami "I'm surprised you actually asked before coming in!... What do you need?"


    menu event_nami_room_menu:

        #"Flirt":
        #    jump nami_flirt

        "Play a game":
            if nami_love < 10:
                narrador "Requires [nami.n] love greater than 10"
                jump event_nami_room_menu

            jump start_cards

        "Back":
            $ game.clock.next()
            jump ship_mid
   