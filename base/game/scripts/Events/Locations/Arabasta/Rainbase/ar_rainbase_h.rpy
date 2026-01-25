# Version event: 3
# Version game: 0.31

label ar_rainbase_h():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = False
    $ game.location = "ar_rainbase_vip"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()

    nami "Well, here we are... The VIP lounge."  
    robin "How strange, there's no one guarding the entrance again... Nothing is stopping us from going in..."  
    player "We can't worry about that now, we have to go in and find [crocodile.n]."  


    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ar_rainbase_vip_in"
    scene BG locations
    hide screen screen_black with Dissolve(0.3)
    window auto
    
    vivi "Now what do we do? The path splits into two."  

    nami "The VIP path goes to the left, and the right one is for... pirates?!?!"  

    player "(Mmm, I'm a pirate, so we should go right then...)"  
    player "(But the VIP lounge is surely full of beautiful women!)"  
    player "(No doubt about it! The decision is obvious!)"  
    player "Let's go down the VIP path!!"  

    robin "Good thinking, captain. The right path seems like a very obvious trap..."  
    nami "No one would be stupid enough to fall for such a trap, [robin.n]..."
    player "Hahahe that's exactly what I thought!"    

    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ar_rainbase_stairs"
    scene BG locations
    hide screen screen_black with Dissolve(0.3)
    window auto

    narrador "After several minutes of walking, you arrive at a staircase leading downward." 

    nami "Should we go down?"  
    vivi "Quiet, I hear a voice coming from below..."  
    robin "It would be best to carefully observe what's happening before getting involved."  
    yamato "Right, the element of surprise is important..."

    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ar_rainbase_jail_pell"
    scene BG locations

    show crocodile:
        xalign 1.0
        yalign 1.0
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #MAYBE BOSS MUSIC HERE O DARK MUSIC ej cap 107 min 19:30

    crocodile "Ha ha ha, filthy rat, did you really think you could stop me?"  
    crocodile "Or should I say... filthy eagle..."  
    crocodile "What was your mission here? Were you sent to scout the enemy?"  
    crocodile "It seems you placed too much trust in your ability... You overestimate yourself!"  
    crocodile "Confidence, hahaha, that's the most useless thing in this world."  

    unknown "You may have me imprisoned, but you will never conquer [Arabasta.n]!"  

    crocodile "Conquer [Arabasta.n]?? Is that really what you think I want... You are truly lost..."  
    crocodile "Years without suspicion of me... And suddenly, you come to infiltrate my casino..."  
    crocodile "It seems the king managed to gather some valuable information... But it's too late..."  
    crocodile "Hahaha, my plan is already in motion..."  
    crocodile "Operation Utopia is about to begin!"  

    unknown "Operation Utopia?!?"  

    crocodile "I suppose I can tell you... You'll die here anyway..."  
    crocodile "It will be the end of this pathetic kingdom."  
    crocodile "I will erase [Arabasta.n] from the face of the earth!"  
    crocodile "All its inhabitants will sink into eternal darkness."  
    crocodile "Hahahaha!"  

    unknown "What do you want?!? What are you planning to do to the kingdom of [Arabasta.n]!?!"  

    crocodile "By now, the King must have already been captured..."  

    unknown "You want to kill the King?"  

    crocodile "At this moment, I don't intend to kill him — he's not worth it."  
    crocodile "I will make him suffer a humiliation far crueler than death itself..."  

    unknown "If you don't want to kill him, then what is the purpose of your operation?!?"  

    crocodile "Even though you're about to die, there's no need to tell you the details... I won't waste any more time..."  
    crocodile "But the people's respect for the King will be lost."  
    crocodile "And with that, the rebel army will attack the palace, hahaha."  
    crocodile "Everyone will think they are protecting the kingdom of [Arabasta.n], but they will only lead it to its self-destruction, hahaha."  

    unknown "Why are you doing all this?"

    crocodile "I had to do a lot to make this day happen."  
    crocodile "The shipments of Dance Powder, redirecting the rebel army, the King's abduction..."  
    crocodile "Everything that has happened was planned in detail!"  

    unknown "I'll get out of here and kill you first!"  

    crocodile "Hahaha, remember that this cage is made of Kairōseki, how will you escape?"  
    crocodile "To do that, you'd need to get the key... But I already fed it to my pet!"  
    crocodile "But don't worry, soon enough you'll reunite with that key when he eats you too, hahaha!"  
    crocodile "Well, it's late... I still have a lot to do in Alubarna."  
    crocodile "I want to get there in time and enjoy the spectacle!"

    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ar_rainbase_casino_exit"
    scene BG locations
    hide crocodile
    hide screen screen_black with Dissolve(0.3)
    window auto

    unknown "I will kill you!"

    crocodile "Hahaha"

    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ar_rainbase_jail_pell"
    scene BG locations
    hide crocodile
    hide screen screen_black with Dissolve(0.3)
    window auto

    show vivi anger with dissolve:
        xzoom -1.0
        xalign 0.15
        yalign 1.0

    player "That bastard is [crocodile.n]?"  

    vivi "Yes, he is Mr. 0, the leader of Baroque Works... The one behind everything, it's clear after what we heard!"  
    vivi "I know our goal is to stop him, but first, we need to save that man."
    show vivi serious with Dissolve(0.2)
    vivi "With his help, we could communicate with the entire kingdom easily, and we'd have the advantage..."  
    vivi "That man is [pell.n], one of the two royal guards."  
    vivi "He's considered one of the strongest warriors of [Arabasta.n]."  
    vivi "And he is a Devil Fruit user!"  
    vivi "Not only would he be extremely useful in battle, but I also care about him... He's important to me!"  

    player "I understand. It's decided then... We'll get him out of there first!"  

    nami "Sorry to interrupt... But what is that?!?"  

    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ar_rainbase_room"
    scene BG locations
    show expression enemy_bananawani.image:
        xalign 0.5
        yalign 0.5
    hide screen screen_black with Dissolve(0.3)
    window auto

    vivi "It's a Bananawani, it must be the pet [crocodile.n] was talking about!!"  
    vivi "They're very dangerous, they can even devour a Sea King!"  

    robin "We need to get that key it swallowed if we want to free [pell.n] from there!"  

    player "Leave it to me, don't worry!"  

    hide vivi

    call fight_start pass (enemy_pass = enemy_bananawani, no_run = True, no_interface = True) from _fight_ar_rainbase_h
    
    hide expression enemy_bananawani.image with dissolve

    $ music_arabasta()

    nami "Well done Capitan!!"

    $ robin_love += 1
    $ nami_love += 1
    $ yamato_love += 1
    $ vivi_love += 1
    narrador "[robin.n], [yamato.n], [nami.n] and [vivi.n] Love +1"

    nami "Look over there! The Bananawani just spat out the key!"  
    vivi "Let's free [pell.n] as soon as possible!"

    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ar_rainbase_jail"
    scene BG locations

    show vivi:
        xzoom -1.0
        xalign 0.15
        yalign 1.0

    show pell:
        xalign 0.85
        yalign 1.0
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    pause 0.4
    pell "Princess [vivi.n], I'm so glad to see you safe and sound!!"  
    pell "Thank you so much for saving me!!"  

    vivi "The kingdom needs you, [pell.n]!"  
    vivi "We heard all of [crocodile.n]'s plan."  
    vivi "Go quickly to Alubarna, meet up with Chaka, and find the king!"  
    vivi "We'll go after [crocodile.n]!"  

    pell "Understood, take care, Princess. We will meet again!!"

    hide pell with Dissolve(0.3)

    narrador "[pell.n] transformed into a falcon and quickly flew away."  

    player "Wow, he turned into a falcon and flew off, AMAZING!"
    show vivi serious with Dissolve(0.5)
    vivi "It's something incredible to see the first time... But we don't have time to waste being amazed..."  
    player "You're right! Let's catch up to [crocodile.n] and stop him! We will save [Arabasta.n]!"


    if not ar_rebel_army:
        player "(Maybe there's still time to reveal the truth to the rebel army!)"  
        player "(If we head to Alubarna now, there will be no turning back...)"  
        player "(On one hand, with their help, it might be easier to face [crocodile.n]...)"  
        player "(Though defeating him alone without help would surely impress [vivi.n]...)"  
        player "(With or without help, I will stop [crocodile.n] no matter what!!)"  



    $ game.clock.next(increment = 5)
    $ Arabasta.h = 13
    pause 0.1
    $ ui_interface = True


    $ sleep_event = "event_ar_vivi_blowjob"

    jump ar_rainbase
    
