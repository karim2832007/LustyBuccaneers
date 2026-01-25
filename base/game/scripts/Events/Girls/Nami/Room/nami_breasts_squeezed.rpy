# Version event: 2
# Version game: 0.14

label nami_breasts_squeezed:
    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ game.location = "ship_girls_room"
    scene BG locations:
        blur 3
    
    show events nami breastssqueezed nami_breasts_squeezed:
        xalign 0.5
        yalign 1.0

    hide screen screen_black with Dissolve(0.3)
    window auto

    window hide
    pause 0.5

    player "(Damn!! This is sooo incredible!!)"     
    nami "A debt is a debt..."
    nami "Is this how you wanted it, Captain?"
    nami "What do you think, am I doing it well?"
    player "Incredibly well, yesyesyesyes!!!"      
    nami "Do you like it when I press my breasts with my hands, Captain?!"
    nami "Alright... I'll let you watch me like this for a few seconds!"

    pause 3.0

    nami "I think that's enough... Consider yourself lucky for seeing this!"
    nami "If you think of something else to bet on, let me know, and let's play again!"
    nami "Until next time!!"

    $ nami_lust += 1
    narrador "[nami.n] Lust +1"

    $ ui_interface = True
    $ game.clock.next()
    jump ship_mid
    
