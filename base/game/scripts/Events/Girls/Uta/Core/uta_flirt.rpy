# Version event: 1
# Version game: 0.28

label uta_flirt:
    show uta c1 shame with Dissolve(0.2)
    narrador "You spend several minutes making sexually suggestive comments..."
    $ uta_lust += 1
    narrador "[uta.n] Lust +1"
    
    jump uta_bye