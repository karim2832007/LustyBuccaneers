# Version event: 4
# Version game: 0.12

default robin_titjob = 0

label robin_titjob:

    if robin_titjob == 0:

        player "[robin.n] I'm going to steal some of your time again!"
        robin "I don't mind at all... What's going on?"
        player "I would love to use your tits for an experiment... What do you think?"
        show robin c1 shame with dissolve
        robin "Hahah... I love those kinds of experiments... But i don't know..."

    else:
        robin "Do you want to repeat, Captain?"
        robin "Surely you took note of the previous opportunity..."
        

    call lewd_robin_check pass (check_love = 35, check_lust = 35) from _lewd_robin_check_titjob
           
    $ robin_titjob += 1

    pause 1.0
    window hide
    show robin neutral c1_naked with dissolve

    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events robin titjob robin_titjob_1 at vibration
    hide screen screen_black with Dissolve(0.8)

    pause 3.0
    window hide
    pause 0.8
    window auto

    robin "Finally!!!... Your dick is between my boobs Captain!!"    
    player "Your bare tits, they are so, damn huge.... Fuck..."
    robin "It feels good, right? I love it too!!"
    robin "The feeling of putting it between breaasts!!!"
    robin "Tell me?!? Does it feel good to get squeezed by my boobs?"
    player "[robin.n]'s boobs.... Feels really good... "   
    
    window hide
    window auto
    show screen screen_black with Dissolve(0.8)
    show events robin titjob robin_titjob_2
    hide screen screen_black with Dissolve(0.8)
    play gems "gem_02"

    show events robin titjob robin_titjob_2 at vibration with vpunch
    
    pause 2.0
    robin "Can you feel my heart beating??"
    robin "The lewd sounds of your big hard cock sliding between my breasts?!?"
    player "I'll be sure to violate them properly"
    robin "You can defile them as much as you want!!!"   
    robin "Let me finish you offf okay?"
    robin "Don't hold back!! let it all out!!"

    window hide
    pause 1.0
    window auto

    show events robin titjob robin_titjob_2 at truecenter

    play sound "titjob_1" fadein 0.5 loop

    show events robin titjob robin_titjob_2:
        xalign 0.5 yalign 0.0 zoom 1.02
        linear 0.45 zoom 1.12 yalign 0.8
        ease 0.3 zoom 1.02 yalign 0.0
        repeat
    
    pause 3


    window hide
    pause 0.5
    window auto

    
    play sound "cum_01"
    show events robin titjob robin_titjob_3 with flash
    show events robin titjob robin_titjob_3 at vibration with vpunch
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    robin "Wow it's shooting so much!!!"
    robin "Ahahh you let out a lot"
    robin "It's hot, captain's semen is all bubbly, look... it's really thick"
    robin "So full of energy you caught me off guard there..."
    robin "I already received my vitamins for the day, thank you very much captain!!"
    pause 3.0

    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events robin doggystyle
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()


    show robin happy with dissolve

    $ robin_lust += 2
    $ robin_love += 2
    narrador "[robin.n] Lust +2 and Love +2" 

    window hide
    show robin c1 with dissolve
    hide robin with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location
