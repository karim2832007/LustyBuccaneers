# Version event: 1
# Version game: 0.12

label hancock_hangout:
    $ hancock_hangout_random = renpy.random.choice(["hancock_hangout_1","hancock_hangout_2","hancock_hangout_3","hancock_hangout_4"])
    
    #$ hancock_hangout_random = "hancock_hangout_3"
    
    call expression hancock_hangout_random from _call_hancock_hangout_random

    jump hancock_bye
