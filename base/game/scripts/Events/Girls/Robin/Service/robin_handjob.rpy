# Version event: 3
# Version game: 0.32

default robin_handjob = 0

image movie_robin_handjob slow = MovieFallback(play="movie/robin/handjob/1.webm", image="movie/robin/handjob/img.webp", character="robin")
image movie_robin_handjob fast = MovieFallback(play="movie/robin/handjob/2.webm", image="movie/robin/handjob/img.webp", character="robin")
image movie_robin_handjob cum  = MovieFallback(play="movie/robin/handjob/3.webm", image="movie/robin/handjob/img.webp", character="robin")

image robin_handjob_cum = "movie/robin/handjob/cum.webp"

label event_robin_handjob:

    if robin_handjob == 0:
        player "[robin.n] I'm going to steal some of your time again!"
        robin "I don't mind at all... What's going on?"
        player "Maybe we could continue experimenting together again?"
        player "I would love if you help me to relax a bit..." 
        show robin c1 shame with dissolve
        robin "Hahah... I love those kinds of experiments... But i don't know..."

    else:
        robin "Do you want another session [player.n]?"
        robin "Surely you took note of the previous opportunity..."


    window hide
    call robin_check pass (check_love = 20, check_lust = 20) from _robin_check_handjob
    show robin neutral with Dissolve(0.4)
           
    $ robin_handjob += 1

    pause 0.5
    show robin neutral c1_underwear with dissolve
    pause 0.5
    show robin neutral c1_naked with dissolve
    window auto

    player "Today we're going to do some manual work, what do you think?"    
    robin "Mnmnm i like it... Then..."
    robin "Your dick [player.n], show it to me!"
    robin "Today I will stroke it for you okay?!?"

    
    window hide
    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    #play gems ["<silence 0.8>","gem_02","<silence 0.8>"] loop
    #play sound "titjob_1" loop
    show movie_robin_handjob slow
    
    window auto
    hide screen screen_black with Dissolve(0.8)

    pause 2
    robin "Look at the size of you..."
    player "(And I'd say the same, look at those two huge melons)"
    robin "[player.n]'s dick is soo amazing..."
    robin "The way it hangs hard, heavy, arrogant..."
    robin "The smell... So obscene and strong..."
    robin "Your dick must be so tired after such a long day of work..."
    robin "I'm going to help you relax..."

    jump event_robin_handjob_slow

#handjob
label event_robin_handjob_slow:
    window hide
    window auto
    show movie_robin_handjob slow

    pause 1.0
    #REPETITIVE
    robin "Good..."    
    robin "I'll make it even more wet and slippery!"
    robin "This smell again, strong, sharp... Like heat and skin!"
    robin "It twitches, like it's waiting for me... Like it knows i'll keep going..."
    player "It feels so good that you're jerking me off [robin.n]"
    robin "It feels good when i rub the tip too? ...Does it feel good?"
    robin "I'll focus on the tip for a while!"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_robin_handjob slow
            pause
            jump event_robin_handjob_slow

        "Faster":
            jump event_robin_handjob_fast
    

label event_robin_handjob_fast:
    window hide
    window auto
    show movie_robin_handjob fast

    pause 3.0
    #dialogos repetitivos
    player "Ahhh faster, don't stop! Keep stroking it hard!"
    robin "It's twitching so much... You're about to explode aren't you?"
    player "Fuck... yes, if you keep this up I won't last!"
    robin "Then let it go... spill it all out for me!"
    robin "I'll make you lose control, [player.n]... Just give it to me!"
   

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_robin_handjob_slow

        "Keep going":
            show movie_robin_handjob fast
            pause
            jump event_robin_handjob_fast

        "Cum":
            jump event_robin_handjob_cum


label event_robin_handjob_cum:

    show movie_robin_handjob cum

    robin "Does it feel good?"
    robin "Come on let it out. Let it all out!"
    robin "Come one just hurry and shoot your load!"
    robin "Cun for me [player.n]!!!"
    player "Take it them!!"

    
    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    #play gems "gem_01"
    show robin_handjob_cum at vibration  with flash
    hide movie_robin_handjob

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    #stop gems
    with flash
    pause 0.2
    with flash
    pause 2.0

    robin "Aaaaaahhhh yesssss... So warm... So hot..."
    robin "That's... So much... Leaking out"
    robin "It's everywhere... So good!"
    robin "You came buckets!"
    robin "I can feel [player.n]'s jizz pouring out... "


    window hide
    window auto
    pause 1.0
    jump event_robin_handjob_end


label event_robin_handjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    #stop gems
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_robin_handjob
    hide robin_handjob_cum
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

    jump robin_bye