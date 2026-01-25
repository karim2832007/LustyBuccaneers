# Version event: 3
# Version game: 0.35

label training_gameover:
    $ _window_hide()
    $ renpy.pause(1.5, hard=True)
    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    scene BG locations:
        blur 3
    hide screen screen_black with Dissolve(0.8)

    #if yamato_training == 0:

    show yamato smile with dissolve:
        xalign 0.5
        yalign 1.0

    narrador "Despite all your effort, you can't hold the weight any longer and it drops to the floor..."

    yamato "Hahaha, I knew it! I WON!"
    yamato "Looks like I'm still the strongest one on this ship!"
    player "Damn, that was really heavy... This is seriously tough..."

    if Strength >= 10 * player_level:
        narrador "You've reached the strength limit for your current level."
    else:
        $ Strength += 1
        narrador "Strength +1"

    $ yamato_love += 1
    narrador "[yamato.n] Love +1"


    yamato "Well, [player.n], we can train again whenever you want."


    $ game.clock.next()
    jump expression game.location
