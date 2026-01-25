# Version event: 1
# Version game: 0.28

label uta_bye:
    window hide
    hide uta with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location