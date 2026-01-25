# Version event: 3
# Version game: 0.20

default nami_handjob = 0

image movie_nami_handjob slow = MovieFallback(play="movie/nami/handjob/1.webm", image="movie/nami/handjob/img.webp", character="nami")
image movie_nami_handjob fast = MovieFallback(play="movie/nami/handjob/2.webm", image="movie/nami/handjob/img.webp", character="nami")
image movie_nami_handjob cum  = MovieFallback(play="movie/nami/handjob/3.webm", image="movie/nami/handjob/img.webp", character="nami")

label event_nami_handjob:

    if nami_handjob == 0:

        player "[nami.n] how are you? I'm here for you again..."
        nami "Captain! all good! How can I help you?"
        player "I want to enjoy your services again..."
        show nami c1 shame with dissolve
        nami "Hehe! At it again, Captain..."
        player "This time I want you to use your hands... I want something quick..."
        show nami c1 neutral with dissolve
        nami "I'll make you see the stars... But..."
        nami "You know how this world works Captain..."

    else:
        nami "Do you want another session Captain?"
        nami "I'd love to... But you know how this works..."

    menu:
        "40 berries" if berries >= 40:
            call nami_check pass (check_love = 15, check_lust = 15, check_berries = 40) from _nami_check_handjob_40
            show nami happy with dissolve

        "Bargain, 20 berries" if berries >= 20:
            call nami_check pass (check_love = 20, check_lust = 20, check_berries = 20) from _nami_check_handjob_20
            show nami happy with dissolve

        "No payment":
            call nami_check pass (check_love = 25, check_lust = 25, check_berries = 0) from _nami_check_handjob_0
            show nami neutral with dissolve
           
    $ nami_handjob += 1

    pause 0.2
    window hide
    show nami c1_underwear with dissolve
    pause 0.4
    show nami neutral c1_naked with dissolve

    nami "Your dick Captain, show it to me!"
    nami "Today I will stroke it for you okay?"
    nami "I'm gonna squeeze it dry with my hands!"

    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    show movie_nami_handjob slow

    hide screen screen_black with Dissolve(0.8)

    nami "Look at the size of you..."
    nami "Captain's dick is soo amazing..."
    nami "The smell... So obscene and strong..."
    nami "Your dick must be so tired after such a long day of work..."
    nami "I'm going to help you relax..."
    nami "I've been holding myself from having sex for sooooo long"
    nami "With this cock..."
    nami "I don't know how I'm going to do it!!!"

    jump event_nami_handjob_slow

#handjob
label event_nami_handjob_slow:
    window hide
    window auto
    show movie_nami_handjob slow

    pause 3.0
    #dialogos repetitivos

    nami "Good..."    
    nami "I'll make it even more wet and slippery!"
    player "It feels so good that you're jerking me off [nami.n]"
    nami "It feels good when i rub the tip too? ...Does it feel good?"
    nami "I'll focus on the tip for a while!"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_nami_handjob slow
            pause
            jump event_nami_handjob_slow

        "Faster":
            player "Go faster!!"
            jump event_nami_handjob_fast
    

label event_nami_handjob_fast:
    window hide
    window auto
    show movie_nami_handjob fast

    pause 3.0
    #dialogos repetitivos
    
    nami "Your dick is throbbing like crazy, are you close to cum or not?"    
    player "Shit, if you continue like this... I'm gonna cum!!"
    nami "I can go even faster if you want!..."
    nami "Let it aaall out..."     
    nami "But if you defile me with your hot cum, you'll have to pay me more fine?..."
   


    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_nami_handjob_slow

        "Keep going":
            show movie_nami_handjob fast
            pause
            jump event_nami_handjob_fast

        "Cum":
            jump event_nami_handjob_cum


label event_nami_handjob_cum:

    nami "Does it feel good?"
    nami "Come on let it out. Let it all out.. Hurry up and cum!"

    show movie_nami_handjob cum
    
    window hide
    window auto

    pause 1.0

    play sound "cum_01"
    show events nami handjob nami_handjob_cum at vibration  with flash
    hide movie_nami_handjob

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    nami "Woow Captain!... so much of your hot stuff is coming out!"
    nami "Captain's semen is really thick!!"
    nami "I love your dick!!"
    pause 0.2
    nami "Hahaha you let out a lot!!"
    nami "I'll let the whole mess you made here go and I won't charge you extra this time."
    nami "Give me a moment and I'll eat it all Captain!"


    window hide
    window auto
    pause 1.0
    jump event_nami_handjob_end


label event_nami_handjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_nami_handjob
    hide events nami handjob nami_handjob_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show nami happy with dissolve
    
    nami "Why don't we have sex next time Captain?"
    nami "I'll be waiting for you!"

    $ nami_lust += 2
    $ nami_love += 2
    narrador "[nami.n] Lust +2 and Love +2" 

    window hide
    show nami c1_underwear with dissolve
    pause 0.2
    show nami c1 with dissolve

    #jump nami_bye

    window hide
    hide nami with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location