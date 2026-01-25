# Version event: 2
# Version game: 0.34

default uta_titjob = 0

image movie_uta_titjob slow = MovieFallback(play="movie/uta/titjob/1.webm", image="movie/uta/titjob/img.webp", character="uta")
image movie_uta_titjob fast = MovieFallback(play="movie/uta/titjob/2.webm", image="movie/uta/titjob/img.webp", character="uta")
image movie_uta_titjob cum  = MovieFallback(play="movie/uta/titjob/3.webm", image="movie/uta/titjob/img.webp", character="uta")

image uta_titjob_cum = "movie/uta/titjob/cum.webp"

label event_uta_titjob:
    if uta_titjob == 0:
        player "[uta.n], lately I feel like there's something different between us..."
        player "We don't just talk or spend time together... there's something more, isn't there?"
        show uta c1 shame with dissolve
        uta "I... I've felt it too. Every time I look at you, my heart races..."
        player "Hahah. You blush every time I get close."
        uta "T-That's not true!..."
        pause 1.0 
        uta "Maybe a little..."
        player "Hahaha... Maybe it's time to just let things flow. Without overthinking it."
        uta "You really don't know when to stop teasing, do you?"
        player "Not when you react like that. I like seeing you flustered."
        show uta c1 happy with dissolve
        uta "I don't know if I should, but... with you, I feel safe."
        player "Then trust that. Trust what you feel right now."
        uta "Alright... tell me what you want me to do."
        player "Just listen to my voice, and let yourself go. The rest will come naturally."

    else:
        player "Every day you're more attractive and sexy, [uta.n]..."
        player "Since we're here, why don't we repeat what we did last time..."
        player "Just listen to my voice, and let yourself go. The rest will come naturally."


    window hide
    call uta_check pass (check_love = 20, check_lust = 20) from _uta_check_titjob
    show uta neutral with Dissolve(0.4)
    
    $ uta_titjob += 1

    pause 0.5
    show uta neutral c1_underwear with dissolve
    pause 0.5
    show uta neutral c1_naked with dissolve
    window auto

    uta "Don't just stand there doing nothing [player.n]... I'm really nervous..."
    uta "Tell me what to do..."


    window hide
    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "titjob_1" loop
    show movie_uta_titjob slow
    
    window auto
    hide screen screen_black with Dissolve(0.8)

    pause 2
    uta "([player.n]'s body is so close... I can feel his warmth against my skin.)"
    pause 0.5
    uta "(His cock... thick, veined, massive...)"
    uta "(Every movement leaves me breathless... everything feels so intense.)"
    uta "(My breathing quickens... my heart won't listen, it's pounding so hard...)"
    uta "My breasts... they're so sensitive... Your cock is so heavy between them..."
    player "These tits... fuck... They are perfect!!"

    pause 0.5

    jump event_uta_titjob_slow

label event_uta_titjob_slow:
    window hide
    window auto
    show movie_uta_titjob slow

    pause 1.0
    uta "(The warmth between us surrounds me, burns me... and yet I don't want to move away.)"
    uta "(I've never felt anything like this before... a mix of nerves and desire that completely disarms me.)"
    uta "(I want to remember every second... his gaze, his breath, the way time seems to stop and his body trembles.)"
    uta "Just relax and enjoy yourself okay?"
    player "Wow, it feels so good, you're doing it perfectly!"
    uta "You prefer it faster my love ??"

    pause 1.0

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_uta_titjob slow
            pause
            jump event_uta_titjob_slow

        "Faster":
            jump event_uta_titjob_fast
    

label event_uta_titjob_fast:
    window hide
    window auto
    show movie_uta_titjob fast

    pause 3.0
    uta "It's so hot... your head's is so near... pressing against my face..."
    pause 1.0
    player "Yeesss so hot... I can't get enough of these massive tits..."
    uta "[player.n] is fucking my tits... my heart's pounding... I'm so happy..."
    uta "I'd like to try this beautiful cock of yours..."
    uta "Hah... I'll love y-you taste... so strong... ngh"
    pause 1.0

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_uta_titjob_slow

        "Keep going":
            show movie_uta_titjob fast
            pause
            jump event_uta_titjob_fast

        "Cum":
            jump event_uta_titjob_cum


label event_uta_titjob_cum:

    show movie_uta_titjob cum

    uta "More... more [player.n]... my body's already melting... i wont last..."
    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    show uta_titjob_cum at vibration  with flash
    hide movie_uta_titjob

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    #stop gems
    with flash
    pause 0.2
    with flash
    pause 2.0
    uta "Hey... easy there, haha."
    player "Fuck... So good..."
    uta "You really don't hold back, do you?"
    uta "It's... warm, and kind of ticklish..."
    uta "You always surprise me with how intense you can be."
    uta "Looks like you enjoyed it, [player.n]."
    uta "What a little mess we made..."
    uta "Don't worry, I'll help you clean up, okay?"
    
    window hide
    window auto
    pause 1.0
    jump event_uta_titjob_end


label event_uta_titjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    stop gems
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_uta_titjob
    hide uta_titjob_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show uta happy with dissolve
    
    uta "I don't think I've ever felt this relaxed before..."
    player "Me neither... it feels like the whole world stopped for a while."
    uta "I liked that... just being close to you."
    player "Then let's stay like this a little longer."
    uta "Mm... yes, just a little longer... before reality comes back."

    $ uta_lust += 2
    $ uta_love += 2
    narrador "[uta.n] Lust +2 and Love +2" 

    window hide
    show uta c1_underwear with dissolve
    pause 0.2
    show uta c1 with dissolve

    jump uta_bye