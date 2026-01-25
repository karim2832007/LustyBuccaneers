# Version event: 3
# Version game: 0.15

label robin_breasts_squeezed:
    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ game.location = "ship_girls_room"
    scene BG locations:
        blur 3
    
    show events robin breastssqueezed robin_breasts_squeezed:
        xalign 0.5
        yalign 1.0

    hide screen screen_black with Dissolve(0.3)
    window auto

    window hide
    pause 0.5

    player "(Hoooly!!)"     
    robin "What bad luck I had! I underestimated you and lost..."
    robin "Is this how you wanted it, Captain?"
    robin "Is it just me, or is it starting to get warm in here?"
    player "Yeeees!!! Soooo hot..."      
    robin "Maybe I have a bit of a fever, I might need you to check me."
    player "Yes, of course! I can help... I'm a professional, maybe I could..." 

    pause 3.0

    robin "What bad luck...."
    robin "I think I've more than fulfilled my debt, Captain."
    robin "What do you think? Perhaps we can continue playing another time..."
    player "(Reallyyyy?!?)" 
    robin "If you think of something else to bet on, let me know, and let's play again!"
    robin "Until next time Captain!!"


    $ robin_lust += 1
    narrador "[robin.n] Lust +1"

    $ ui_interface = True
    $ game.clock.next()
    jump ship_mid
    
