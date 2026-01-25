# Version event: 2
# Version game: 0.28

default nami_doggystyle_anal = 0

image movie_nami_doggystyle_anal_ass = MovieFallback(play="movie/nami/anal/doggystyle/ass.webm", image="movie/nami/anal/doggystyle/ass_img.webp", character="nami")

image movie_nami_doggystyle_anal slow = MovieFallback(play="movie/nami/anal/doggystyle/1.webm", image="movie/nami/anal/doggystyle/img.webp", character="nami")
image movie_nami_doggystyle_anal fast = MovieFallback(play="movie/nami/anal/doggystyle/2.webm", image="movie/nami/anal/doggystyle/img.webp", character="nami")
image movie_nami_doggystyle_anal cum  = MovieFallback(play="movie/nami/anal/doggystyle/3.webm", image="movie/nami/anal/doggystyle/img.webp", character="nami")


label nami_doggystyle_anal:

    if nami_doggystyle_anal == 0:
        player "[nami.n] how's everything going?"
        player "Our situation is improving rapidly... You know, the whole financial issue of the crew"
        show nami happy with dissolve
        nami "That's great, Captain!"
        show nami neutral with dissolve
        nami "When you bring up these financial topics with me, I already know where you're going with this..."
        nami "You want to 'relax' again, don't you?"
        nami "You know how things work around here... I can give you whatever you want... But that comes at a price..."
        player "I'll pay well! That's for sure hahaha"


    else:
        nami "Do you want to repeat Captain?"
        nami "I'm delighted... But you know how this works..."

    menu:
        "80 berries" if berries >= 80:
            call nami_check pass (check_love = 50, check_lust = 50, check_berries = 80) from _nami_check_doggystyle_anal_80
            show nami happy with dissolve

        "Bargain, 40 berries" if berries >= 40:
            call nami_check pass (check_love = 55, check_lust = 55, check_berries = 40) from _nami_check_doggystyle_anal_40
            show nami happy with dissolve

        "No payment":
            call nami_check pass (check_love = 60, check_lust = 60, check_berries = 0) from _nami_check_doggystyle_anal_0
            show nami neutral with dissolve

           
    pause 1.0
    window hide
    show nami neutral c1_underwear with dissolve
    pause 0.5
    show nami neutral c1_naked with dissolve

    nami "Do you like what you see, Captain?"
    nami "Just tell me what to do and I'll obey without question"
    nami "I'm all yours now!"
    player "I love it! Get on the bed... but on all fours first, I want to get a good look at you..."

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show movie_nami_doggystyle_anal_ass
    hide screen screen_black with Dissolve(0.8)

    pause 4.0

    if nami_doggystyle_anal == 0:
        nami "How is it? Can you see it well?"
        nami "Fufu everything is for eperience... Do you want to try practicing anals sex?"
        player "I'll love to shov my cockc in this tight pretty hole!" 
        nami "It must be your first time having an up-close look at my ass Captain"
        nami "This fuckhole wants your cock inside!"
        nami "It wants your dick so bad that it's twitching, see?"
        nami "Please let this ass devour that... poor dick of yours... that it's about to explode!!"

    else:
        nami "How is it? Can you see it well?"
        nami "This fuckhole wants your cock inside!"
        nami "It wants your dick so bad that it's twitching, see?"
        nami "Please let this ass devour that... poor dick of yours... that it's about to explode!!"

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    play sound "footjob_1" loop
    #play sound "titjob_1" loop
    hide movie_nami_doggystyle_anal_ass
    show movie_nami_doggystyle_anal slow

    hide screen screen_black with Dissolve(0.8)

    $ nami_doggystyle_anal += 1

    player "Your ass is tight as fuck [nami.n]!"
    nami "(This feels so... different from my pussy!)"
    nami "(Damn it.. damn it... it's in sooo deep!)"
    nami "It's been a while since i've had an anal sex!"
    nami "M-my ass is letting out weird noises beacuse of your fat dick!"


    jump nami_doggystyle_anal_slow

#doggystyle_anal
label nami_doggystyle_anal_slow:
    window hide
    window auto
    show movie_nami_doggystyle_anal slow

    pause 3.0
    #dia rep

    nami "Nnnnggghhhhh!! I don't remember anal sex feeling this good!!"
    nami "The deeper you go, the more i love it!"
    nami "Y-you're going to make me hooked on this!"
    nami "Anal feels a lot different from my pussy"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_nami_doggystyle_anal slow
            pause
            jump nami_doggystyle_anal_slow

        "Faster":
            player "Go faster!!"
            jump nami_doggystyle_anal_fast
    

label nami_doggystyle_anal_fast:
    window hide
    window auto
    show movie_nami_doggystyle_anal fast

    pause 3.0
    #dia rep
    
    nami "Fucking me hard, captain!"
    nami "(He's grinding soo deep against me...)"
    nami "(Every time he trusts, i can fell the wave of pleasure closing in!)"
    nami "Ohn! Oh! Nhonnn!! Ooghnnn!"
    nami "Your dick is... Stabbing my womb from my asss!!!"
    nami "My ass is gonna breaaaaaak!!"
    nami "Other guys are just no match for you Captain!!"    

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump nami_doggystyle_anal_slow

        "Keep going":
            show movie_nami_doggystyle_anal fast
            pause
            jump nami_doggystyle_anal_fast

        "Cum":
            jump nami_doggystyle_anal_cum


label nami_doggystyle_anal_cum:

    show movie_nami_doggystyle_anal cum

    nami "Impregnating dickk!"
    nami "Breeding dick!"
    nami "I love it!"
    nami "Your raw coock is great!"
    nami "My ass is gonna take your shape..."
    nami "Impregnate my asss!"
    nami "I'm cumming, cumming, cumming!"    
    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    show events nami anal doggystyle nami_doggystyle_cum at vibration  with flash
    hide movie_nami_doggystyle_anal

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    nami "What a huge load..."   
    nami "Aahh it's sho hot and sho thick, Captain!"
    nami "Huh... Oohh my ass is burniiing!!"
    nami "Ehehe cum tastes sho goood!"

    window hide
    window auto
    pause 1.0
    jump nami_doggystyle_anal_end


label nami_doggystyle_anal_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_nami_doggystyle_anal
    hide events nami anal doggystyle nami_doggystyle_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show nami happy with dissolve
    
    player "Wow you were incredible... It was very good"
    player "If you keep cuming like this, I'm going to have to charge you."

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