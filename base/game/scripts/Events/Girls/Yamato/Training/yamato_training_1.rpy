# Version event: 2
# Version game: 0.35

image movie_yamato_training_1 = MovieFallback(play="movie/yamato/training/1.webm", image="movie/yamato/training/1.webp", character="yamato")

label event_yamato_training_1:
    $ _window_hide()
    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show movie_yamato_training_1
    hide screen screen_black with Dissolve(0.8)

    if yamato_training == 0:
        #first time
        pause 1.0

        narrador "The sound of punches and the creaking of weights echoes through the ship's gym."
        narrador "Among the equipment, you see [yamato.n] training intensely, her breathing steady and determined."

        player "(Wow... she hasn't slowed down for a single second...)"
        player "(She's so sexy... even when she's just stretching...)"
        pause 0.5
        yamato "Ah! [player.n]! I didn't hear you come in. Why are you just standing there staring at me without saying anything?"
        player "I was simply admiring your beauty, [yamato.n]."
        yamato "Hahaha, you'll never change!"
        pause 0.5
        yamato "I was just warming up a bit before starting the heavy exercises."
        player "Looks like you take it very seriously... you should teach me your routine sometime."
        yamato "Really? I didn't think you'd be interested in training with me."
        player "Of course I am. Besides... there's no better motivation than doing it by your side."
        yamato "Hahaha, you always know what to say... Alright, let's see if you can keep up with me."
        player "That sounds like a challenge, and challenges don't scare me."
        pause 0.5        
        yamato "Excellent! Then let's make a little game out of it..."
        player "A game?"
        yamato "Yes, a game!"
        yamato "I'll give you a dumbbell, and you'll have to hold it—same as me."
        yamato "But to make it more entertaining for me, I'll use much heavier weight than you."
        yamato "That way, we'll both be training, and whoever drops their dumbbell first loses..."
        yamato "Simple, right?!?"
        player "So I just have to hold it longer than you?"
        yamato "Exactly—but even if you have less weight, I won't make it easy for you!"
        player "Alright, sounds fair... let's begin!"
        yamato "Perfect. I warn you... I don't plan on holding back!"
        player "Just the way I like it, [yamato.n]. Let's see if you can wear me out before the day ends."
        yamato "Hehehe, careful what you wish for, [player.n]... when I train, I don't let anyone quit halfway."

        pause 1.0

    else:
        #second time
        yamato "Back again, [player.n]?!"
        yamato "Are you ready to compete? How about another little game again..."
        player "Alright, let's get started!"


    if yamato_training == 0:
        $ yamato_training = 1

    yamato "Ready?!?"
    yamato "Goooo!!"
    
    $ _window_hide()
    $ black_to_img("minigames training training_run")

    show minigames training training_run at vibration

    $ v_miniGameWeight = MinigameWeight(yamato_duration=15.0, weight=40)
    call screen s_miniGameWeight
    #change code for weight <<<<<<<<<<<<<<<<<<<<<<<


    jump ship_training_room