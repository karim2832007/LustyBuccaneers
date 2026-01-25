# Version event: 1
# Version game: 0.35

default yamato_training = 0

label event_yamato_training:

    if yamato_training == 0:
        jump event_yamato_training_1
    

    jump event_yamato_training_1
