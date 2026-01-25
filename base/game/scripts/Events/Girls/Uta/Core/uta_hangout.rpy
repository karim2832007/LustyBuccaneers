# Version event: 1
# Version game: 0.28

label uta_hangout:
    $ uta_hangout_random = renpy.random.choice(["uta_hangout_1","uta_hangout_2","uta_hangout_3","uta_hangout_4","uta_hangout_5","uta_hangout_6"])
    
    #$ uta_hangout_random = "uta_hangout_3"
    
    call expression uta_hangout_random from _call_uta_hangout_random

    jump uta_bye
