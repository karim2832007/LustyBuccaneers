# Version event: 3
# Version game: 0.15

label event_robin_room:
    
    robin "Who is looking for me?!?"
    player "[robin.n]? It's me, may I come in?..."
    robin "Yes Captain, give me a second..."
    robin "Please come in!"

    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ game.location = "ship_girls_room"
    scene BG locations:
        blur 3

    show robin c1 with dissolve
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    robin "I'm surprised you actually asked before coming in!... I know how you usually act hehe, What do you need?"


    menu event_robin_room_menu:

        "Play a game":
            if robin_love < 10:
                narrador "Requires [robin.n] love greater than 10"
                jump event_robin_room_menu

            jump start_cards_memory

        "Back":
            $ game.clock.next()
            jump ship_mid
   