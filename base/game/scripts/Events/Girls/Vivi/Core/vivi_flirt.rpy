# Version event: 1
# Version game: 0.23

label vivi_flirt:
    show vivi c1 shame with dissolve
    narrador "You spend several minutes making sexually suggestive comments..."
    $ vivi_lust += 1
    narrador "[vivi.n] Lust +1"
    
    jump vivi_bye