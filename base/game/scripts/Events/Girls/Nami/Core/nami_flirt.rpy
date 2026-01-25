# Version event: 1
# Version game: 0.14

label nami_flirt:
    show nami c1 shame with dissolve
    narrador "You spend several minutes making sexually suggestive comments..."
    $ nami_lust += 1
    narrador "[nami.n] Lust +1"
    
    jump nami_bye