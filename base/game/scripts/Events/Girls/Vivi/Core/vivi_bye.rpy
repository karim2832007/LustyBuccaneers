# Version event: 1
# Version game: 0.23

label vivi_bye:
    window hide
    hide vivi with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location