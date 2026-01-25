# Version event: 1
# Version game: 0.12

label robin_check(check_love = 0, check_lust = 0):
    if robin_lust < check_lust or robin_love < check_love:
        narrador "Requires [robin.n] lust greater than [check_lust] and love greater than [check_love]"
        jump robin_refuse

    return