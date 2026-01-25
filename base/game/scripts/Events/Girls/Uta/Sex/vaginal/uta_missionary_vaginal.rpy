# Version event: 7
# Version game: 0.33

default uta_missionary = 0

image movie_uta_missionary slow = MovieFallback(play="movie/uta/missionary/vaginal/1.webm", image="movie/uta/missionary/vaginal/img.webp", character="uta")
image movie_uta_missionary fast = MovieFallback(play="movie/uta/missionary/vaginal/2.webm", image="movie/uta/missionary/vaginal/img.webp", character="uta")
image movie_uta_missionary cum  = MovieFallback(play="movie/uta/missionary/vaginal/3.webm", image="movie/uta/missionary/vaginal/img.webp", character="uta")

image uta_missionary_cum_in = "movie/uta/missionary/vaginal/cum_in.webp"
image uta_missionary_cum_out = "movie/uta/missionary/vaginal/cum_out.webp"

label event_uta_missionary_vaginal:

    if uta_missionary == 0:
        
        player "[uta.n]... you're very quiet today, you look a little nervous."
        show uta shame with dissolve
        uta "[player.n]... why are you looking at me like that?!?"
        uta "It's just that I'm nervous, I've never been in a situation like this before..."
        player "You don't have to be afraid. You're incredible, and I want you to always remember that."
        uta "You say it with such confidence... you make me feel special."
        player "(Her hands are trembling... I should be gentle.)"
        player "There's no rush. We can discover each other little by little, at our own pace."
        uta "That sounds... beautiful. I've never shared something so intimate."
        uta "I spent so much time alone, focused on my music... that I forgot what it feels like to have someone close."
        uta "I certainly never had a relationship this close... It's all so strange"
        player "Well, you're not alone now. Tonight is just for us."
        uta "Your words... make me feel calm"
        player "And the way you look at me makes me want to take care of you even more. If there's anything you don't like, tell me and we'll stop."
        uta "I trust you [player.n]... more than I thought possible."
        player "(Her eyes... are full of truth.)"
        player "May I come a little closer?"
        uta "Yes... come closer, please."
        show uta happy with dissolve
        uta "Your embrace... fills me with warmth. I've never felt so safe."
        player "I want you to always remember this moment, with a smile."
        uta "And what if I don't know what to do...?"
        player "You don't have to know anything. Just let yourself go, I'll be with you."
        show uta shame with dissolve
        uta "If it's with you... I want to take this step."
        player "[uta.n], I need to hear it from you... do you want this with me, tonight?"
        uta "Yes... I do. I want to give myself to you."
        player "Then it will be slow, gentle... together."
        uta "Together."



    else:
        uta "[player.n]!! I've been waiting for you..."
        uta "Since the last time... I'll love to repet!"
        uta "Make me yours!!!"

    window hide
    call uta_check pass (check_love = 25, check_lust = 25) from _uta_check_missionary
    show uta neutral with Dissolve(0.4)
           
    $ uta_missionary += 1

    pause 0.5
    show uta neutral c1_underwear with dissolve
    pause 0.5
    show uta neutral c1_naked with dissolve
    window auto

    uta "Tell me what to do...."
    uta "Don't make me wait like this!"
    uta "I'm very anxious, Make me yours!"
    player "Come to bed, I'll take care of the rest..."

    window hide
    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    play gems ["<silence 0.8>","gem_02","<silence 0.8>"] loop
    #play sound "titjob_1" loop
    show movie_uta_missionary slow
    
    window auto
    hide screen screen_black with Dissolve(0.8)

    pause 2
    uta "Nnh... h-hahh... I'am leaking..."
    uta "I'm a mess... I can't hide it anymore..."
    uta "Looks like we're finally having sex... we can't just be friends anymore, can you hear me?"
    player "Of course not [uta.n], you are excellent!"

    pause 0.5
    uta "(It hurts so much... I can't breathe... but my head is going blank... Ah...)"
    uta "(Oh God, this is insane... Are you telling me that sex is this amazing?)"
    uta "(My body's screaming for it... begging for more...)"
    uta "(I'm gonna cum again... just like before... oh God, I'm gonna cum... I'm gonna...)"

    uta "Shiiiiiit sooo good [player.n]"
    uta "You're being so rough!"
    player "Do you want me to stop?"
    uta "No...{size=40} NO!!{/size}"
    uta "Please... Keep fucking me like that!"
    uta "It feels sooo good!"

    jump event_uta_missionary_vaginal_slow

label event_uta_missionary_vaginal_slow:
    window hide
    window auto
    show movie_uta_missionary slow

    pause 1.0
    uta "Your cock is such a perfect fit for my pussy!"
    uta "Mnmnm... [player.n]... your cock's so fucking big... stretching me so deep..."
    uta "You feel that? My pussy's sucking you in... like it never wants to let go..."
    uta "Shit—every thrust's hitting that spot... fuck, I can't stop clenching around you."
    uta "Nghh... [player.n]... more—deeper—don't stop!"
    uta "I want it all, every inch; slam it into me till I forget everything!"
    uta "Don't you fucking dare stop—fill me, [player.n]—make me overflow!"
    uta "{size=40}Fuck me faster, please{/size}!!!"


    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_uta_missionary slow
            pause
            jump event_uta_missionary_vaginal_slow

        "Faster":
            jump event_uta_missionary_vaginal_fast
    

label event_uta_missionary_vaginal_fast:
    window hide
    window auto
    show movie_uta_missionary fast

    pause 1.0
    uta "So... good... mmmm... deeper..."
    uta "Fuck me... {size=40}harder{/size}... ahh..."

    uta "I... love... it!"
    uta "{size=40}Use me!!!{/size}"    
    uta "Make me yours!!!"
    pause 4.0
    uta "Omg... Omgg!!!!... Yes... {size=40}I'm close again!!!{/size}"
    uta "I need more! Pleeeeeaseeee a litle more..."
    player "Fuuuuck... I can't take it anymore!!!"
    uta "Yes... I want to feel your cum deep inside of me!"
    uta "{size=40}Cum with mee my love!{/size}"
    pause 1.0

    window hide
    window auto
    pause 1.0

    menu:
        "Slower":
            jump event_uta_missionary_vaginal_slow

        "Keep going":
            show movie_uta_missionary fast
            pause
            jump event_uta_missionary_vaginal_fast

        "Cum":
            jump event_uta_missionary_vaginal_cum


label event_uta_missionary_vaginal_cum:
    #player "(Fuuck... I'm reaching my limit...She do it so well!)"

    menu:
        "Cum inside":
            jump event_uta_missionary_vaginal_cum_inside

        "Cum outside":
            jump event_uta_missionary_vaginal_cum_outside


label event_uta_missionary_vaginal_cum_inside:

    show movie_uta_missionary cum

    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    play gems "gem_01"
    player "Fuuuuck... Take it all!!!"
    show uta_missionary_cum_in at vibration  with flash
    hide movie_uta_missionary

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    #stop gems
    with flash
    pause 0.2
    with flash
    pause 2.0
    uta "Mnmnm... fuck... I can feel you dripping out of me..." 
    uta "So warm... still twitching inside me..." 
    uta "(I never imagined it would be like this...)"
    pause 0.5 
    uta "My legs... They're gone... I'm stuck, cumming again..." 
    uta "I'm trembling... it's messy... but I can't stop feeling so good..."
    uta "You really filled me up, huh?"
    uta "I love it!!"

    window hide
    pause 0.5 
    window auto
    pause 1.0
    jump event_uta_missionary_vaginal_end


label event_uta_missionary_vaginal_cum_outside:

    show movie_uta_missionary cum

    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    play gems "gem_01"
    player "Fuuuuck... Take it all!!!"
    show uta_missionary_cum_out at vibration  with flash
    hide movie_uta_missionary

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    #stop gems
    with flash
    pause 0.2
    with flash
    pause 2.0
    uta "Ahhh... it's everywhere... so hot... all over my chest..."
    uta "It's running down my sides... I'm so sticky..."
    uta "(Every breath makes my chest feel even hotter...)"
    player "So hot... You are beautiful [uta.n]..."    
    uta "My heart's racing... I can't calm down..."
    uta "It's dripping down... sticky and warm... I can barely breathe..."
    pause 0.5
    uta "My skin's burning... my whole body feels like fire..."
    uta "So much... you covered me completely..."
    uta "Having my chest this warm... This must be love..."

    
    window hide
    pause 0.5 
    window auto
    pause 1.0
    jump event_uta_missionary_vaginal_end


label event_uta_missionary_vaginal_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    stop gems
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_uta_missionary
    hide uta_missionary_cum_in
    hide uta_missionary_cum_out
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show uta happy with dissolve
    
    player "Wow so intense [uta.n]..."
    show uta happy with dissolve
    uta "That was really good!!"
    show uta shame with dissolve
    uta "I had a great time [player.n], I love you!"

    $ uta_lust += 2
    $ uta_love += 2
    narrador "[uta.n] Lust +2 and Love +2" 

    window hide
    show uta c1_underwear with dissolve
    pause 0.2
    show uta c1 with dissolve

    #jump uta_bye

    window hide
    hide uta with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location