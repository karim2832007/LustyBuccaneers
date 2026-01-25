# Version event: 1
# Version game: 0.28

label uta_check(check_love = 0, check_lust = 0):
    if uta_lust < check_lust or uta_love < check_love:
        narrador "Requires [uta.n] lust greater than [check_lust] and love greater than [check_love]"
        jump uta_refuse

    return