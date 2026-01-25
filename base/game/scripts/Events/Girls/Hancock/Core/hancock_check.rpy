# Version event: 1
# Version game: 0.12

label hancock_check(check_love = 0, check_lust = 0):
    if hancock_lust < check_lust or hancock_love < check_love:
        narrador "Requires [hancock.n] lust greater than [check_lust] and love greater than [check_love]"
        jump hancock_refuse

    return