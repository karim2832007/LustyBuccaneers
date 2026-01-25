# Version event: 1
# Version game: 0.12

label hancock_bye:
    window hide
    hide hancock with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location