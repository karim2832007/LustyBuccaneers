# Version event: 2
# Version game: 0.18

default yamato_handjob = 0

image movie_yamato_handjob slow = MovieFallback(play="movie/yamato/handjob/1.webm", image="movie/yamato/handjob/img.webp", character="yamato")
image movie_yamato_handjob fast = MovieFallback(play="movie/yamato/handjob/2.webm", image="movie/yamato/handjob/img.webp", character="yamato")
image movie_yamato_handjob cum  = MovieFallback(play="movie/yamato/handjob/3.webm", image="movie/yamato/handjob/img.webp", character="yamato")

label event_yamato_handjob:

    if yamato_handjob == 0:
        player "[yamato.n] I'm going to steal some of your time again!"
        player "What do you think about training the arms today?!"
        yamato "Ohhh that's new, I know exactly what exercise we can do!"
        player "This one in particular, I'm not sure if you know it, but with me it's going to be different!"
        show yamato c1 happy with dissolve
        yamato "Hahaha, I see where this is going!... I love those kinds of exercises, But i don't know..."

    else:
        yamato "Do you want to repeat, Captain?"
        yamato "I've been waiting for you...I need a new session of arms right now!"

    call lewd_yamato_check pass (check_love = 20, check_lust = 20) from _yamato_check_handjob
    show yamato neutral with dissolve
           
    $ yamato_handjob += 1

    pause 1.0
    window hide
    show yamato neutral c1_naked with dissolve

    yamato "Your dick Captain, show it to me!"
    yamato "Today I will stroke it for you okay?"

    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    show movie_yamato_handjob slow

    hide screen screen_black with Dissolve(0.8)

    yamato "My,oh, my... It's so lively..."
    yamato "Captain's dick is soo amazing..."
    yamato "The smell... So obscene and strong..."
    yamato "Your dick reeks of smegma, I love it!"
    yamato "I've been holding myself from having sex for sooooo long"
    yamato "With this cock..."
    yamato "I don't know how I'm going to do it!!!"

    jump event_yamato_handjob_slow

#handjob
label event_yamato_handjob_slow:
    window hide
    window auto
    show movie_yamato_handjob slow

    pause 3.0
    #dialogos repetitivos

    yamato "Good..."    
    yamato "I'll make it even more wet and slippery!"
    player "It feels so good that you're jerking me off [yamato.n]"
    yamato "It feels good when i rub the tip too? ...Does it feel good?"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_yamato_handjob slow
            pause
            jump event_yamato_handjob_slow

        "Faster":
            player "Go faster!!"
            jump event_yamato_handjob_fast
    

label event_yamato_handjob_fast:
    window hide
    window auto
    show movie_yamato_handjob fast

    pause 3.0
    #dialogos repetitivos
    
    player "Fuckk!!"
    yamato "I can go even faster if you want!..."   
    yamato "Your dick is throbbing like crazy, are you close to cum or not?"

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_yamato_handjob_slow

        "Keep going":
            show movie_yamato_handjob fast
            pause
            jump event_yamato_handjob_fast

        "Cum":
            jump event_yamato_handjob_cum


label event_yamato_handjob_cum:

    yamato "Does it feel good?"
    yamato "Come on let it out. Let it all out.. Hurry up and cum!"


    show movie_yamato_handjob cum
    
    window hide
    window auto

    pause 1.0

    play sound "cum_01"
    show events yamato handjob yamato_handjob_cum at vibration  with flash
    hide movie_yamato_handjob

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    yamato "Wow...captain's semen is really thick!!"
    yamato "I love your dick Captain!!"
    pause 0.2
    yamato "Hahaha you let out a lot!!"
    yamato "Give me a moment and I'll eat it all Captain!"
    yamato "Now that I have my proteins, I can continue training peacefully!"


    window hide
    window auto
    pause 1.0
    jump event_yamato_handjob_end


label event_yamato_handjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_yamato_handjob
    hide events yamato handjob yamato_handjob_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show yamato happy with dissolve
    
    yamato "Why don't we have sex next time Captain?"
    yamato "I'll be waiting for you!"

    $ yamato_lust += 2
    $ yamato_love += 2
    narrador "[yamato.n] Lust +2 and Love +2" 

    window hide
    show yamato c1_underwear with dissolve
    pause 0.2
    show yamato c1 with dissolve

    #jump yamato_bye

    window hide
    hide yamato with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location