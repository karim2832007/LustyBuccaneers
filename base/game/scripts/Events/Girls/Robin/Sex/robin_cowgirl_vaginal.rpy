# Version event: 4
# Version game: 0.30

default robin_cowgirl = 0

image movie_robin_cowgirl slow = MovieFallback(play="movie/robin/cowgirl/1.webm", image="movie/robin/cowgirl/img.webp", character="robin")
image movie_robin_cowgirl fast = MovieFallback(play="movie/robin/cowgirl/2.webm", image="movie/robin/cowgirl/img.webp", character="robin")
image movie_robin_cowgirl cum  = MovieFallback(play="movie/robin/cowgirl/3.webm", image="movie/robin/cowgirl/img.webp", character="robin")

image robin_cowgirl_cum = "movie/robin/cowgirl/cum.webp"

label event_robin_cowgirl:

    if robin_cowgirl == 0:
        player "[robin.n] I was just looking for you... The rest of the girls are busy with different tasks I gave them..."
        player "It's a good time for you and me to enjoy some time alone..."
        player "I want another advanced anatomy lesson... You know what I mean!"
        robin "I've been waiting for you [player.n]"
        robin "All this teasing with over these past days... Has made me soooo... Horny!"
        robin "I just can't help it..."
        show robin c1 shame with dissolve
        robin "I have a problem in my lower area... Perhaps you can see me, doctor...."
        player "I don't think there's any other option... I need to be able to check the area..."


    else:
        robin "Do you want to repeat, [player.n]?"
        robin "Surely you took note of the previous opportunity..."


    window hide
    call robin_check pass (check_love = 30, check_lust = 30) from _robin_check_cowgirl
    show robin neutral with Dissolve(0.4)
           
    $ robin_cowgirl += 1

    pause 0.5
    show robin neutral c1_underwear with dissolve
    pause 0.5
    show robin neutral c1_naked with dissolve
    window auto

    robin "My pussy has a mind of it own and it's dripping right now..."
    player "I see it clearly... It's a serious problem..."
    robin "It's because i've been a naughty girl, haven't I?"
    robin "I think i deserve to be punished...."
    robin "What do you thin, [player.n]?"
    robin "Are you ready to punish me for being such a bad... bad... girl?!?"
    
    window hide
    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    play gems ["<silence 0.8>","gem_02","<silence 0.8>"] loop
    #play sound "titjob_1" loop
    show movie_robin_cowgirl slow
    
    window auto
    hide screen screen_black with Dissolve(0.8)

    pause 2
    player "Wow... Fuck!!"
    robin "Yeeeesssss... It's going in... Sooo deep!"
    robin "Do you like it as much as I do, [player.n]?"
    player "Fuck yess!!"
    robin "Mmmmfff"
    pause 1.0
    robin "Focus on me, doctor... I don't want to lose you so quickly... "
    robin "Look at these huge tits you have here in front of you [player.n]..."  
    robin "I know you've always liked these big tits of mine"
    robin "Every time I see you, I can feel you drooling all over them"
    robin "Does the thought of you groping my tits make you hard, [player.n]?"
    robin "These are just begging to be ravaged"
    robin "I'm your dirty little slut... After all"
    player "Fuck yess!! I swear I will!"

    jump event_robin_cowgirl_slow

label event_robin_cowgirl_slow:
    window hide
    window auto
    show movie_robin_cowgirl slow

    pause 3.0

    robin "If you liked that, I want to see how much you enjoy what's next!"


    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_robin_cowgirl slow
            pause
            jump event_robin_cowgirl_slow

        "Faster":
            player "Go faster!!"
            jump event_robin_cowgirl_fast
    

label event_robin_cowgirl_fast:
    window hide
    window auto
    show movie_robin_cowgirl fast

    pause 3.0
    
    robin "I love being your little slut and i love your cock [player.n]!"
    robin "I love how it's twitching... Begging for more.."
    robin "Your cock is such a perfect fit for my pussy!"
    robin "I want you to feed me your cum, [player.n], i really want it!"

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_robin_cowgirl_slow

        "Keep going":
            show movie_robin_cowgirl fast
            pause
            jump event_robin_cowgirl_fast

        "Cum":
            jump event_robin_cowgirl_cum


label event_robin_cowgirl_cum:

    show movie_robin_cowgirl cum

    robin "Come one just hurry and shoot your load!"
    robin "Cun for me [player.n]!!!"
    player "Take it them!!"

    
    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    play gems "gem_01"
    show robin_cowgirl_cum at vibration  with flash
    hide movie_robin_cowgirl

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    #stop gems
    with flash
    pause 0.2
    with flash
    pause 2.0

    robin "Aaaaaahhhh yesssss...."
    robin "So good!"
    robin "You came buckets!"
    robin "I can feel [player.n]'s jizz pouring out... "


    window hide
    window auto
    pause 1.0
    jump event_robin_cowgirl_end


label event_robin_cowgirl_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    stop gems
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_robin_cowgirl
    hide robin_cowgirl_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show robin happy with dissolve
    
    player "Wow you were incredible [robin.n]..."
    robin "And there is still a lot to teach you... But that will be the next time...."
    player "There will be more time to play... See you next time!"


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