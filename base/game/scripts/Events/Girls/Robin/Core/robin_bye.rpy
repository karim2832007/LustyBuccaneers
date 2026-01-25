# Version event: 1
# Version game: 0.12

label robin_bye:
    window hide
    hide robin with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location