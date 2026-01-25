# Version event: 2
# Version game: 0.23

label vivi_hangout:
    $ vivi_hangout_random = renpy.random.choice(["vivi_hangout_1","vivi_hangout_2","vivi_hangout_3","vivi_hangout_4","vivi_hangout_5","vivi_hangout_6"])
    
    #$ vivi_hangout_random = "vivi_hangout_3"
    
    call expression vivi_hangout_random from _call_vivi_hangout_random

    jump vivi_bye
