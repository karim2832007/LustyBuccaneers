# Version event: 5
# Version game: 0.35

default vivi_cowgirl = 0

image movie_vivi_cowgirl slow = MovieFallback(play="movie/vivi/cowgirl/1.webm", image="movie/vivi/cowgirl/img.webp", character="vivi")
image movie_vivi_cowgirl fast = MovieFallback(play="movie/vivi/cowgirl/2.webm", image="movie/vivi/cowgirl/img.webp", character="vivi")
image movie_vivi_cowgirl cum  = MovieFallback(play="movie/vivi/cowgirl/3.webm", image="movie/vivi/cowgirl/img.webp", character="vivi")

label event_vivi_cowgirl:

    if vivi_cowgirl == 0:
        player "Every time I see you, [vivi.n], I feel something growing inside me that I can't ignore anymore."
        show vivi c1 shame with dissolve 
        vivi "What are you implying, [player.n]?!?... It's true that I've been feeling very close to you lately..."
        player "You know!... Getting to know each other deeply, seeing you as you truly are, and enjoying ourselves together..."
        player "Let me teach you new things, I'm sure we'll enjoy it together!... What do you say?"
        vivi "You always speak with that confidence of yours... and somehow it makes my heart race."
        player "Haha, then maybe you feel the same way I do..."
        vivi "Maybe I do... or maybe I'm just too curious about what you're planning next."
        player "Then let me show you... slowly, carefully... you'll decide how far we go."
        vivi "You're always so gentle... it's hard to say no when you look at me like that."
        player "Trust me, [vivi.n]... we'll make every moment unforgettable."
        player "So... what do you say? Shall we take that next step together?"


    else:
        player "How are you [vivi.n]?? ... What do you think if we repeat what we did last time?"
        player "We're really starting to enjoy spending time together!"
        player "We had such a great time! Why don't we repeat? What do you say?"
        show vivi c1 shame with dissolve
        vivi "..."
        pause 0.5

    call vivi_check pass (check_love = 30, check_lust = 30) from _vivi_check_cowgirl
    show vivi neutral with dissolve
           
    $ vivi_cowgirl += 1

    pause 1.0
    window hide
    show vivi neutral c1_underwear with dissolve
    pause 0.5
    show vivi neutral c1_naked with dissolve

    vivi "I'm ready [player.n]... I've been waiting for this moment since I met you."
    player "(She is soo sexy!!)"
    vivi "Please be gentle [player.n]..."

    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    #play sound "titjob_1" loop
    show movie_vivi_cowgirl slow

    hide screen screen_black with Dissolve(0.8)

    vivi "Mnmnmngg..."
    player "Wow, looks like we're finally are having sex, huh?!?" 
    player "You don't need to worry about anything, just relax..."
    vivi "([player.n]'s cock is coming.... inside!!)"
    vivi "(Whah ishhh this...?)"
    vivi "(There's a shock through my body...)"
    player "[vivi.n]... Why don't you answer me?!?"
    vivi "(Right there... ahh.... ooohhh it's close...)"    
    vivi "(I want him to go as far as he wants...)"
    vivi "(I want him fill me up...)"
    player "[vivi.n] You just keep moving, but you don't answer me haha!!"
    vivi "(Ohh my god...)"
    vivi "(This feels amazing I fell so refreshed... Serves you right [player.n]...)"
    vivi "(I'm gonna grind all over you and let you soak in my scent)"
    vivi "(I'm sooo excited...)"
    player "[vivi.n]!!!"

    jump event_vivi_cowgirl_slow

#cowgirl
label event_vivi_cowgirl_slow:
    window hide
    window auto
    show movie_vivi_cowgirl slow

    pause 3.0
    #dia rep

    vivi "Oh!!! S-sorry, I was lost in my thoughts..."
    vivi "Tell me what I have to do! I want to feel you better."

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_vivi_cowgirl slow
            pause
            jump event_vivi_cowgirl_slow

        "Faster":
            player "Go faster!!"
            jump event_vivi_cowgirl_fast
    

label event_vivi_cowgirl_fast:
    window hide
    window auto
    show movie_vivi_cowgirl fast

    pause 3.0
    #dia rep
    
    player "That's it! move it more!!"
    player "Go swing your hips like an animal and lust for me more!"
    vivi "Fuuuck..."
    vivi "This grinding is amazing... my belly is tingling!"   
    vivi "Come on, go deepeer until our bodies stick even closer!!!"   
    

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_vivi_cowgirl_slow

        "Keep going":
            show movie_vivi_cowgirl fast
            pause
            jump event_vivi_cowgirl_fast

        "Cum":
            jump event_vivi_cowgirl_cum


label event_vivi_cowgirl_cum:

    show movie_vivi_cowgirl cum

    vivi "Your dick is twitching! are you going to come out?"
    vivi "(Oh no.... I'm gonna cum again... just like before....)"
    vivi "(But i just can't stop moving.... )"
    vivi "(I knew it... I can't live without this!!!)"
    vivi "Oh god.... I'm gonna cum.... I'm gonna... cuuuuuuuuuummm gyaaaa ah ha aaaaa ahh... hooo.."
    
    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    show events vivi cowgirl vivi_cowgirl_cum at vibration  with flash
    hide movie_vivi_cowgirl

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    vivi "(Impregnation... Ejaculation...)"
    vivi "(In my melting uterus... Please...)"
    vivi "Pleaaassshh"
    pause 0.2
    vivi "You're shhhhooting soooo muuuch!!"
    vivi "Caaaaptain's cum... feels... so warm!"
    vivi "What a huge load.... you came sooo much!"

    window hide
    window auto
    pause 1.0
    jump event_vivi_cowgirl_end


label event_vivi_cowgirl_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_vivi_cowgirl
    hide events vivi cowgirl vivi_cowgirl_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show vivi happy with dissolve
    
    vivi "Sorry Captain, I got a little carried away... But I had a great time, I hope we do it again."
    player "What are you saying? You were excellent, I assure you we'll be back!"

    $ vivi_lust += 2
    $ vivi_love += 2
    narrador "[vivi.n] Lust +2 and Love +2" 

    window hide
    show vivi c1_underwear with dissolve
    pause 0.2
    show vivi c1 with dissolve

    #jump vivi_bye

    window hide
    hide vivi with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location