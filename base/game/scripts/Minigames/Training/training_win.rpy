# Version event: 3
# Version game: 0.35

label training_win:
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

    yamato "Phew... you're really good..."
    yamato "You beat me!"
    yamato "You're really strong, you've got incredible endurance..."

    if v_miniGameWeight.weight == 40:
        yamato "Looks like we can take it up a notch, push ourselves harder... I'm sure you can handle more weight."
        yamato "Next time, I'll give you even more to lift. You still have a long way to catch up to me, but we can start adding a bit more..."

    if Strength >= 10 * player_level:
        narrador "You've reached the strength limit for your current level."
    else:
        $ Strength += 2
        narrador "Strength +2"

    $ yamato_love += 1
    narrador "[yamato.n] Love +1"


    yamato "Well, [player.n], we can train again whenever you want!"
    yamato "Come see me, I'll be waiting for you!"

    $ game.clock.next()
    jump expression game.location
