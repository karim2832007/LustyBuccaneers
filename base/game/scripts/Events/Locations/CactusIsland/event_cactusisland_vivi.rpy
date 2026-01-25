# Version event: 5
# Version game: 0.31

label event_cactusisland_vivi:
    show screen screen_basic_black with Dissolve(0.8)

    narrador "After several drinks..."
    window hide
    window auto
    $ game.clock.next(increment = 5)
    hide screen screen_basic_black with Dissolve(0.8)


    pause 1.0
    show nami happy at center with dissolve
    nami "Wow, we've had such a great time, haven't we?!... We've been drinking until late!"

    hide nami with dissolve

    show robin at center with dissolve
            
    robin "It was fun, but I gathered very little useful information..."



        
    show robin:
        linear 0.4 xalign 0.85

    pause 0.4

    show yamato with dissolve:
        yalign 1.0
        xalign 0.5 
        
    yamato "Yeahhh! what do you think Captain?"

    pause 0.4

    menu:
        "It was fun!":
            player "At least it wasn't a complete waste of time! This bar is pretty entertaining!"
            show yamato happy with dissolve
            yamato "Hahah that's the spirit Captain!!"


            $ yamato_love += 2
            narrador "[yamato.n] Love +2"

        "Waste of time!":
            player "Meeeehh it wasn't that good, it was full of bounty hunters..."
            player "(And not a single decent woman!!)"
            yamato "Hahaha Don't say that Captain! We had a good time there"

            $ yamato_love += 1
            narrador "[yamato.n] love +1"  

    
    show yamato neutral with dissolve

    yamato "On the other hand..."
    show yamato smile with dissolve
    pause 0.5

    yamato "What's that?!?"

    window hide
    window auto

    hide robin
    hide yamato
    with dissolve

    show karoo with dissolve

    pause 0.5

    nami "What a strange animal this is?"

    window hide
    window auto

    show karoo:
        xalign 0.5
        yalign 1.0

        linear 0.4 xalign 0.40
        linear 0.6 xalign 0.50
        linear 0.4 xalign 0.60
        linear 0.6 xalign 0.50
        repeat

    pause 1.0

    nami "What is it doing?"
    yamato "It seems to be doing something..."
    robin "It looks like he wants us to follow him, Captain."

    player "Hahaha, what a strange animal!"
    player "I like him!!"
    player "Let's follow him and see what he wants."

    window hide
    window auto
    show screen screen_basic_black with Dissolve(0.8)
    hide karoo

    narrador "You follow the animal through several alleys in the city..."
    player "Hahaha, now he turned here at the corner... If he doesn't have an owner, we'll keep him as a pet..."

    $ game.location = "ci_alley"
    hide screen screen_basic_black with Dissolve(0.8)

    player "But what the hell happened here?!?"
    yamato "It seems there was a fight here recently, Captain... There are signs of a recent battle..."

    nami "Look over there, there's a man lying on the ground!!"
    robin "Did that duck bring us here?"   
    nami "Let's help the old man get up."

    show igaram with Dissolve(0.8)

    player "Hey, are you okay, old man? Looks like you got beaten up..."

    igaram "Those guys need much more than what they did to take down this old man..."
    igaram "Please, young travelers, I need your help..."

    $ igaram_name = "Igaram"
    igaram "My name is [igaram.n], and I am the Captain of the Royal Guard of [Arabasta.n]."
    player "And what's that? Is it important?"

    show igaram:
        linear 0.4 xalign 0.85

    pause 0.4

    show robin annoyed with dissolve:
        yalign 1.0
        xalign 0.5 
    
    robin "It's an important desert kingdom, a few islands away from here, Captain..."
    igaram "I'll overlook your offense for today... Because what happened is a matter of vital importance!"
    igaram "I beg you, I need your help!! You look young and strong enough... It has to be enough!"
    igaram "I swear you will be greatly rewarded!!"

    player "Look, sir, I see you're in a tough situation, but we don't do charity work for just any second-rate job..."

    igaram "This is not a second-rate job, It's a matter of vital importance. The princess has been kidnapped!!"

    show robin:
        linear 0.4 xalign 0.15

    show yamato annoyed with dissolve:
            yalign 1.0
            xalign 0.5

    yamato "Really?!?"
    robin "If he's telling the truth... This is a very delicate matter..."
    player "A princess!!!"
    player "(If she's a princess, she must be beautiful!!... A princess in my crew wouldn't be bad!)" 
    robin "(What is a princess and her bodyguard doing so far from the kingdom and in a place like this?)"

    hide robin with dissolve
    pause 0.5
    show nami serious with dissolve:
        yalign 1.0
        xalign 0.15 

    show nami berries with dissolve
    nami "(A princess as a hostage... We could get a lot of berries out of this guy!)"
    show yamato smile with dissolve
    yamato "(We'd have to overcome many battles to rescue her!... It would be a fun challenge!)"
 

    nami "Being the Royal Guard, the reward should be true, right? We accept the proposal..."
    nami "How about a billion [Berries.n]?"

    igaram "What?!?! A b... b... billion..."
    show yamato happy with dissolve
    yamato "I'd fight for much less, honestly..."

    show nami anger with dissolve:
        yalign 1.0
        xalign 0.15 

    nami "Shut up, [yamato.n]... Let me handle the negotiations..."

    show yamato happy with dissolve

    yamato "Hahah sorry! I'll step aside for a moment"
    
    hide yamato with dissolve
    show nami neutral with dissolve:
        yalign 1.0
        xalign 0.15          

    nami "Alright, where were we?"
    nami "You are the imperial guard, and it's a serious failure if you return to the kingdom just like that!"
    nami "If we don't close the deal soon, who knows what will happen... The princess's life will be in danger!"
    nami "Who knows what they might do to a young and beautiful princess surrounded by scoundrels!"

    igaram "B... b... But I'm just a humble servant, I can't promise that amount of money!"

    nami "So, the princess isn't worth it? Is that what you're implying?!?"

    igaram "No! I can't promise that amount, but if you save the princess, you can negotiate directly with her!"
    igaram "The princess's kindness knows no bounds, I'm sure she will agree to a generous sum!"

    igaram "Her life is in danger as we speak! I beg you, please, there's no time to lose!"

    igaram "If something happens to the princess... The kingdom of [Arabasta.n] would be lost!"

    nami "Hmmm... I don't know..."
    player "Alright, We can't leave a young and beautiful princess defenseless [nami.n]!"
    player "I'll speak with this princess once the job is done!"
    
    show yamato happy with dissolve:
            yalign 1.0
            xalign 0.5
    
    yamato "That's the spirit, Captain!"
    player "Where did they take her?!?"

    igaram "The princess's pet will lead you to where she's being held prisoner."
    igaram "Sorry for not being able to guide you, I'm very hurt I'll just slow you down."
    igaram "I will reach you as soon as I can..."
    igaram "I trust you!... The kingdom of [Arabasta.n] depends on you!"

    window hide
    hide nami
    hide yamato
    with dissolve
    window auto

    show igaram:
        linear 0.3 xalign 0.80

    pause 0.5
    igaram "Alright... Karoo, come here!"

    show karoo with Dissolve(0.8):
        xalign 0.10
        yalign 1.0

    pause 1.0

    igaram "Take them, Karoo, guide them to the princess!"
    igaram "They've promised to help us!"


    window hide
    window auto
    
    show screen screen_basic_black with Dissolve(0.8)
    hide igaram
    hide karoo
    $ game.location = "ci_den"
    hide screen screen_basic_black with Dissolve(0.8)

    player "Alright, this should be the place..."
    yamato "So far, they're just a simple band of mercenaries... How could the old man have lost to them?!"
    nami "With the captain here, this will be a piece of cake... An easy million [Berries.n]..."
    pause 0.5
    robin "!!!!!!"
    robin "Interesting..."
    robin "Look over there, [player.n]! Above the door..."
    player "Mmnm?!?... What is that symbol?"

    robin "That's the symbol of an alleged criminal underworld organization..."
    robin "All the available information about them is questionable or unreliable, but according to sources, their influence is quite significant."
    robin "They call themselves Baroque Works... No one knows what they're after, but their headquarters must be nearby..."
    robin "Most of their activities are recorded in these seas."
    robin "We should be cautious, there's a reason they have the princess... They must be planning something big!"
    player "I don't know who we'll encounter, but it surely won't be a problem!"
    player "Let's go in!"

    window hide
    window auto
    show screen screen_basic_black with Dissolve(0.8)
    $ game.location = "ci_captured"
    show events vivi captured vivi_captured
    hide screen screen_basic_black with Dissolve(0.8)

    player "(Wow, is this the princess? She looks so sexy in those chains!)"
    player "(I knew she was truly beautiful! I made the right choice coming here...)"
    player "(These chains just gave me an idea...)" 
    player "(Maybe I should have a room like this on the ship!)"
    yamato "Alright!!! We found her!... Honestly, that was easy..."
    nami "We need to get her down, let's find the key."


    show mr5 with dissolve:
        yalign 1.0
        xalign 0.10

    unknown "Hahaha! So you're the ones causing all this commotion..."
    unknown "So, you plan to take the princess?"
    player "We came to take her, you better stick to your duties... Pretend you didn't see anything..."
    unknown "Hahaha! How arrogant, little one... You have no idea what you're getting yourself into..."
    player "And who are you?"
    unknown "I'm the one in charge here... The boss wants her alive, so unfortunately, I'll have to take her with me..."
    player "Well, tell your boss it'll have to be another time. She's ours now!"
    unknown "How interesting... You really don't know who you're dealing with!"
    robin "You're an executive of Baroque Works, aren't you?"
    unknown "Mnmnm!?!... It seems you know too much... No matter, it's already too late, You won't leave here alive..."     
    mr5 "I am [mr5.n]"
    mr5 "The boss said: They've uncovered my secrets."
    mr5 "I honestly don't know what secrets he was talking about..."
    mr5 "But it doesn't matter because if someone searches for and uncovers the boss's secrets..."
    mr5 "They'll pay for their crime with death."
    mr5 "And if you try to help her, you'll meet the same fate!"


    window hide
    window auto
    show screen screen_basic_black with Dissolve(0.8)
    hide events vivi captured vivi_captured
    hide mr5
    show expression enemy_mr5.image with Dissolve(1.0):
        xalign 0.5
        yalign 0.5
    hide screen screen_basic_black with Dissolve(0.8)

    mr5 "In the name of the boss, you must be eliminated."
    mr5 "You'll pay with your life for getting in the way of Baroque Works."

    call fight_start pass (enemy_pass = enemy_mr5, no_run = True) from _fight_event_cactusisland_vivi

    hide expression enemy_mr5.image with Dissolve(0.8)

    $ music_arabasta()

    pause 0.2

    window hide
    window auto
    show screen screen_basic_black with Dissolve(0.8)
    show events vivi captured vivi_captured
    hide screen screen_basic_black with Dissolve(0.8)

    pause 0.5

    player "(Good! I thought it was going to be more complicated...)"

    menu:
        "Tough battle, but I was prepared":
            player "Tough battle, but I was prepared!!"
            robin "Well said Captain!"

            $ robin_love += 2
            narrador "[robin.n] Love +2"

        "Not tough enough":
            player "He was tough... But not tough enough."
            yamato "Easy job for our Captain!"

            $ yamato_love += 2
            narrador "[yamato.n] love +2"  


    player "I've got the key, let's get the princess down and get out of here!"

    hide events vivi captured vivi_captured with Dissolve(0.8)
    show vivi serious with Dissolve(0.8)

    call set_name_vivi from _call_set_name_vivi
    show vivi serious with dissolve 
    vivi "Thank you for rescuing me, strangers. I don't know who you are, but I'm very grateful... My name is [vivi.n]!"
    player "A pleasure, [vivi.n]. We know who you are, [igaram.n] told us everything… We'd better find another place to talk..."
    vivi "You're right. I think I have a lot to explain..."
    vivi "They could send reinforcements at any moment. Follow me, I'll take you somewhere safe..."

    pause 0.5

    window hide
    window auto
    show screen screen_basic_black with Dissolve(0.8)
    $ game.location = "ci_river"
    hide screen screen_basic_black with Dissolve(0.8)

    vivi "Alright... We should be safe here."
    show vivi happy with dissolve 
    vivi "I'm so thankful!... I really thought this was the end..."

    player "(Woooow!!! So this is what it means to be royalty. She's stunning!)"

    window hide
    pause 1.0
    window auto

    show vivi:
        linear 0.4 xalign 0.85

    show nami neutral at center with dissolve  

    nami "Well, it wasn't exactly easy!! You really weren't far from the end..."
    show nami berries with dissolve
    nami "[igaram.n] promised us a big reward for bringing you back! If it weren't for us, who knows what might have happened to you..."

    vivi "[igaram.n] is alright!?!... It's incredible... Even in his condition, he managed to find you all..."
    show nami neutral with dissolve
    vivi "I'll forever be grateful to him and to you!"

    show nami:
        linear 0.4 xalign 0.15

    pause 0.5    
    show yamato neutral at center with dissolve  

    yamato "Actually, it was your duck that guided us to him and then to where you were held captive... That duck is amazing! Hahaha!"
    vivi "Karoo!! I always trusted you, thank you so much!"

    #show vivi serious with dissolve
    show vivi serious with dissolve
    vivi "Unfortunately, this isn't a good time..."
    vivi "I assure you, I'll compensate you as soon as I can... Your kindness will always be remembered by me and my kingdom..."
    vivi "But this situation is much graver than you imagine!"

    hide yamato with dissolve
    show robin neutral at center with dissolve  

    robin "We're sure it is, princess, but what's the situation... Why were you taken prisoner?"
    vivi "It's a very long story, honestly..."
    player "We've got time to hear it, princess..."
    vivi "Well, I suppose that's the least I can offer you right now..."  
    
    vivi "As you know, I'm the princess of the kingdom of [Arabasta.n]."
    vivi "This was a prosperous and secure kingdom, a magnificent realm... It had been growing immeasurably compared to the rest of the region."
    vivi "But now, all of that has abruptly changed..."

    show vivi annoyed with dissolve 

    vivi "The kingdom is currently going through a great civil war!"
    show nami serious with dissolve
    show robin annoyed with dissolve
    vivi "The citizens are taking up arms against the current government, plunging the kingdom into complete chaos..."
    vivi "For now, the king, my father, is avoiding acting against the people, but there will come a time when he'll have no choice but to confront them..."
    vivi "The people are preparing... I have information that the final uprising will break out at any moment!"
    vivi "I can't stand by and watch my kingdom destroy itself! I must stop it!" 
    robin "But how could such a prosperous kingdom reach this point..."

    vivi "This is all the fault of Baroque Works... I don't know how, but they're manipulating the situation..."
    vivi "Gathering more information and finding those responsible was impossible, so I turned to [igaram.n]..."
    vivi "He helped me infiltrate the organization to discover who was behind it all and why!"

    hide robin with dissolve
    show yamato serious at center with dissolve  
    yamato "Looks like you're a very brave princess!"
    yamato "Did you find out who's behind all this?"

    vivi "Yes, the one behind it all calls himself Mr. 0 within the organization!..."
    vivi "But that's not all... His true identity makes the situation even worse... His real name is:" 

    show vivi anger with dissolve 

    vivi "[crocodile.n]!!!!"


    yamato "You can't be serious!!!"

    hide yamato with dissolve
    show robin annoyed at center with dissolve 

    robin "What did you say!!?!!"

    show nami annoyed with dissolve     
    nami "This can't be!! And on top of that, we let [mr5.n] escape!! How did we get ourselves into this..."
    player "And who's that?... Why are you so worried, girls..."
    robin "[crocodile.n] isn't just a nobody in the seas, Captain... How did you even set sail without knowing so many things?"
    player "That's why I have you, [robin.n]! Hahaha!" 
    
    vivi "I need to return and put a stop to his plan... I don't know if he wants to take over the kingdom of [Arabasta.n] or what he desires..."

    show vivi annoyed with dissolve 
    vivi "But I'll stop him!!"

    nami "If someone as dangerous as [crocodile.n] is involved, we won't get out of this easily!!!"
    nami "It doesn't matter what the reward is, we need to leave as soon as possible!"
    show vivi serious with dissolve
    robin "We can't just leave like that, it's too late for that now!"
    vivi "Now you know how serious the situation is!"
    vivi "With [mr5.n] escaping, your identity is also exposed. I'm sorry for getting all of you involved!... But now there's no other option..."            
    vivi "[player.n], I've seen how strong you are, I beg you to help me stop [crocodile.n]!!!"
    vivi "With your help, I'm sure we can bring peace back to the kingdom!!!"
    vivi "Please, I'll do anything!"

    pause 0.5
    player "!!!"


    menu:
        "Of course we will help!!":
            player "Of course we will help!"
            player "We can't leave a princess in trouble alone!"

            $ robin_love += 2
            $ nami_love += 2
            $ yamato_love += 2
            $ vivi_love += 1
            narrador "[robin.n], [yamato.n] and [nami.n] Love +2"

            narrador "[vivi.n] Love +1"

        "Anything!?!":
            player "Anything, you say!?!"

            $ vivi_lust += 2
            narrador "[vivi.n] lust +2"  

    show nami neutral with dissolve  
    show vivi shame with dissolve 
    vivi "Yes! Once the problem is resolved, my father, the king, will reward you enormously!!"
    player "(This is my chance... Nothing ventured, nothing gained!!!)"
    player "Then it's decided!!!"
    show vivi happy with dissolve
    vivi "Thank you so much for taking on this complicated request, [player.n]!!"
    nami "I can't believe it, Captain...."

    hide nami with dissolve
    show yamato happy with dissolve:
        yalign 1.0
        xalign 0.15

    yamato "This is getting exciting!!!"
    show robin neutral with dissolve 
    robin "This is getting interesting... Coincidentally, I needed to head to [Arabasta.n] anyway..."
    player "Really, [robin.n]?? You never told me you wanted to go there..."
    robin "I have important personal matters... But now isn't the time for that..."
    player "???"
    vivi "Alright then... Let's go get [igaram.n] and set sail!!"
    vivi "I'll give you the Eternal Pose to Arabasta, with it, we can easily reach my kingdom!"

    $ epose_arabasta = True
    narrador "Eternal Pose: Arabasta"

    player "On our way!!"

    $ CactusIsland.h = 3
    jump ci_whisky_peak



