# Version event: 1
# Version game: 0.12

label hancock_flirt:
    show hancock c1 shame with dissolve
    narrador "You spend several minutes making sexually suggestive comments..."
    $ hancock_lust += 1
    narrador "[hancock.n] Lust +1"
    
    jump hancock_bye