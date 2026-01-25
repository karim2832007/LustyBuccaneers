# Version event: 3
# Version game: 0.24

image movie_ar_vivi_blowjob slow = MovieFallback(play="movie/vivi/ar_blowjob/1.webm", image="movie/vivi/ar_blowjob/img.webp", character="vivi")
image movie_ar_vivi_blowjob fast = MovieFallback(play="movie/vivi/ar_blowjob/2.webm", image="movie/vivi/ar_blowjob/img.webp", character="vivi")
image movie_ar_vivi_blowjob cum  = MovieFallback(play="movie/vivi/ar_blowjob/3.webm", image="movie/vivi/ar_blowjob/img.webp", character="vivi")

label event_ar_vivi_blowjob:

    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ship_captains_cabin"
    scene BG locations:
        blur 3
    hide screen screen_black with Dissolve(0.3)
    window auto

    narrador "Toc Toc Toc!"
    player "Come in!!"

    show vivi serious at center with dissolve        
    vivi "Hello [player.n], sorry for bothering you so early."  

    player "Don't worry, [vivi.n], I was just getting ready..."  

    vivi "About that... I wanted to thank you for everything you're doing for me and for [Arabasta.n]."  
    vivi "It's been quite some time since you rescued me, and now here in my kingdom, you're helping me so much..."  
    vivi "I feel ashamed... You've fought so many battles for me... And now you have to face [crocodile.n]."  
    vivi "Is there anything I can do for you?"  
    vivi "I really owe you a lot!"

    menu:
        "Your gratitude is enough":  
            player "(So many things come to mind that you could do... But I think I should play it safe for now...)"  
            player "Your gratitude is enough for me!"  
            player "We're helping without any hidden motives... There will be time to celebrate later!"  
            show vivi happy with Dissolve(0.5)     
            vivi "Oh really?!"  
            player "Yes, don't worry! We'll have time to relax... Right now, we have an important mission to accomplish!"  
            vivi "I can only thank you for everything you do, I hope I can repay you someday!"  
            player "(I'm sure that day will come!!)"  
            vivi "I'll go now, thank you for everything, [player.n]!! I was really lucky to meet you, I'll leave you be!"  

            $ vivi_love += 3  
            narrador "[vivi.n] Love +3"   
            $ sleep_event = None
            return  

        "I can think of one thing you could do":  
            show vivi neutral at center with dissolve      
            player "If you really want to thank me, I have an idea of how you could..."  
            player "Lately, I have a lot on my mind... All this about [crocodile.n] is causing me stress that I can't seem to shake off..."  
            player "At this age, being a man, I have certain... needs that must be met..."  
            player "I'm sure if I take care of it, I'll be fully prepared for battle!"  
            vivi "What you're saying is completely understandable... The pressure on your shoulders must be immense..."  
            vivi "But I don't understand... How could I help?!?"  
            player "Come, get on your knees, and I'll tell you what to do!"
            show vivi shame with Dissolve(0.5)   
            vivi "W-what?!?"
            player "Come, get on your knees, trust me everything is fine..."  

    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black onlayer master with Dissolve(0.8)
    $ ui_interface = False
    #play sound [ "blowjob_mid_01","<silence 0.2>","blowjob_02","blowjob_03","blowjob_01","<silence 0.2>","blowjob_01"] loop
    play sound "footjob_1" loop
    show movie_ar_vivi_blowjob slow
    
    vivi "We're really going to do this..."
    player "Relax [vivi.n], just relax and start sucking it gently..."
    player "I assure you, that this will do me sooooo soo good..."
    vivi "I've never done this before, it's my first time... But I trust you, tell me what to do [player.n]"

    hide screen screen_black onlayer master with Dissolve(0.8)

    pause 1.0

    player "You're doing perfectly well [vivi.n], keep it up!"   
    vivi "This is my first time having a real... a real cock... So close to my face..."
    player "And what do you think, do you like it?"  
    vivi "You are super hard... plus, what a strong smell!!"
    vivi "(It's turning me on)"
    vivi "..."
    player "Hahah I'm sure you'll like it over time, keep it up..."   


    jump event_ar_vivi_blowjob_slow


label event_ar_vivi_blowjob_slow:
    window hide
    window auto
    show movie_ar_vivi_blowjob slow

    pause 3.0
    
    vivi "How does it feel??" 
    vivi "Does [vivi.n]'s mouth feel good?!?"
    player "I'm in heaven, keep it up!"   


    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_ar_vivi_blowjob slow
            pause
            jump event_ar_vivi_blowjob_slow

        "Faster":
            player "Go faster [vivi.n]!!"
            jump event_ar_vivi_blowjob_fast
    

label event_ar_vivi_blowjob_fast:
    window hide
    window auto
    show movie_ar_vivi_blowjob fast

    pause 3.0
    
    player "Your slippery tongue feels too good!!"
    player "(There's no way i can hold it in!!)"
    vivi "The smells is getting even stronger!!"   
    vivi "I can't stop drooling..."
    vivi "I love this smell..."
    player "(Wow she has loosened up all of a sudden, she's not as shy as before...)"  
    vivi "I can't stop sucking !!"  

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_ar_vivi_blowjob_slow

        "Keep going":
            show movie_ar_vivi_blowjob fast
            pause
            jump event_ar_vivi_blowjob_fast

        "Cum":
            jump event_ar_vivi_blowjob_cum


label event_ar_vivi_blowjob_cum:

    vivi "Your balls are throbbing [player.n]!"
    vivi "They smell like cum...."
    player "(Wow this princess... She's a slut inside... and she's breaking free!!)"
    vivi "Your dick is really really hard, It's convulsing.... As if it's about to cum..."
    vivi "You want to cum now?!?"
    player "Yeaaahhh... Take it alll princess!!"

    show movie_ar_vivi_blowjob cum
    
    window hide
    window auto

    pause 1.0

    play sound "cum_01"
    show events vivi ar_blowjob ar_vivi_blowjob_cum at vibration  with flash
    hide movie_ar_vivi_blowjob

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0
    player "Hoooly shit!"
    vivi "You've come so much..."    
    vivi "I'm still not very good at sucking dick, but i'wll do my best next time!"

    window hide
    window auto
    pause 1.0
    jump event_ar_vivi_blowjob_end


label event_ar_vivi_blowjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_ar_vivi_blowjob
    hide events vivi ar_blowjob ar_vivi_blowjob_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show vivi shame with dissolve
    
    vivi "I hope it has been useful for you [player.n]... I have things to do, I'll say goodbye first!"    

    $ vivi_lust += 3
    $ vivi_love += 1
    narrador "[vivi.n] Lust +3 and Love +1" 

    window hide
    show vivi c1 with dissolve

    window hide
    hide vivi with moveoutright
    pause 0.5
    
    if vivi_blowjob > 0:
        $ game.clock.next()
        jump expression game.location

    else:
        $ sleep_event = None
        return