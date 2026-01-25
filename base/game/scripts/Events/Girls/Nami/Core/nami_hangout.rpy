# Version event: 1
# Version game: 0.14

label nami_hangout:
    $ nami_hangout_random = renpy.random.choice(["nami_hangout_1","nami_hangout_2","nami_hangout_3"])
    
    #$ nami_hangout_random = "nami_hangout_3"
    
    call expression nami_hangout_random from _call_nami_hangout_random

    jump nami_bye
