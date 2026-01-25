# Version event: 1
# Version game: 0.14

label nami_check(check_love = 0, check_lust = 0, check_berries = 0):
    if nami_lust < check_lust or nami_love < check_love:
        narrador "Requires [nami.n] lust greater than [check_lust] and love greater than [check_love]"
        jump nami_refuse
        
    if check_berries > 0:
        $ berries -= check_berries
        narrador "-[check_berries] [Berries.n]"

    return