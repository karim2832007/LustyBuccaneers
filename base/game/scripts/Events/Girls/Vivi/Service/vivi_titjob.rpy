# Version event: 2
# Version game: 0.26

default vivi_titjob = 0


image movie_vivi_titjob slow = MovieFallback(play="movie/vivi/titjob/1.webm", image="movie/vivi/titjob/img.webp", character="vivi")
image movie_vivi_titjob fast = MovieFallback(play="movie/vivi/titjob/2.webm", image="movie/vivi/titjob/img.webp", character="vivi")
image movie_vivi_titjob cum  = MovieFallback(play="movie/vivi/titjob/3.webm", image="movie/vivi/titjob/img.webp", character="vivi")

label event_vivi_titjob:

    if vivi_titjob == 0:
        player "How are you, [vivi.n]?... We're really starting to enjoy spending time together. You know what I mean"
        show vivi c1 shame with dissolve        
        vivi "It's all thanks to you, [player.n]..."
        player "I think that can continue to improve..."
        player "Let's try something new this time!"
        player "Kneel down [vivi.n], I'll tell you what to do... You'll help me relax, maybe you'll even like it..."

    else:
        player "How are you [vivi.n]?? ... what do you think if we have a new session like the last time..."
        player "We're really starting to enjoy spending time together!"
        show vivi c1 shame with dissolve  
        vivi "That sounds pretty good, i feel like this time i'll be able to do even better..."
        player "I have no doubt about that, now get on your knees [vivi.n], be a good princess..."


    call vivi_check pass (check_love = 35, check_lust = 35) from _vivi_check_titjob
    show vivi neutral with dissolve
           
    $ vivi_titjob += 1

    pause 1.0
    window hide
    show vivi neutral c1_naked with dissolve
    pause 1.0
    vivi "I'm ready, tell me what I have to do..."

    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "titjob_1" loop
    show movie_vivi_titjob slow

    hide screen screen_black with Dissolve(0.8)

    pause 1.5

    vivi "You're always sneaking peeks at my boobs, aren't you?"
    vivi "I don't mind if you touch them, you know..."
    vivi "But..."
    vivi "This time... Do you want to splurt your cum... Inbetween my boobs?"

    jump event_vivi_titjob_slow

#titjob
label event_vivi_titjob_slow:
    window hide
    window auto
    show movie_vivi_titjob slow

    pause 3.0
    
    player "Amazing... my cock is completely buried between your boobs..."
    player "It feels like it's glued to me... Damn..."
    player "It's rubbing the back of my dick... It feels soo good..."
    vivi "I'll do it more in the future then..."

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_vivi_titjob slow
            pause
            jump event_vivi_titjob_slow

        "Faster":
            jump event_vivi_titjob_fast
    

label event_vivi_titjob_fast:
    window hide
    window auto
    show movie_vivi_titjob fast

    pause 3.0
    vivi "Ahnn sooo relentless..."
    vivi "[player.n] you look like you're really enjoying it... This is twitching too,"
    vivi "I can see the tip it's twtching nonstop"
    vivi "Are you gonna cum?"

    pause 2.0

    menu:
        "Slower":
            jump event_vivi_titjob_slow

        "Keep going":
            show movie_vivi_titjob fast
            pause
            jump event_vivi_titjob_fast

        "Cum":
            jump event_vivi_titjob_cum


label event_vivi_titjob_cum:
    show movie_vivi_titjob cum

    player "Oh god... [vivi.n] I'm gonna cum!!"
    player "Show me your tongue!!"
    vivi "So take a gooood look..."

    window hide
    window auto

    pause 1.0

    play sound "cum_01"
    show events vivi titjob vivi_titjob_cum at vibration with flash
    
    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    vivi "Mmnmnmnmnm!!!!!"
    vivi "So creamy... Ah, you really are something else."
    vivi "Hahhaha it's still coming out!! Shoot it all out okay..."
    vivi "Just relax... enjoy the feeling of your cum out..."
    vivi "Good boy... Good boy...."

    window hide
    window auto
    pause 1.0
    jump event_vivi_titjob_end


label event_vivi_titjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_vivi_titjob
    hide events vivi titjob vivi_titjob_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show vivi happy with dissolve
    
    vivi "I'll be waiting for the next time"

    $ vivi_lust += 2
    $ vivi_love += 2
    narrador "[vivi.n] Lust +2 and Love +2" 

    window hide
    show vivi c1_underwear with dissolve
    pause 0.2
    show vivi c1 with dissolve

    jump vivi_bye