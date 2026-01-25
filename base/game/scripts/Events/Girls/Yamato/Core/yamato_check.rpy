# Version event: 1
# Version game: 0.12

label yamato_check(check_love = 0, check_lust = 0):
    if yamato_lust < check_lust or yamato_love < check_love:
        narrador "Requires [yamato.n] lust greater than [check_lust] and love greater than [check_love]"
        jump yamato_refuse

    return