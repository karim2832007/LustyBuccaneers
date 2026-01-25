# Version event: 2
# Version game: 0.25

default hancock_cowgirl = 0

image movie_hancock_cowgirl slow = MovieFallback(play="movie/hancock/cowgirl/1.webm", image="movie/hancock/cowgirl/img.webp", character="hancock")
image movie_hancock_cowgirl fast = MovieFallback(play="movie/hancock/cowgirl/2.webm", image="movie/hancock/cowgirl/img.webp", character="hancock")
image movie_hancock_cowgirl cum  = MovieFallback(play="movie/hancock/cowgirl/3.webm", image="movie/hancock/cowgirl/img.webp", character="hancock")

label event_hancock_cowgirl:

    if hancock_cowgirl == 0:

        player "[hancock.n] I feel like we're getting closer lately."
        player "You're truly attractive and sexy woman..."
        player "Now we can keep moving forward..."
        show hancock c1 shame with dissolve           
        hancock "Always saying such flattering things about me [player.n]..."
        hancock "What is it that you want to do?"
        player "Why don't you take off your clothes and come with me to the bed?..."

    else:
        player "Every day you're more attractive and sexy, [hancock.n]..."
        player "You know you shouldn't hide so much beauty from the world..."
        player "Why don't you take off your clothes and come with me to the bed again?..."


    window hide
    call hancock_check pass (check_love = 30, check_lust = 30) from _hancock_check_cowgirl
    show hancock neutral with Dissolve(0.4)
           
    $ hancock_cowgirl += 1

    pause 1.0
    show hancock neutral c1_underwear with dissolve
    pause 0.5
    show hancock neutral c1_naked with dissolve
    window auto

    hancock "I'm ready... Make me yours [player.n]..."

    window hide
    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    #play sound "titjob_1" loop
    show movie_hancock_cowgirl slow
    
    window auto
    hide screen screen_black with Dissolve(0.8)

    pause 2
    hancock "(Yeeees, this is it!!)"
    hancock "([player.n]'s cock went inside my vagina...)"
    hancock "(It's so delicious...)"
    hancock "(Give me lots of raw fuckin!)"

    jump event_hancock_cowgirl_slow

label event_hancock_cowgirl_slow:
    window hide
    window auto
    show movie_hancock_cowgirl slow

    pause 3.0

    hancock "I'm so happy!"
    player "[hancock_name]... Wow [hancock_name]...."
    hancock "I'm so happy! more more..."
    hancock "Fuck me harder and say my name more!"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_hancock_cowgirl slow
            pause
            jump event_hancock_cowgirl_slow

        "Faster":
            player "Go faster!!"
            jump event_hancock_cowgirl_fast
    

label event_hancock_cowgirl_fast:
    window hide
    window auto
    show movie_hancock_cowgirl fast

    pause 3.0
    #dia rep
    
    hancock "Your cock today... is the hardest that's ever been..."
    hancock "Your thick part... is stirring up... my insides"
    hancock "It feels soooo good... it's pulling at my insides"
    hancock "(Aaah!!! your cock is so deep!!!)"
    hancock "(I love you cock sooo much... I'm gonna go insane!!)"
    player "Fuuuckk...."    
    hancock "Fill this hole with your cock!!"
    hancock "Yes, yeeesss, at this angle! if you thrust like this, my womb will took your shape!"
    hancock "I've gotten drunk on cock!"
    hancock "Keep goin! let's cum!"


    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_hancock_cowgirl_slow

        "Keep going":
            show movie_hancock_cowgirl fast
            pause
            jump event_hancock_cowgirl_fast

        "Cum":
            jump event_hancock_cowgirl_cum


label event_hancock_cowgirl_cum:

    show movie_hancock_cowgirl cum

    hancock "(I want to become pregnant with [player.n]'s child!!)"
    hancock "Cum with me!!! Cum in my womb!!"
    
    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    show events hancock cowgirl hancock_cowgirl_cum at vibration  with flash
    hide movie_hancock_cowgirl

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    hancock "Sooo hot!! it's filling me up...?!"
    hancock "Looks like we both came at the same time, huh?"
    hancock "You let out so much inside me..."
    pause 0.2
    hancock "Creampie feels crazy... I might get addicted to this..."

    window hide
    window auto
    pause 1.0
    jump event_hancock_cowgirl_end


label event_hancock_cowgirl_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_hancock_cowgirl
    hide events hancock cowgirl hancock_cowgirl_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show hancock happy with dissolve
    
    hancock "I enjoy being with you more and more, let's see when we repeat."

    $ hancock_lust += 2
    $ hancock_love += 2
    narrador "[hancock.n] Lust +2 and Love +2" 

    window hide
    show hancock c1_underwear with dissolve
    pause 0.2
    show hancock c1 with dissolve

    #jump hancock_bye

    window hide
    hide hancock with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location