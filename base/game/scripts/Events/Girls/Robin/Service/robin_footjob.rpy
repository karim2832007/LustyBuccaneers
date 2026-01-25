# Version event: 2
# Version game: 0.16

default robin_footjob = 0

image movie_robin_footjob slow = MovieFallback(play="movie/robin/footjob/1.webm", image="movie/robin/footjob/img.webp", character="robin")
image movie_robin_footjob fast = MovieFallback(play="movie/robin/footjob/2.webm", image="movie/robin/footjob/img.webp", character="robin")
image movie_robin_footjob cum  = MovieFallback(play="movie/robin/footjob/3.webm", image="movie/robin/footjob/img.webp", character="robin")

label event_robin_footjob:

    if robin_footjob == 0:
        player "[robin.n] I'm going to steal some of your time again!"
        robin "I don't mind at all... What's going on?"
        player "I would love to use your body for a 'test'... Maybe we could continue experimenting together again?"
        show robin c1 shame with dissolve
        robin "Hahah... I love those kinds of experiments... But i don't know..."

    else:
        robin "Do you want to repeat?"
        robin "Surely you took note of the previous opportunity..."
        robin "Does my Footjob feels good, Captain?"


    call robin_check pass (check_love = 35, check_lust = 35) from _robin_check_footjob
    show robin neutral with dissolve
           
    $ robin_footjob += 1

    robin "Come here, I have something on my mind..."

    window hide
    window auto

    pause 0.3
    show robin neutral c1_naked with dissolve
    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events robin footjob robin_footjob_1
    hide screen screen_black with Dissolve(0.8)
    pause 1.5
    window hide
    window auto

    robin "What do you think, Captain? Do you like what you see?"
    player "(WOW!!, [robin.n] is soooo sexy. She knows what she's doing... I like how she thinks!)"
    robin "You thought i was going to use my hands?"
    robin "Today, for you my feet is enough..."
    player "Whatever you say my captain!"



    window hide
    window auto
    pause 1.0
    show robin_footjob_2_1
    show robin_footjob_2_2:
        xalign 0.5
        yalign 1.0
        yoffset 700
    show robin_footjob_2_3
    with dissolve
    hide events robin footjob robin_footjob_1

    pause 0.3
    robin "Come on [player.n], put your big hard cock between my feet right now!"
    window hide
    window auto
    pause 0.3

    show robin_footjob_2_2:
        xalign 0.5
        yalign 1.0
        yoffset 700
        ease 0.6 yoffset 0

    pause 2

    robin "Whoahh you're rock hard... Looks like it's going to explode!"
    robin "I'll start moving, tell me if you want me to go slower or faster."

    window hide
    window auto
    play sound "footjob_1" loop
    show movie_robin_footjob slow with dissolve
    hide robin_footjob_2_1
    hide robin_footjob_2_2
    hide robin_footjob_2_3

    jump event_robin_footjob_slow

#footjob
label event_robin_footjob_slow:
    window hide
    window auto
    show movie_robin_footjob slow

    pause 3.0
    #dialogos repetitivos
    robin "Uwah... It's really hot..."
    robin "Does my footjob make your cock feel good?"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_robin_footjob slow
            pause
            jump event_robin_footjob_slow

        "Faster":
            player "Ughhg... Go faster!"
            jump event_robin_footjob_fast
    

label event_robin_footjob_fast:
    window hide
    window auto
    show movie_robin_footjob fast

    pause 3.0
    #dialogos repetitivos
    robin "My feet... Are covered in you lewd juice now..."
    robin "You are a naughty boy..."
    robin "Go on cum!! Cum for me!"

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_robin_footjob_slow

        "Keep going":
            show movie_robin_footjob fast
            pause
            jump event_robin_footjob_fast

        "Cum":
            robin "Ah it's throbbing, that means you're about tu cum right?"
            robin "Show me how you cum from my feet Captain"  
            robin "Go on cum!"            
            robin "Cum from being jacked off by my feet"          
            jump event_robin_footjob_cum


label event_robin_footjob_cum:
    show movie_robin_footjob cum
    
    window hide
    window auto

    pause 1.0

    
    play sound "cum_01"
    show events robin footjob robin_footjob_cum at vibration
    hide movie_robin_footjob with flash
    

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    robin "You came a lot!!"
    robin "The touch of my feet is very confortable right?"               
    robin "Look... It's all stringy... It's like natto..."
    robin "It's so thick ah... awesome!!!"

    window hide
    window auto
    pause 1.0
    jump event_robin_footjob_end


label event_robin_footjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_robin_footjob
    hide events robin footjob robin_footjob_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show robin happy with dissolve
    
    robin "That was fun, let's do it again!!"

    $ robin_lust += 2
    $ robin_love += 2
    narrador "[robin.n] Lust +2 and Love +2" 

    window hide
    show robin c1_underwear with dissolve
    pause 0.2
    show robin c1 with dissolve

    jump robin_bye