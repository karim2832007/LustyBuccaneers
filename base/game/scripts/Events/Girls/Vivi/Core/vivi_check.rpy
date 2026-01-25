# Version event: 1
# Version game: 0.23

label vivi_check(check_love = 0, check_lust = 0):
    if vivi_lust < check_lust or vivi_love < check_love:
        narrador "Requires [vivi.n] lust greater than [check_lust] and love greater than [check_love]"
        jump vivi_refuse

    return