# Version event: 1
# Version game: 0.12

label perona_check(check_love = 0, check_lust = 0):
    if perona_lust < check_lust or perona_love < check_love:
        narrador "Requires [perona.n] lust greater than [check_lust] and love greater than [check_love]"
        jump perona_refuse

    return