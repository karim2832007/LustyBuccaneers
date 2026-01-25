# Version event: 4
# Version game: 0.31

default robin_doggystyle = 0

image movie_robin_doggystyle slow = MovieFallback(play="movie/robin/doggystyle/1.webm", image="movie/robin/doggystyle/img.webp", character="robin")
image movie_robin_doggystyle fast = MovieFallback(play="movie/robin/doggystyle/2.webm", image="movie/robin/doggystyle/img.webp", character="robin")
image movie_robin_doggystyle cum  = MovieFallback(play="movie/robin/doggystyle/3.webm", image="movie/robin/doggystyle/img.webp", character="robin")

image robin_doggystyle_cum = "movie/robin/doggystyle/cum.webp"

label event_robin_doggystyle_vaginal:

    if robin_doggystyle == 0:
        player "[robin.n] I'm going to steal some of your time again!"
        robin "I don't mind at all, [player.n]! Don't worry... what's going on?"
        player "I want another advanced anatomy lesson... you know what I mean!"
        show robin c1 shame with dissolve
        robin "I love those kinds of lessons... What topic will we cover today?"

    else:
        robin "Do you want to repeat, [player.n]?"
        robin "Surely you took note of the previous opportunity..."


    window hide
    call robin_check pass (check_love = 25, check_lust = 25) from _robin_check_doggystyle
    show robin neutral with Dissolve(0.4)
           
    $ robin_doggystyle += 1

    pause 0.5
    show robin neutral c1_underwear with dissolve
    pause 0.5
    show robin neutral c1_naked with dissolve
    window auto

    robin "I feel like this lesson will be very interesting, [player.n]..."
    robin "If you like what you see, I want to see how much you enjoy what's next!"

    window hide
    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    play gems ["<silence 0.8>","gem_02","<silence 0.8>"] loop
    #play sound "titjob_1" loop
    show movie_robin_doggystyle slow
    
    window auto
    hide screen screen_black with Dissolve(0.8)

    pause 2


    robin "(Aaaah... My whole body jolts... What the helll?!)"
    robin "(Too big... God, he's filling me so fast, so deep...)"
    robin "([player.n]'s cock is filling every inch of me, hitting walls i didn't know existed)"

    jump event_robin_doggystyle_vaginal_slow

label event_robin_doggystyle_vaginal_slow:
    window hide
    window auto
    show movie_robin_doggystyle slow

    #REP KEEP
    pause 2.0

    player "Wow... Fuck!!"
    robin "Yeeeesssss... It's going in... Sooo deep!"
    robin "Do you like it as much as I do, [player.n]?"
    player "Fuck yess!!"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_robin_doggystyle slow
            pause
            jump event_robin_doggystyle_vaginal_slow

        "Faster":
            jump event_robin_doggystyle_vaginal_fast
    

label event_robin_doggystyle_vaginal_fast:
    window hide
    window auto
    show movie_robin_doggystyle fast

    pause 3.0
    
    robin "Ohh yess..."
    robin "Right theeere!!!"
    play gems "gem_02"
    robin "(The way he moves... It's like he's trying to hit all the right spots!!)"
    player "(Her pussy stretches with every inch I slide my cock into her!!)"
    player "(It's so addictive!!)"        
    robin "(Fuuuck!.. It's going faster and faster!)"
    robin "Ahhhm, mmf, yeeeessss [player.n]! Let's do it faster!"
    robin "(My insides are being dragged!!!... It's turning me inside out!!)"
    robin "I... I can't even catch my breath, yet..."
    robin "Fuuuck yeeesss... Do it faster!, Doooo it fa- faaaster!"    

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_robin_doggystyle_vaginal_slow

        "Keep going":
            show movie_robin_doggystyle fast
            pause
            jump event_robin_doggystyle_vaginal_fast

        "Cum":
            jump event_robin_doggystyle_vaginal_cum


label event_robin_doggystyle_vaginal_cum:

    show movie_robin_doggystyle cum

    robin "(I want to cum... I want to cum from him cumming inside off meee!!)"
    robin "Inside please!!! I waaant you to cuuuum insiiide me [player.n]!"
    robin "I-inside of my tummy!!"
    player "(Fuck she's crazy like fuck!!)"
    robin "I want you to shoot it out deep inside my tummy pleaseeee!!"
    robin "My womb I want it in my womb!!!"
    robin "I want you to cum straight into my womb [player.n]!"
    robin "Yeeeeesss!!!"    
    robin "It's feels, really really good... I'am goin to cum!!!!"
    robin "My senses are going numb, but i can clearly feel the pleasure!"
    player "Take it all!! take every single cell of sperm in my balls!!"    


    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    play gems "gem_01"
    show robin_doggystyle_cum at vibration  with flash
    hide movie_robin_doggystyle

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    #stop gems
    with flash
    pause 0.2
    with flash
    pause 2.0

    robin "I'm cummingggg... yeeessssss"
    robin "Inside my womb!!!"
    robin "(H-he's pooouring it soo deeeep iiinside!!!)"
    robin "Nfu aah aha nkuhh  twank ywouu!!!"
    robin "Aah he... he he eek..."
    player "You're a bitch when you're in this state..."
    robin "Nfu aah aha... Twank ywouu [player.n]!!!"
    player "Let me have a proper look at your face"
    player "You 're making such a lewd face..."
    player "You always make amazing cumming faces!!"

    window hide
    window auto
    pause 1.0
    jump event_robin_doggystyle_vaginal_end


label event_robin_doggystyle_vaginal_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    stop gems
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_robin_doggystyle
    hide robin_doggystyle_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show robin happy with dissolve
    
    player "Wow you were incredible... It was very good"
    $ talk_random = renpy.random.choice([
        _("Very, very good indeed!, next time let's practice another session!"),
        _("That was really really good! Until next time Captain!."),
    ])

    robin "[talk_random]"

    $ robin_lust += 2
    $ robin_love += 2
    narrador "[robin.n] Lust +2 and Love +2" 

    window hide
    show robin c1_underwear with dissolve
    pause 0.2
    show robin c1 with dissolve

    #jump robin_bye

    window hide
    hide robin with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location