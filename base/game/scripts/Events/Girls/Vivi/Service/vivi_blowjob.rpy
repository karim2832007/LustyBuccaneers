# Version event: 3
# Version game: 0.35

default vivi_blowjob = 0

label vivi_blowjob:

    if vivi_blowjob == 0:
       
        player "How are you, [vivi.n]?... Lately, I feel like you've lost all the shyness and embarrassment you had with me..." 
        player "I feel like you really trust me now."
        show vivi c1 shame with dissolve        
        vivi "It's all thanks to you, [player.n]..."
        vivi "You make me feel so good here... I'm glad to be part of your crew."
        player "You make me feel so good too..."
        player "Every time we talk, I feel a warmth between us... something that keeps growing."
        vivi "I feel it too... it's strange but exciting at the same time."
        player "You've changed a lot, [vivi.n]... you're more confident, more radiant than ever."
        vivi "Maybe being by your side gives me that confidence..."
        player "Then maybe I can ask for a small favor, to ease my tension after such a long day..."
        vivi "What is it?! Tell me... I would do anything for you."
        player "Kneel down, [vivi.n]... I'll tell you exactly what to do. You'll help me relax, and maybe you'll end up enjoying it too..."
        vivi "Mmm... you always find ways to surprise me, [player.n]..."


    else:
        player "How are you [vivi.n]?? ... what do you think if we have a new session like the last time..."
        player "We're really starting to enjoy spending time together!"
        show vivi c1 shame with dissolve  
        vivi "That sounds pretty good, i feel like this time i'll be able to do even better..."
        player "I have no doubt about that, now get on your knees [vivi.n], be a good girl..."


    call vivi_check pass (check_love = 15, check_lust = 15) from _lewd_vivi_check_blowjob
           
    $ vivi_blowjob += 1

    show vivi neutral with dissolve
    window hide
    window auto
    pause 0.4

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
    vivi "I don't have much experience in this... But I trust you, tell me what to do [player.n]"
    
    hide screen screen_black onlayer master with Dissolve(0.8)

    pause 1.0

    player "You're doing perfectly well [vivi.n], keep it up!"   
    vivi "This is a real... a real cock... So close to my face..."
    player "And what do you think, do you like it?"  
    vivi "You are super hard... plus, what a strong smell!!"
    vivi "(It's turning me on)"
    vivi "..."
    player "Hahah I'm sure you'll like it over time, keep it up..."  

    jump event_ar_vivi_blowjob_slow