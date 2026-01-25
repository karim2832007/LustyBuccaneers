# Version event: 1
# Version game: 0.22

default sleep_event = None

label sleep:
    $ game.clock.sleep()

    python:
        if sleep_event:
            if renpy.has_label(sleep_event):
                renpy.call(sleep_event)
            sleep_event = None

    $ RPGPlayer.sleep()

    jump ship_captains_cabin

label sleep_night:
    narrador "It got late, and you preferred to return to your cabin to sleep."
    jump sleep