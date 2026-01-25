# Version event: 2
# Version game: 0.13

#default alvida_cowgirl = 0

label event_alvida_cowgirl:

    player "I will teach you to respect me!"
    player "Take off your clothes and get on all fours on the bed!"
    alvida "What? You can't be serious..."
    alvida "You're just a small-time pirate! Who do you think you are!?!"
    player "I'm not giving you an option, [alvida.n]. Do as I say..."
    player "You're on my ship now... You have no power here!"
    alvida "I can't believe this is happening..."
    player "Now, move. I don't have all day..."
    player "I warn you... you don't want to see me angry."
    alvida "Fine... I'll do as you say... But don't think I'll forget this!!"
    player "You're right, you'll never forget... my cock!"

    pause 1.0
    window hide
    show alvida neutral c1_naked with dissolve
    pause 0.3

    player "That's it, just the way I like it. Good girl."
    alvida "Let's end this!"    
    player "I like what I see...Now you're the one who's eager."
    alvida "..."
    alvida "I can't believe it...."
    alvida "Big talk, but I bet you won't last a second..."
    player "Hahaha... you'll see!"
    player "Now to bed..."


    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events alvida vaginal cowgirl alvida_cowgirl_1 at vibration 
    play gems "nami_gem_1"
    hide screen screen_black with Dissolve(0.8)
    pause 2.5
    window hide
    pause 0.8
    window auto

    alvida "Ahnnnn ahnnnn no way so rough..."
    alvida "(Is sooo fat, and stupidly big... Even just getting it put in made me cum...)"
    alvida "(Only the tip is in but... If it went alll the way in to my deepest parts...)"
    play sound "cum_01"
    alvida "Mnnnnmng... Mngngng..."
    player "You pirate slut"
    player "I've realized how much you like it... You can't deny it..."
    player "We haven't even started..."
    alvida "(I can't agree with him... As much as I like it, I just can't give in...)"
    alvida "(At this rate i will be used and throw away, I will be subdued and raped...)"
    player "Deep down, you want to be treated like a cheap slut right?"
    alvida "(I wanna move... I wanna feell even better!!)"
    alvida "(It's uselessss... I love this, I love cocks...)"
    player "Heheh take this then!!"

    play gems "gem_02"


    window hide
    window auto 

    play gems "nami_gem_2"
    show events alvida vaginal cowgirl alvida_cowgirl_2 at vibration with vpunch
    
    pause 3.0
    play gems "gem_02"
    alvida "(I can't stop bucking my hips...)"
    player "The pirate [alvida.n] is actually a masochist whore!!"
    alvida "You're crushing my womb!!"
    alvida "I came... Caaamee..."

    window hide
    window auto

    # Disable vibration
    show events alvida vaginal cowgirl alvida_cowgirl_2 at truecenter

    play sound "nami_cowgirl_1" fadein 0.5 loop

    show events alvida vaginal cowgirl alvida_cowgirl_2:
        xalign 0.5 yalign 0.0 zoom 1.02
        linear 0.25 zoom 1.09 yalign 0.1
        ease 0.2 zoom 1.02 yalign 0.0
        repeat

    pause 3.0
    alvida "S-sstop right now... I'am not your plaything and I dont fell good at all hnggg..."
    alvida "Y-your disgusting stinky cock is the worst"
    player "Hahaha you cant even lie properly..."
    player "And who allows you to talk back!!"
    player "You have no right to talk!!"
    alvida "I-iam sorry I... I lied your big burly cock made me come, Captain-sama"
    alvida "Amazing! i can't hold it any-more!"
    alvida "It's reaching my wombb...."
    alvida "I'm cuming i'm cuming againgg!!!"

    window hide
    pause 0.5
    window auto

    show events alvida vaginal cowgirl alvida_cowgirl_2_cum at vibration with vpunch
    play sound "cum_01"
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    play gems ["<silence 0.1>","nami_gem_5","<silence 0.3>","nami_gem_6","<silence 0.3>","nami_gem_3","<silence 0.2>","nami_gem_end_1"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    alvida "I'm cuming... i'm cuming..."   
    player "Fuuuuckkk..."

    alvida "Tou're shoo haaarddd..."
    alvida "Feels sooo goood... I-I'm breakinggg"  
    alvida "Cock... shooo guuuddd..."    

    window hide
    window auto

    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events alvida doggystyle
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    player "Get out of here... We'll meet again..."
    alvida "(Damn fourth-rate pirate... This isn't over!!)" 

    window hide
    show alvida c1 with dissolve
    hide alvida with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location
