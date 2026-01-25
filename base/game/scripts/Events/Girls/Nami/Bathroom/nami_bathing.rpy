# Version event: 3
# Version game: 0.38

image movie_nami_bathing = MovieFallback(play="movie/nami/bathing/1.webm", image="movie/nami/bathing/img.webp", character="nami")

label nami_bathing:
    $ _window_hide()
    show screen screen_black with Dissolve(0.6)
    $ ui_interface = False
    show movie_nami_bathing:
        xalign 0.5
        yalign 1.0
    
    show layer_nami_bathing_censored_1
    show layer_nami_bathing_censored_2 at v_low_move 
    show layer_nami_bathing_censored_3 at v_low_move 

    hide screen screen_black with Dissolve(0.3)
    pause 2.0

    #if renpy.random.choice([True, False]):

    player "(This is incredible...)"
    player "(To think I'd get a chance like this!)"
    player "(This is the reason why the bathroom is one of the main rooms on this ship!)"
    pause 0.5
    player "(Look at the curves on this goddess...)"
    player "(But... there's still a lot of steam anyway!!)"
    player "(I can't really see much right now... This steam leaves so much to the imagination!!)"
    player "(And the foam too!! It almost feels on purpose...)"
    pause 0.5
    player "(Maybe if I wait a bit, the steam will go down... But the risk will keep getting higher!)"


    $ _window_hide()
    menu:
        "Continue peeking":
            if renpy.random.choice([True, False, False, False, False]):
                jump nami_bathing_detected

            hide layer_nami_bathing_censored_3 with Dissolve(0.8)
            player "(Much better...)"
            player "(Waiting works!! It's just a matter of time before the good part comes... But...)"
            player "(If I keep waiting and she discovers me, I'll die!)"
            player "(What am I supposed to do?!... Is the risk worth it?)"

            menu:
                "Continue peeking":
                    if renpy.random.choice([True, False, False, False]):
                        jump nami_bathing_detected

                    hide layer_nami_bathing_censored_2 with Dissolve(0.8)
                    player "(Better, much better... This is incredible...)"
                    player "(I'm so far away, and yet so close...)"
                    player "(Just a little more and I'll get the big reward!!!)"
                    player "(What am I supposed to do?!... At this point, maybe...)"

                    menu:
                        "Continue peeking":
                            if renpy.random.choice([True, False, False]):
                                jump nami_bathing_detected
                                
                            hide layer_nami_bathing_censored_1 with Dissolve(0.8)
                            pause 1.0
                            player "(Jackpot!!!!)"
                            player "(Now I can see her clearly...)"
                            player "(She's so beautiful!!)"
                            player "(Every second of waiting was worth it...)"
                            player "(It's something very few get to see... Something unique... Just for me...)"
                            player "(I could stay here forever!)"
                            player "(I have to store these images in my mind!)"  
                            pause 0.5
                            player "(How lucky I am!)"                              

                        "Leave":
                            pass

                "Leave":
                    pass

        "Leave":
            pass

    player "I'd better leave before she discovers me... I've had enough for today!"
    $ game.clock.next()
    jump ship_mid

label nami_bathing_detected:
    $ _window_hide()
    show screen screen_black with Dissolve(0.6)

    $ game.location = "ship_bathroom_tub"
    scene BG locations:
        blur 3

    show nami c1_naked serious at center

    hide screen screen_black with Dissolve(0.3)
    
    if nami_love >= 20:

        nami "[player.n], what are you doing spying on me?"
        nami "You shouldn't be doing this in secret..."
        nami "If you want to see me naked, you just have to ask and we could reach an agreement..."
        nami "You know very well that I'm willing to give you... EVERYTHING... for the right price, of course..."
        pause 0.5
        nami "Hahaha, come on, get out of here before I have to charge you for seeing me like this"


    else:
        show nami annoyed with Dissolve(0.3)
        pause 0.5

        nami "What are you doing there!! How long have you been watching?!?"
        nami "You're a shameless pervert... The girls will hear about this!!"
        nami "You'd better leave before I catch you... Or else... You'll see!"
        nami "Get out of here right now!"

        # sound: door slam

        $ _window_hide()
        show screen screen_black with Dissolve(0.6)
        $ game.location = "ship_bathroom"
        scene BG locations:
            blur 3
        hide screen screen_black with Dissolve(0.3)

        $ nami_love -= 1
        narrador "[nami.n] Love -1"


    $ game.clock.next()
    jump ship_mid
    
