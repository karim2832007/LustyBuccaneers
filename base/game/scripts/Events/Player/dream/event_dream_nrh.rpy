# Version event: 2
# Version game: 0.17

default dream_nrh = False

image movie_group_nrh slow = MovieFallback(play="movie/group/nrh/1.webm", image="events group nrh nrh", character="nami")
image movie_group_nrh fast = MovieFallback(play="movie/group/nrh/2.webm", image="events group nrh nrh", character="nami")
image movie_group_nrh cum  = MovieFallback(play="movie/group/nrh/3.webm", image="events group nrh nrh", character="nami")

# Nami Robin Hancock
label event_dream_nrh:
    if dream_nrh:
        menu:
            narrador "Do you want to see the dream with [nami.n], [robin.n] and [hancock.n]?"

            "Yes":
                pass

            "No":
                jump sleep

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    hide screen screen_black with Dissolve(0.8)

    # toc toc
    narrador "Knock Knock"
    player "Mnmnm... (What time is it?)"
    player "(Who could it be this early... We haven't even started yet, and they already need me... These girls...)"
    player "Come in!!"
    pause 0.5

    show nami at center 
    show robin at left
    show hancock at right
    with dissolve

    player "(What?!?... What are the three of her doing here? What could they be up to...)"
    player "What's going on? It's strange to see all of you here so early..."
    nami "Good morning, Captain..."
    hancock "Were you resting, [player.n]..."
    robin "Up sleepy head!!..."
    player "Mnmnmn, what are you three plotting..."
    hancock "It surprises me that you'd think that of us, [player.n], with how much we care about you!"
    robin "You know something captain..."
    robin "Extra classes suck..."
    robin "But... If it was a physical lesson type..."
    robin "I'd be earning top grades"

    player "Are you kidding?"
    player "Hhahah, Wanna put all of you to test??"

    nami "We would like to practice bedroom activities..."
    nami "Would you be so kind as to spar with us?"
    player "Really?!?"

    hancock "It's so hot outside.... Let's cool off a bit"

    window hide
    window auto

    show nami neutral c1_underwear 
    show robin neutral c1_underwear     
    show hancock neutral c1_underwear 
    with Dissolve(0.8)
    pause 0.5
    show nami neutral c1_naked 
    show robin neutral c1_naked     
    show hancock neutral c1_naked 
    with Dissolve(0.8)

    #se desnudan
    player "(Damn!!!... I can't believe it!!)"
    robin "Hurry up and get started!!!"
    nami "I'll go first since I was the first to join the crew!"
    hancock "That's unfair! I wanted to go first!"


    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    window hide
    window auto

    show screen screen_black with Dissolve(0.8)
    show events group nrh nrh
    hide nami
    hide robin
    hide hancock
    hide screen screen_black with Dissolve(0.8)

    pause 1

    player "(Wow, I must be dreaming!)"
    robin "There is still some time before the rest of the girls comes back..."
    hancock "Now we're all going to feel good"
    nami "Do your best! To have fun doing it together!!"
    hancock "Woah that's Huge, [player.n] cock is the best!"

    jump event_dream_nrh_slow


label event_dream_nrh_slow:
    window hide
    window auto
    show movie_group_nrh slow with Dissolve(0.3)

    pause 3.0

    #repetitivo
    nami "It feels soooo good!"
    hancock "Watching [nami.n] made me become soooo hot!"
    robin "I want to play with [nami.n] tooo!!"
    nami "You'll have your turn whores, this huge cock is all mine now!"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_group_nrh slow with Dissolve(0.5)
            pause
            jump event_dream_nrh_slow

        "Faster":
            jump event_dream_nrh_fast


label event_dream_nrh_fast:
    window hide
    window auto
    show movie_group_nrh fast with Dissolve(0.5)

    pause 3.0
    #dialogos repetitivos

    nami "Soooo good!!"    
    hancock "I wanna get fucked by [player.n] too... Pound me hard!!!... I bet my pussy feels even better!"
    robin "It's not fair that [nami.n] gets all the attention! When is my turn?"
    nami "Don't listen to these bitches, and do it harder!!"
    nami "Right there Captain!!! Make me a sloppy mess"

    pause 2.0

    menu:
        "Slower":
            jump event_dream_nrh_slow

        "Keep going":
            show movie_group_nrh fast with Dissolve(0.5)
            pause
            jump event_dream_nrh_fast

        "Cum":
            jump event_dream_nrh_cum

label event_dream_nrh_cum:
    show movie_group_nrh cum

    player "(Fuuck... I'm reaching my limit...She do it so well!)"
    nami "Feels sho guuuuud!"
    nami "Hngggg"
    nami "My head is going crazzy!"
    robin "Go ahead [nami.n] cum! cum!"
    nami "Ah  I'm going to cum!!!"
    hancock "[player.n] let's cum together!"
    player "Don't you worry I'm gonna fill you up with plenty of jizz [nami.n]!!"

    window hide
    window auto

    pause 1.0

    play sound "cum_01"
    show events group nrh nrh_cum at vibration
    hide movie_group_nrh with flash

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    player "Wow this was incredible it almost didn't seem real!"
    hancock "There is so much everywhere!!"
    nami "Shoooo guuuuud!"
    robin "Hahaha it looks like a brainless!!"
    hancock "Now it's my turn, you have to take responsibility [player.n]!"
    robin "I hope you are ready for 2 or 3 more rounds!"

    window hide
    window auto

    hide events group nrh nrh_cum with Dissolve(1.2)
    pause 0.5

    $ ui_interface = True
    $ dream_nrh = True
    jump sleep_dream