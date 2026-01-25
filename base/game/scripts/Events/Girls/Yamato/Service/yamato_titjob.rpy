# Version event: 2
# Version game: 0.12

default yamato_titjob = 0

label event_yamato_titjob:

    if yamato_titjob == 0:
        player "[yamato.n] I'm going to steal some of your time again!"
        player "What do you think about training the chest area today?!"
        yamato "You really want to work chest today, Captain? I know several exercises!"
        player "This one in particular, I'm not sure if you know it, but with me it's going to be different!"
        show yamato c1 happy with dissolve
        yamato "Hahaha, I see where this is going!... I love those kinds of exercises, But i don't know..."

    else:
        yamato "Do you want to repeat, Captain?"
        yamato "I've been waiting for you...I need a new session right now!"
        
        
    call lewd_yamato_check pass (check_love = 35, check_lust = 35) from _lewd_yamato_check_titjob
           
    $ yamato_titjob += 1

    pause 1.0
    window hide
    show yamato neutral c1_naked with dissolve

    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events yamato titjob yamato_titjob_1 at vibration
    hide screen screen_black with Dissolve(0.8)

    pause 3.0
    window hide
    pause 0.8
    window auto

    yamato "Niiice cock Captain... I love it!"
    player "[yamato.n], these tits... They are amazing!"
    yamato "What a strange sensation to feel your dick between my boobs Captain!!"
    yamato "Oh god! It's sooo big!"
    yamato "It's even harder than before..."    
    player  "It feels good, right? I love it too!!"
    yamato "That should be my line, Captain, hahaha!"    
    yamato "The feeling of putting it between breaasts!!!"
    yamato "Tell me?!? Does it feel good to get squeezed by my well-trained boobs?"
    player "[yamato.n]'s boobs.... Feels really really good... "   
    
    window hide
    window auto
    show screen screen_black with Dissolve(0.8)
    show events yamato titjob yamato_titjob_2
    hide screen screen_black with Dissolve(0.8)
    play gems "gem_02"

    show events yamato titjob yamato_titjob_2 at vibration with vpunch
    
    pause 2.0
    yamato "Can you feel my heart beating??"
    yamato "The lewd sounds of your big hard cock sliding between my breasts?!?"
    yamato "Just enyoing every inch of you..."
    yamato "It's a good workout, I like it!!"   
    yamato "Let me finish you offf okay?"
    yamato "Don't hold back!! let it all out!!"


    window hide
    pause 1.0
    window auto

    show events yamato titjob yamato_titjob_2 at truecenter

    play sound "titjob_1" fadein 0.5 loop

    show events yamato titjob yamato_titjob_2:
        xalign 0.5 yalign 0.0 zoom 1.02
        linear 0.45 zoom 1.12 yalign 0.8
        ease 0.3 zoom 1.02 yalign 0.0
        repeat
    
    pause 3
    player "Shit the way you're rubbing... It feels amazing... "   
    yamato "Ready to cum yet? Just relax and enjoy yourself okay?!!"
    player "Guhhh fuuuck!"   
    player "I can't hold back any more..."
    yamato "yeeeeess cum!!! Cuuuum for me!!"

    window hide
    pause 0.5
    window auto

    
    play sound "cum_01"
    show events yamato titjob yamato_titjob_3 with flash
    show events yamato titjob yamato_titjob_3 at vibration with vpunch
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    
    yamato "Ahahh you let out a lot!!"
    yamato "It's hot, captain's semen is really thick!!"
    pause 0.2
    yamato "Sooo full of energy, I love your dick Captain!!"
    yamato "I already received my vitamins for the day, thank you very much captain!!"
    yamato "Now that I've had my protein, I can train peacefully!"
    yamato "Let me know if you want a second round, Captain!!!"

    pause 3.0

    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events yamato doggystyle
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()


    show yamato happy with dissolve

    $ yamato_lust += 2
    $ yamato_love += 2
    narrador "[yamato.n] Lust +2 and Love +2" 

    window hide
    show yamato c1 with dissolve
    hide yamato with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location
