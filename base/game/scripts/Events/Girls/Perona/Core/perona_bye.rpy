# Version event: 1
# Version game: 0.14

label perona_bye:
    window hide
    hide perona with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location