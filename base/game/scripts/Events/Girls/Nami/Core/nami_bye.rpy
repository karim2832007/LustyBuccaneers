# Version event: 1
# Version game: 0.14

label nami_bye:
    window hide
    hide nami with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location