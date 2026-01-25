# Version event: 5
# Version game: 0.31

default yamato_doggystyle = 0

image movie_yamato_doggystyle slow = MovieFallback(play="movie/yamato/doggystyle/1.webm", image="movie/yamato/doggystyle/img.webp", character="yamato")
image movie_yamato_doggystyle fast = MovieFallback(play="movie/yamato/doggystyle/2.webm", image="movie/yamato/doggystyle/img.webp", character="yamato")
image movie_yamato_doggystyle cum  = MovieFallback(play="movie/yamato/doggystyle/3.webm", image="movie/yamato/doggystyle/img.webp", character="yamato")

image yamato_doggystyle_cum = "movie/yamato/doggystyle/cum.webp"

label event_yamato_doggystyle_vaginal:

    if yamato_doggystyle == 0:
        player "[yamato.n], after so many moments lived, I think it's time to train seriously..."
        show yamato happy with dissolve
        yamato "Hahaha!"    
        yamato "What do you mean, [player.n]?!? I always train seriously..."
        player "Not like what I'm about to show you now..."
        player "This is a special training... First, I need you to get naked for me... What do you say?"
        pause 0.5
        show yamato shame with dissolve
        yamato "W-What?!"    
        yamato "I... erm.. I don't know..."
        pause 1.0   

    else:
        yamato "[player.n]!! I've been waiting for you..."
        yamato "Since the last time we trained, I can't stop thinking about you... I need a new session right now!"

    window hide
    call yamato_check pass (check_love = 25, check_lust = 25) from _yamato_check_doggystyle
    show yamato neutral with Dissolve(0.4)
           
    $ yamato_doggystyle += 1

    pause 0.5
    show yamato neutral c1_underwear with dissolve
    pause 0.5
    show yamato neutral c1_naked with dissolve
    window auto

    yamato "I already knew where you were going with this... Do you like what you see?"
    yamato "Let's see if you're up to the challenge... Let's see how fit you are..."

    window hide
    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    play gems ["<silence 0.8>","gem_02","<silence 0.8>"] loop
    #play sound "titjob_1" loop
    show movie_yamato_doggystyle slow
    
    window auto
    hide screen screen_black with Dissolve(0.8)

    pause 2
    yamato "Oh god! It's sooo big!"
    yamato "Niiice cock [player.n]..."
    yamato "I'm too wet, too full..."
    pause 0.5
    yamato "Beautiful scenery, isn't it?... Do you like having me in this submissive position?"
    yamato "This isn't a marathon, you know!... And we've only just begun..."  
    yamato "Pace your cardio well, I don't want to be disappointed..." 
    yamato "I'm a very hot and energetic girl! I want you to give me what I need!"

    jump event_yamato_doggystyle_vaginal_slow

label event_yamato_doggystyle_vaginal_slow:
    window hide
    window auto
    show movie_yamato_doggystyle slow

    pause 1.0
    yamato "Fuuuck... soo good, right?"
    yamato "I wish we had done this so much sooner!"
    yamato "I love the way it fills me so much!"
    yamato "Just enyoing every inch of you..."
    yamato "Just like you wanted, right?"
    pause 0.5
    yamato "Nmnmn... soo good... you like it when i talk dirty?"
    player "Fuck, I love it!!!!!"

    pause 0.5
    yamato "I love when my hot fucking captain stretches my trained pussy with his big fat cooock!!"
    yamato "That feels sooo good!"
    yamato "I love how hot it is..."
    pause 2.0
    yamato "Nnm... nmnm... Ahhh.."
    pause 1.0

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_yamato_doggystyle slow
            pause
            jump event_yamato_doggystyle_vaginal_slow

        "Faster":
            jump event_yamato_doggystyle_vaginal_fast
    

label event_yamato_doggystyle_vaginal_fast:
    window hide
    window auto
    show movie_yamato_doggystyle fast

    pause 3.0
    yamato "This rhythm... It's pulling me in... burning me up"
    yamato "(He's doing it faster... omfgood!!)"
    yamato "(It's too slick, too tight... burning where he's splitting me open)"
    yamato "(My body it's humming, craving, against my will)"    
    yamato "Come on and fuck me with that big, manly cock of yours!!"
    pause 8.0
    yamato "(Omg... Omgg!!!!)"
    yamato "(I'm too wet, too full... I can't get him out!)"
    yamato "I love the  feeling i get when your huge dick fills me up just right that!!"
    pause 1.0
    player "Fuuuuck... I can't take it anymore!!!"
    yamato "Yesss!!... Cum for mommy baby!!!, make me cum my brains out for you!"
    pause 1.0

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_yamato_doggystyle_vaginal_slow

        "Keep going":
            show movie_yamato_doggystyle fast
            pause
            jump event_yamato_doggystyle_vaginal_fast

        "Cum":
            jump event_yamato_doggystyle_vaginal_cum


label event_yamato_doggystyle_vaginal_cum:

    show movie_yamato_doggystyle cum

    yamato "(I'm a mess, filthy... i can't... Too much.... I'm lost...)"
    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    play gems "gem_01"
    show yamato_doggystyle_cum at vibration  with flash
    hide movie_yamato_doggystyle

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    #stop gems
    with flash
    pause 0.2
    with flash
    pause 2.0
    yamato "Fuuuuuck yes..."
    pause 0.5
    yamato "My legs... They're gone... I'm stuck, cumming again..."
    yamato "Shitt..."
    yamato "Ooohh... Shitt... That was really good!!"
    
    window hide
    window auto
    pause 1.0
    jump event_yamato_doggystyle_vaginal_end


label event_yamato_doggystyle_vaginal_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    stop gems
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_yamato_doggystyle
    hide yamato_doggystyle_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show yamato happy with dissolve
    
    player "Wow so intense [yamato.n]..."
    show yamato happy with dissolve
    yamato "Shitt... That was really good!!"
    yamato "I had a great time [player.n], but you need a little more cardio hehe... We will improve it the next time!"



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