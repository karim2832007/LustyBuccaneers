# Version event: 5
# Version game: 0.6

label event_robin_hangout:

    show robin c1 with dissolve

    robin "Hello, Captain. Do you need anything from me?"
    
    jump event_robin_hangout_menu

label event_robin_hangout_menu:
    menu:
        "Hangout":
            call robin_hangout from _call_robin_hangout

        "Give":
            call event_robin_give from _call_event_robin_give_hangout
            jump event_robin_hangout_menu

        "Dismiss Her":
            player "That's all, [robin.n]. You can go back to your tasks."

            if robin_love < 10: 
                show robin anger with Dissolve(0.2)
                robin "If there's nothing important to do, please try not to waste my time. I get distracted from my research!"

            elif robin_love < 20:
                show robin with dissolve
                robin "Great, Captain. You know I'm here if you need any advice!"

            elif robin_love >= 20:
                show robin with dissolve
                robin "What a shame! I thought we would continue spending time together. Call me again whenever you wish, Captain!"

                if robin_lust >= 20:
                    robin "Time flew by so quickly!! You know I love learning anything with you. When you have time, I'd like you to teach me more privately!"
                else:
                    robin "If you need anything else, just call me!"

    hide robin with moveoutright
    pause 0.5
    return

label robin_hangout:
    $ robin_random_talk = renpy.random.choice(["robin_hangout_1","robin_hangout_2","robin_hangout_3","robin_hangout_4"])

    #$ robin_random_talk = "robin_hangout_4"

    call expression robin_random_talk from _call_robin_random_talk_hangout
    return

label robin_hangout_1:
    robin "How are you, Captain?... As you know, I spend a lot of my time researching and investigating the history of the world..."
    robin "I hope to receive all the possible help from you and the rest of the crew to achieve my goals..."

    menu:
        "I'll keep it in mind":
            player "(Boring...)"
            player "At the moment, we have many important issues to attend to... I'm always very busy..."
            player "I don't think I can help right now, but I'll keep it in mind for the future... I'll ask some of the other girls."
            show robin c1 anger with dissolve
            robin "I figured as much..."
            robin "Don't worry, I don't know why I asked... Until next time."

            $ robin_love -= 1
            narrador "[robin.n] Love -1"

        "We'll help you":
            player "Obviously, we'll help you in any way we can!"
            player "I don't know much about science or history, but it could be fun and I might learn a thing or two!"
            show robin c1 happy with dissolve
            robin "Thank you so much for your support, Captain! It's important..."
            robin "I'm sure I can teach you several interesting things! Until next time."

            $ robin_lust += 1
            narrador "[robin.n] Lust +1"

    return

label robin_hangout_2:
    player "[robin.n], how are you? What do you think about all the recent events happening in the world and the start of this new pirate era?"
    robin "Captain!! What an interesting question, I didn't think you were interested in political matters..."
    robin "The world has always been in constant conflict and suffering, surrounded by internal intrigues and mysteries!" 
    robin "It's essential that we learn from the past and history to advance wisely into the future."
    robin "Don't worry, I'll always try to guide you and keep you informed about the latest news..."

    menu:
        "I feel reassured with you here":

            player "I feel reassured knowing I have someone by my side who is always well-informed!"
            show robin c1 happy with dissolve
            robin "That's how it will be, Captain. I'll return to my investigations. Take care!"

            $ robin_love += 1
            narrador "[robin.n] Love +1"

        "I find our conversation very stimulating":

            player "I find our conversation very stimulating. It's always great to hear a smart and sexy woman like you, [robin.n], talk about political topics!"
            player "We should spend more time discussing these subjects!"
            show robin c1 shame with dissolve
            robin "I didn't realize you saw me that way, Captain. Your compliments are flattering! I'll get back to my work for now." 
            player "I'm sure we'll have more opportunities to talk about these topics."
            player "I look forward to it! Keep it up, best wishes!"

            $ robin_lust += 1
            narrador "[robin.n] Lust +1"

        "The story is not interesting":

            player "I never found history interesting, it always seems so boring... Such a waste of time..."
            show robin c1 anger with dissolve
            robin "Not everything is about adventures, Captain! If we don't learn from the mistakes of the past, we'll keep stumbling over the same stone..." 
            robin "It's important to be well-informed about various subjects..."
            robin "I didn't think you were so narrow-minded... I'll get back to my work..."


            $ robin_love -= 1
            narrador "[robin.n] Love -1"

    return

label robin_hangout_3:
    player "[robin.n], what do you like to do in your free time? Do you have any hobbies or activities that you do frequently?"
    robin "Captain!! I'm flattered that you ask..." 
    robin "As you know, I often focus on my research and reading all kinds of information, books, and history that I can access..." 
    robin "But I also spend time cultivating rare plants that I find around the seas..."
    robin "Continuing to learn and document new knowledge is what will preserve the world and nourish future generations."

    menu:
        "So interesting!!":

            player "How interesting everything you tell me! I knew I made the right choice in recruiting you for my crew."
            show robin c1 happy with dissolve
            robin "Thank you for the kind words, Captain! It's time for me to get back to my work. Goodbye!"
            

            $ robin_love += 1
            narrador "[robin.n] Love +1"

        "I find our conversation very stimulating":

            player "I find our conversation very stimulating, you are so sexy when you talk about these topics so seriously, we have more in common than you might imagine [robin.n]!"
            player "Maybe in the future we can explore our desires!"
            show robin c1 shame with dissolve
            robin "I didn't realize you saw me in that way, Captain. Your compliments are flattering! I'll get back to my work for now." 
            robin "I would like to discuss these topics more often with you..."
            player "I look forward to it! Keep it up, best wishes!"


            $ robin_lust += 1
            narrador "[robin.n] Lust +1"

        "Always reading... Soooo boring...":
            player "You have rather peculiar tastes, to be honest... Don't you get bored always reading documents?"
            show robin c1 anger with dissolve
            robin "I don't find it strange that a pirate like you doesn't see value in time spent on research..." 
            robin "Perhaps I should consider the source of the comment..."
            robin "I won't argue with you about this topic. I'll get back to my work..."


            $ robin_love -= 1
            narrador "[robin.n] Love -1"

    return

label robin_hangout_4:
    robin "How are you, Captain?... What do you think of the following phrase:"
    robin "Those fools who do not respect and learn from the past, are doomed to repeat it..."

    menu:
        "It's quite complex to understand":
            player "Umm... Well, I'm not sure about it"
            player "It must be something you read in your books, perhaps??"
            robin "..."
            robin "That's a rather poor analysis, Captain... But don't worry, you have me to take care of these matters..."
            robin "It's a shame that you have no interest in these topics, your lack of intellect is quite unsexy..."  
            robin "Thanks for the chat. We'll continue it another time!"


            $ robin_lust -= 1
            narrador "[robin.n] Lust -1"

        "How interesting":
            player "Well, it's quite an interesting phrase, someone very wise must have said it..."
            player "I suppose it's related to the study and learning of history, coming from you"
            robin "That's an interesting way to see it, Captain!"
            robin "One interpretation could be what you mentioned, about studying history to avoid repeating the same mistakes..."
            robin "Thanks for the chat. We'll continue it another time!"


            $ robin_love += 1
            narrador "[robin.n] Love +1"

    return