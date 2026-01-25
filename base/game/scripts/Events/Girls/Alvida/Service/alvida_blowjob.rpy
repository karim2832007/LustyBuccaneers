# Version event: 2
# Version game: 0.27

default alvida_blowjob = 0

image movie_alvida_blowjob slow = MovieFallback(play="movie/alvida/blowjob/1.webm", image="movie/alvida/blowjob/img.webp", character="alvida")
image movie_alvida_blowjob fast = MovieFallback(play="movie/alvida/blowjob/2.webm", image="movie/alvida/blowjob/img.webp", character="alvida")
image movie_alvida_blowjob cum  = MovieFallback(play="movie/alvida/blowjob/3.webm", image="movie/alvida/blowjob/img.webp", character="alvida")

label event_alvida_blowjob:

    if alvida_blowjob == 0:

        player "I will teach you to respect me!"
        player "Take off your clothes and get on your knees!"
        alvida "What? You can't be serious..."
        player "I'm not giving you an option, [alvida.n]. Do as I say..."
        player "You're on my ship now... You have no power here!"
        alvida "I can't believe this is happening..."
        player "Now, move. I don't have all day..."
        player "I warn you... you don't want to see me angry."
        alvida "Fine... I'll do as you say... But don't think I'll forget this!!"
        player "You're right, you'll never forget... My cock!"

    else:
        player "And here we are again, [alvida.n]..."
        player "How about we repeat what we did last time?"
        player "Why don't Kneel down [alvida.n], I know you liked it...."

           
    $ alvida_blowjob += 1

    pause 0.2
    window hide
    #show alvida c1_underwear with dissolve
    pause 0.4
    show alvida c1_naked with dissolve
    window auto

    pause 0.5

    alvida "You like what you see?!... I'm sure you won't last me even 5 minutes, nobody..."

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    #play sound "footjob_1" loop
    play sound ["deepthroat_01","<silence 0.1>","blowjob_02","<silence 0.2>","blowjob_01"] loop
    show movie_alvida_blowjob slow
    window hide
    window auto
    hide screen screen_black with Dissolve(0.8)

    pause 2.0

    alvida "(Now that his dick is in front of me...)"
    alvida "(It's so big... It can barely fit in my mouth)"
    alvida "(To think that [alvida.n] the Iron Mace will kiss a nobody's cock so submissively...)"

    jump event_alvida_blowjob_slow

#blowjob
label event_alvida_blowjob_slow:
    window hide
    window auto
    show movie_alvida_blowjob slow

    pause 3.0
    #dialogos repetitivos

    alvida "(This warmth....)"
    alvida "(He is dripping so much of his pre cum...)"
    alvida "(This smell...)"
    alvida "(It... Stinks....)"
    alvida "(It's salty... And it tastes grosss... Mnmnm)"
    alvida "(I'm really enjoying it!)" 

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_alvida_blowjob slow
            pause
            jump event_alvida_blowjob_slow

        "Faster":
            player "Go faster!!"
            jump event_alvida_blowjob_fast
    

label event_alvida_blowjob_fast:
    window hide
    window auto
    show movie_alvida_blowjob fast
    play sound ["deepthroat_01","<silence 0.1>","blowjob_01", "<silence 0.1>", "deepthroat_01", "<silence 0.1>", "blowjob_02"] loop

    pause 3.0
    #dialogos repetitivos

    player "well well well... you're so eager swaying you hips like that"      
    alvida "(Sooo good.... I Love it!)"
    alvida "(This is bad... this is real bad... Just from licking it i'm gonna.... Cummmm!!)" 
    alvida "Fuuuuuck...." 
    alvida "(Itsh... shoooo goodd! I love this cock!)" 
    alvida "Splatter my mouth with your jizz pleeeeeease!"
    alvida "spray your fuck-sauce in my moouth!!"   
   
    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_alvida_blowjob_slow

        "Keep going":
            show movie_alvida_blowjob fast
            pause
            jump event_alvida_blowjob_fast

        "Cum":
            jump event_alvida_blowjob_cum


label event_alvida_blowjob_cum:

    show movie_alvida_blowjob cum
    
    window hide
    window auto

    pause 1.0

    play sound "cum_01"
    show events alvida blowjob alvida_blowjob_cum at vibration  with flash
    hide movie_alvida_blowjob

    pause 0.1
    play sound ["deepthroat_01","<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    alvida "Cock... Cock miiiilk!"
    alvida "Sooo good"
    alvida "It was so Thick... I thought my mouth would get pregnant from it!"

    pause 0.2


    window hide
    window auto
    pause 1.0
    jump event_alvida_blowjob_end


label event_alvida_blowjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_alvida_blowjob
    hide events alvida blowjob alvida_blowjob_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()
    
    player "Hahaha! It seems like you enjoyed it in the end..."
    alvida "..."
    show alvida c1_naked neutral with Dissolve(0.2)
    alvida "(It's incredible that he's right... I'm left wanting more....)"
    player "That's all, [alvida.n]. You can go now..."
    alvida "This won't end here... we'll meet again..."

    $ alvida_lust += 2
    $ alvida_love += 2
    narrador "[alvida.n] Lust +2 and Love +2" 

    window hide
    #show alvida c1_underwear with dissolve
    pause 0.2
    show alvida c1 with dissolve

    #jump alvida_bye

    window hide
    hide alvida with moveoutright

    player "I knew she wouldn't forget... I'll be waiting for the next one!"
    
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location