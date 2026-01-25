# Version event: 1
# Version game: 0.28

label yamato_bye:
    $ _window_hide()
    hide yamato with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location