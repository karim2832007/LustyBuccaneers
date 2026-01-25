# Version event: 6
# Version game: 0.33

label event_yamato_hangout:

    show yamato c1 with dissolve

    yamato "Hello, Captain. Do you need anything from me?"
    
    jump event_yamato_hangout_menu


label event_yamato_hangout_menu:
    menu:
        "Hangout":
            call yamato_hangout from _call_yamato_hangout

        "Give":
            call event_yamato_give from _call_event_yamato_give_hangout
            jump event_yamato_hangout_menu

        "Dismiss Her":
            player "That's all, [yamato.n]. You can go back to your tasks."

            if yamato_love < 10:
                show yamato anger with Dissolve(0.2)
                yamato "If there's nothing important to do, please try not to waste my time. Every second lost in training gives our rivals a greater advantage!"

            elif yamato_love < 20:
                show yamato with dissolve
                yamato "Perfect, Captain. You know where to find me if there are any issues!"

            elif yamato_love >= 20:
                show yamato with dissolve
                yamato "So soon?! We hadn't even warmed up yet!"

                if yamato_lust >= 20:
                    yamato "If you need anything else, call me! I have no problem doing additional training with you at night... I could learn a thing or two if you teach me!"
                else:
                    yamato "If you need anything else, just call me!"

    hide yamato with moveoutright
    pause 0.5
    return

label yamato_hangout:
    $ yamato_random_talk = renpy.random.choice(["yamato_hangout_1","yamato_hangout_2","yamato_hangout_3","yamato_hangout_4"])

    #$ yamato_random_talk = "yamato_hangout_4"

    call expression yamato_random_talk from _call_yamato_random_talk_hangout
    return

label yamato_hangout_1:
    player "You're always training! And while I enjoy watching you, I was wondering if you do it for a particular reason?"
    show yamato c1 happy with dissolve
    yamato "Always so attentive... It's true that I have a goal!"
    pause 0.5
    show yamato c1 serious with dissolve
    yamato "I never mentioned it before, but before we met, a great tyrant ruled in my homeland..."
    yamato "The island is completely taken by force..." 
    show yamato c1 anger with dissolve    
    yamato "There is hunger, sadness, and death everywhere..."
    yamato "Anyone who opposes him ends up badly, so one day I had no choice but to flee..."
    yamato "Honestly, it's a topic that concerns me a lot... So many wars, hunger... It's the weakest like the elderly and children who suffer the most."
    show yamato c1 annoyed with dissolve
    yamato "That's why I decided to go out to sea and become strong, to contribute to the change in this new era."
    yamato "And someday, I will return to my homeland and change the situation there as well..."
    yamato "Gradually, we will climb in fame and influence with the crew, providing security to as many people as possible."
    yamato "Everyone will respect and fear us! We'll make the waters safer for our own..."
    player "That's the spirit [yamato.n]! You have a noble goal, and I'll help you achieve it!"
    show yamato c1 happy with dissolve
    yamato "Thank you, Captain! I'll get back to training, there's no time to waste. See you later."
          
    $ yamato_love += 2
    narrador "[yamato.n] Love +2"

    return

label yamato_hangout_2:
    player "[yamato.n], besides being so attractive, you are always so energetic and youthful! You are very active!"
    yamato "Hahaha, you're such a flatterer, Captain... I always try to spend my time training or learning different things..."
    yamato "I always see you doing activities too!"
    player "Hahaha, nowhere near as many as you... I think my youthful days are over..."
    yamato "What are you talking about, you are very young!... Speaking of which, do you know how old I am?"


    menu:
        "33 years old":

            player "Hmm... I think you should be around 33 years old, right?"
            show yamato c1 anger with dissolve  
            yamato "Do I seem that old to you?!"
            yamato "You added a few years, Captain!"
            yamato "Next time, remember it's always better to subtract years from a woman's age!" 


            $ yamato_love -= 1
            narrador "[yamato.n] Love -1"

        "28 years old":

      
            player "I think I remember you were around 28 years old... isn't that right?"
            show yamato c1 happy with dissolve  
            yamato "What a memory, Captain! Always so attentive... Remembering those talks before I joined the crew speaks highly of you..."
            yamato "That is exactly my age!... It must have been pure luck!"
           

            $ yamato_love += 2
            narrador "[yamato.n] Love +2"

        "22 years old":

            player "Hmm... I would say about 22 years old!"
            show yamato c1 happy with dissolve            
            yamato "Hahaha! Seeing me so active confused you, Captain!... That's not my age!"
            yamato "At least you didn't add years! Never do that with women!"


            $ yamato_love += 1
            narrador "[yamato.n] Love +1"

    return

label yamato_hangout_3:
    player "[yamato.n], What do you like to do in your free time? Do you have any hobbies or activities you do frequently?"
    yamato "Ahoy Captain!! Most of the time, I'm training! It's the only way I'll become stronger to keep moving forward with our adventures..."
    yamato "In my free time, I also enjoy fishing or doing any other activity that helps me improve my survival skills."


    menu:
        "That's interesting":

            player "That's interesting, you have your goal clear in mind!"
            player "If you need any help, just let me know!"
            show yamato c1 happy with dissolve
            yamato "I appreciate the words, Captain! It's time to get back to training, I hope to practice with you when I can!"


            $ yamato_love += 1
            narrador "[yamato.n] Love +1"

        "It's a very stimulating conversation...":

            player "I find our conversation very stimulating, you are so sexy when you talk about these topics so seriously..."
            player "We have more in common than you might imagine [yamato.n]!"
            player "Maybe in the future we could train together! I have a couple of routines that could help you."
            show yamato c1 shame with dissolve           
            yamato "Don't say it like that, Captain, it embarrasses me! Maybe I can learn a few things from you. We'll arrange those training sessions later on."
            player "I look forward to it! Keep it up, and best regards!"


            $ yamato_lust += 1
            narrador "[yamato.n] Lust +1"

        "Always training, doesn't it get boring?":

            player "You have quite unusual tastes, to be honest... Always training, doesn't it get boring?" 
            player "For a lovely girl like you, so much training might not be good. It could adversely affect your physique..."
            show yamato c1 annoyed with dissolve   

            yamato "I don't find it surprising that a pirate like you would have that opinion about women... But I'll let your comment slide."
            yamato "I won't argue with you about this. I'll get back to my work..."

           

            $ yamato_love -= 1
            narrador "[yamato.n] Love -1"

    return

label yamato_hangout_4:
    player "I enjoy watching you train so much, [yamato.n]."
    player "Seeing your beautiful and sexy body all sweaty and pumped... Your great effort to improve and surpass yourself..."
    player "I'm so glad I chose you to be part of this crew!"
    show yamato c1 shame with dissolve   
    yamato "You're so flattering and interested in me, Captain..."
    yamato "I didn't think you held me in such high regard..."
    yamato "So tell me, what do you like watching so much? I don't think you just watch me, that would be very boring..."


    menu:
        "See your beautiful body":

            player "It's not the only reason, but your body is the main one..."
            player "It's such a gift to see your sexy figure training daily."
            show yamato c1 shame with dissolve   
            yamato "You're such a flatterer, Captain, so daring!"
            yamato "But I like knowing that you find me attractive!"
            yamato "I'll continue with my tasks, Captain. Until next time!"


            $ yamato_lust += 1
            narrador "[yamato.n] Lust +1"

        "See your dedication and technique":

            player "Seeing your great dedication and effort, and learning from your technique, is what motivates me the most!"
            show yamato c1 happy with dissolve            
            yamato "Thank you for your words, Captain..."
            yamato "I like knowing that you value my effort! Maybe next time we can practice together and I can teach you some things..."
            yamato "I'll continue with my tasks, Captain. Until next time!"

           

            $ yamato_love += 1
            narrador "[yamato.n] Love +1"

    return