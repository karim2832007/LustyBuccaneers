# Version event: 3
# Version game: 0.31

label ar_nanohana_h():

    vivi "We finally arrived... This should be the base of the rebel army!"
    nami "Ufff, finally! That was quite a long journey this time..."
    nami "It would be nice to rest a bit... But I don't see much around here..."
    yamato "That's right... There seems to be very little activity for a rebel base..."
    yamato "Are we in the right place?!?"
    vivi "Yes... There's no mistake, this is the place according to the directions my uncle [toto.n] gave me."
    vivi "But I don't see [koza.n], their leader, anywhere..."
    yamato "Look at that guy over there... He looks suspicious, maybe he knows something..."
    vivi "Perfect, we lose nothing by trying."

    vivi "Excuse me, sir, we are looking for a young man we were told would be here... His name is [koza.n]."
    unknown "Mnmnm... I don't know anyone by that name..."
    vivi "(This guy knows something... He's a terrible liar...)"
    player "You're really bad at lying, old man, hahaha... It's obvious you're not telling the truth..."
    unknown "Eh?!? What are you implying?!?"
    vivi "Hahaha, sorry, my friend is just messing around... Please forgive him!"
    vivi "The truth is that [toto.n] sent us from Yuba to find him... We're sure he should be here!"
    unknown "[toto.n]?!?... So that old pervert sent you..."
    vivi "You know him?!..."
    vivi "I need to speak with [koza.n], it's really urgent... Time is running out!"
    unknown "Mnmmn... You seem sincere..."
    unknown "I'm sorry, but the truth is that [koza.n] left not long ago... It looks like there's a problem in Nanohana, something terrible is about to happen..."
    vivi "Nanohana?"
    unknown "According to the reports we received, the king is there!"
    vivi "I am Princess [vivi.n], and I beg you to help me!!"
    unknown "You are... The princess?!?"
    vivi "I have to speak with [koza.n], it's an urgent message!! He needs to know the truth!"
    unknown "It's true now I recognize you... I thought you were missing!"
    unknown "I understand, follow me. We'll ride horses to Nanohana... The road isn't too long from here, but on foot, it would take much longer..."
    unknown "That way, we'll get there as quickly as possible!"
    vivi "Alright, let's go!"
    
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = False
    $ game.location = "ar_nanohana"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    # sound war

    narrador "Upon arriving in Nanohana, chaos is everywhere... The king's army is fighting against the people of Nanohana all over the city..."
    player "What is happening here?!?"

    show yamato serious at center with dissolve
    
    yamato "Things look pretty intense..."
    
    show yamato:
        yalign 1.0
        linear 0.5 xalign 0.10

    show nami serious with dissolve:
        yalign 1.0
        xalign 0.90

    nami "We have to do something, Captain... This can't go on..."

    show nami:
        yalign 1.0
        linear 0.5 xalign 0.90

    show vivi anger at center with dissolve

    vivi "This can't be happening, why is all of this going on?!"
    vivi "Stop! Please, stop!"

    nami "They don't seem to hear you, Vivi. We'd better find the king and [koza.n] as soon as possible!!"
    nami "It might not be too late if we hurry!!"

    yamato "[player.n], look over there! A kid is running away from someone, we should help him!!"

    player "Alright, let's go there. Maybe we'll run into one of them on the way!!"

    nami "Hey, kid! Wait, come here!!"


    window hide
    window auto
    hide nami
    hide vivi
    hide yamato
    with dissolve

    narrador "You follow the child through some city alleys..."

    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ar_nanohana_h"
    scene BG locations:
        blur 3
    hide screen screen_black with Dissolve(0.3)
    window auto


    player "Wait, kid... Can't you hear me?!?"
    player "..."

    #KING
    show cobra c1 with dissolve

    # sound/music dark villan

    unknown "Hahaha, this operation was a success!"

    player "Mnmnm??"
    robin "Wait, Captain, don't reveal yourself... Something is going on, let's stay hidden for now!"

    unknown "Every day, I'm more impressed by my skills... Everyone believed my story!!"
    unknown "Nanohana is in chaos now, the conflict will escalate, and no one will be able to stop it!!"
    unknown "The plan is already in motion!!"
    unknown "And successfully, hahahaha!!!"

    player "Who is this guy?? He's acting very strangely... Is he the one behind the fights?"
    vivi "That is... That is my father!!!"
    player "Whaaat?!?"
    vivi "N-no... It's not possible that he's behind all this... It doesn't make any sense!"
    vivi "I have to know what's going on!"
    robin "Wait [vivi.n], something is strange about all this..."
    robin "Let's listen a little more from here..."

    unknown "Hahaha, now no one will believe in the king."
    unknown "His word is worthless now..."
    unknown "That's enough... No need to keep up the act..."

    show cobra c1_mr2 with Dissolve(0.4)

    unknown "Ufff, that feels good... I was getting tired..."
    unknown "I missed my own face."

    player "What the hell?!"
    player "The king can change his face!!"
    robin "No, Captain!! That's impossible... It must be due to a Devil Fruit..."
    player "How strange! That makes more sense... What a weird-looking guy..."
    player "He seems funny..."
    vivi "I've had enough of this!"

    show cobra c1_mr2:
        yalign 1.0
        linear 0.5 xalign 0.05

    show vivi annoyed with dissolve:
        yalign 1.0
        xalign 0.95


    vivi "Damn it, you're an imposter!"
    vivi "Who are you, and where is my father?"

    unknown "This is quite disappointing... I didn't know I was being followed..."
    unknown "Looks like I've been discovered!"
    unknown "There aren't many options now... What a shame, you already know too much..."

    hide vivi with dissolve
    show cobra c1_mr2:
        yalign 1.0
        xalign 0.05
        linear 0.5 xalign 0.5

    mr2 "You're right, obviously I'm not the king... My name is [mr2.n], you should have stayed home today..."
    mr2 "Now I'll have to kill you..."
    mr2 "Wait a moment."

    window hide
    window auto

    pause 0.5

    hide cobra c1_mr2 with moveoutright 

    pause 0.5

    show expression enemy_mr2.image with Dissolve(1.0):
        xalign 0.5
        yalign 0.5
        xoffset 1000
        linear 1.0 xoffset 0

    mr2 "Alright, now I'm ready... I'm sorry for you, but I have no choice..."
    mr2 "I don't fight women, but you know too much... Mr. 0 won't let this slide..."     

    call fight_start pass (enemy_pass = enemy_mr2, no_run = True, no_interface = True) from _fight_ar_nanohana_h # event_gameover = "ar_nanohana_h_end",
    
    $ music_arabasta()
    pause 0.5

    mr2 "Okay, that's enough, I give up, I give up!"
    mr2 "I didn't even want to participate in this, but if I didn't, Mr0 would kill me. You have to understand me!"

    show vivi happy with dissolve:
        yalign 1.0
        xalign 0.95

    vivi "Well done, [player.n]!! Tie him up tight...  We can't trust him right now, but you'll serve as proof."
    vivi "Now we have him as a prisoner!"

    $ vivi_love += 2
    narrador "[vivi.n] Love +2"

    mr2 "No problem, I'll be your prisoner and tell you everything..."
    mr2 "I even showed everyone my power if they wanted... But they must forgive me"

    show vivi neutral with Dissolve(0.2)  
    vivi "We'll see!"
    vivi "For now, we need to find [koza.n], make this guy talk, and tell him the whole truth about [crocodile.n]'s plans!"

    window hide
    show screen screen_black with Dissolve(0.6)
    $ game.location = "ar_nanohana"
    scene BG locations:
        blur 3
    hide expression enemy_mr2.image with Dissolve(0.8)
    hide vivi with dissolve
    window auto
    hide screen screen_black with Dissolve(0.1)


    narrador "You start searching the city for [koza.n]"

    show vivi neutral with Dissolve(0.2)

    vivi "There he is..."
    vivi "[koza.n]!!!"

    show vivi with dissolve:
        yalign 1.0
        linear 0.5 xalign 0.90
    
    pause 0.4

    show koza c1_hurt with dissolve:   
        yalign 1.0
        xalign 0.10

    koza "Mnm?!"
    koza "[vivi.n]... It's been so long..."
    koza "I thought your disappearance was part of the king's plot."
    koza "I didn't think you'd be around here..."
    koza "I'm glad you made it this far..."
    koza "If you're here, I suppose you know everything..."
    koza "I won't blame you for what your father did... But... You can't stop me!"
    koza "Your father has crossed the line today... There's no way to stop the people's anger."
    show vivi serious with Dissolve(0.2)
    vivi "[koza.n], I understand your anger, but it's not what it seems. Let me explain everything quickly."
    vivi "This man here, has the power of a strange devil fruit, he dressed up and changed his face like the king.... He is an impostor, the real culprit behind this chaos."
    vivi "My group and this boy are witnesses."
    vivi "We managed to defeat him and bring him here as proof!"
    vivi "But he's just a subordinate. The true mastermind is [crocodile.n]!"

    koza "Mnmn... The owner of the Rains Diner and casino?"
    koza "Mnmnm... It's pretty hard to believe all this."

    vivi "I know, it's completely insane... But let me explain everything briefly."
    vivi "You owe me that much after so many years of friendship!"

    koza "... Fine, you have a point. Tell me everything you know!"
    vivi "Perfect! It all started when we decided to infiltrate [crocodile.n]'s organization along with [igaram.n]..."


    show screen screen_black with Dissolve(0.3)
    pause 0.5
    hide screen screen_black with Dissolve(0.1)

    narrador "You take your time to explain everything to [koza.n]."

    koza "I can't believe all of this is happening..."
    koza "That bastard [mr2.n] tricked us all..."
    koza "I must stop the fighting..."

    vivi "Yes, you have to stop this! I'm sure you can do it!"
    vivi "With this evidence, you can calm things down a little..."
    vivi "Then we'll head to where [crocodile.n] is!"

    koza "I believe in you... I'll calm things down here and then head to Alubarna to protect the king."
    koza "When the time comes, I'll help you face [crocodile.n]. Together, we'll stop him!"

    $ ar_rebel_army = True

    if Arabasta.h == 13:
        vivi "Perfect! We will go ahead to Alubarna to stop [crocodile.n]."

    else:
        vivi "Perfect! Go and help the king!"
        vivi "Meanwhile, we will head to Rainbase, where we can stop [crocodile.n]!"

    jump ar_nanohana

label ar_nanohana_h_end:

    show screen screen_basic_black with Dissolve(0.6)

    stop ambient fadeout 2.0
    stop music fadeout 2.0

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None

    narrador "You passed out and your crew took you out"

    narrador "When you open your eyes, you see that you're lying in your cabin."

    narrador "You feel very weak."

    player "(I should eat something to regain my strength)"

    $ hide_label = "screen_basic_black_hide"
    jump sleep