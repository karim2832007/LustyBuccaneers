# Version event 3
# Version game 0.39

label dressrosa_h14():
    $ ui_interface = False

    show rebecca c2 happy c2_wounds at center with Dissolve(0.8) 

    pause 0.5
    rebecca "[player.n]!!!"
    rebecca "You... you're back! And in one piece!"
    show rebecca c2 serious with Dissolve(0.2) 
    rebecca "How are you?! Are you hurt?! Let me check you..."
    player "Don't worry, I'm fine hahaha. Didn't you see the fight?"

    pause 0.5
    show rebecca c2 neutral with Dissolve(0.2)

    rebecca "I... I still can't believe how easily you defeated [logan.n] out there."
    rebecca "He was one of the most feared fighters in the Colosseum, but you beat him like it was nothing..."
    rebecca "You were so brave... So determined... And ruthless... You didn't give him any chance... I liked how you handled him at the end..."
    player "Haha, all of that was for you..."
    rebecca "..."
    show rebecca c2 serious with Dissolve(0.2)
    rebecca "In my fight..."
    rebecca "In my fight, everyone was cheering for him to kill me... I felt so alone."

    menu:
        "Embrace her warmly to comfort her.":
            player "Hey... It's okay. Come here."
            narrador "You gently pull [rebecca.n] into a warm embrace."
            player "You're not alone anymore, [rebecca.n]. I promise."
            rebecca "*sniff* Th-Thank you... I..."

            $ rebecca_love += 2
            narrador "[rebecca.n] love +2"

        "Reassure her with determination.":
            player "Listen to me, [rebecca.n]. We will defeat [donflamingo.n]!"
            player "I swear I'll protect you and [Dressrosa.n], no matter what."
            narrador "You place a steady hand on her shoulder, looking into her eyes with resolve."
            player "You're not alone in this fight anymore."
            rebecca "*sniff* O-Okay... I trust you..."

            $ rebecca_love += 1
            narrador "[rebecca.n] love +1"

    rebecca "You don't know how much that means to me."
    player "I meant every word."

    show rebecca c2 shame with Dissolve(0.2)
    rebecca "I-I'm sorry... I just... I wanted to..."
    player "Hey, don't apologize. You have nothing to be sorry for."
    player "To be honest... I've been wanting to say that for a long time too."

    show rebecca c2 neutral with Dissolve(0.2)
    rebecca "You... you did?"
    player "Ever since we fought side by side in that colosseum... every time you smiled at me after a tough battle, every time you trusted me when everything seemed lost..."
    player "Those moments we shared, supporting each other through all the pain and fear... they meant everything to me."
    player "You've become someone incredibly special, [rebecca.n]. More than just a friend, more than an ally."

    show rebecca c2 shame with Dissolve(0.2)
    rebecca "I... I feel the same way. When I was alone in the arena, I never thought I'd find someone who would fight for me the way you did."
    rebecca "You gave me hope again. You made me feel safe... and cared for."
    rebecca "That's why I couldn't hold back just now. My heart wouldn't let me."
    player "And I don't regret a single second of it."
    player "Holding you close like that... it felt right. It felt like something we've both been carrying inside for a while."

    show rebecca c2 happy with Dissolve(0.2)
    rebecca "I'm so glad... It felt warm. It felt... nice. More than nice."

    narrador "We stand in silence for a moment, just looking at each other, the air between us soft and full of unspoken feelings."
    player "Before I have to go face the next fight..."
    player "Could I ask for one small thing? Something to carry with me?"
    player "Maybe... a good luck kiss? Just one, from the girl who's become my reason to keep winning."

    show rebecca c2 shame with Dissolve(0.2)
    rebecca "A kiss... for luck?"
    rebecca "I... I'd like that very much."

    narrador "Smiling softly, her cheeks glowing with a tender blush, [rebecca.n] steps closer."
    narrador "She rises slightly on her toes, places a gentle hand on your chest, and presses her warm lips to yours in a slow, loving kiss full of quiet affection and newfound courage."
    narrador "When she pulls back, her eyes shine with emotion, and a small shy smile curves her lips."

    show rebecca c2 neutral with Dissolve(0.2)
    rebecca "Please... come back to me safe."
    player "I will. I promise."

    show rebecca c2 serious with Dissolve(0.2)
    rebecca "But..."    
    rebecca "But the fight's not over yet."
    rebecca "The next round will be even tougher... and after that..."
    rebecca "Diamante will be there..."
    rebecca "I thought if we won the [HanaHanaFruit.n] fruit, we could become strong enough to free [Dressrosa.n] from [donflamingo.n]."
    rebecca "But... I never imagined that idea would be so hard to carry out... Only now do I see just how much it really is..."
    player "I'm sorry, [rebecca.n]. I promise I'll win that Devil Fruit and use its power to defeat [donflamingo.n]."
    rebecca "[donflamingo.n] is so powerful... the thought of facing him scares me. I can't bear to lose anyone else..."
    player "You won't, I promise. With you cheering me on, I feel like I can defeat anyone... even [donflamingo.n]."
    show rebecca c2 happy with Dissolve(0.2)
    rebecca "Hahah... You... really mean that?"
    player "Every word. Having you by my side gives me strength."
    rebecca "Then I'll be there. I'll cheer for you, no matter what."
    pause 0.5
    player "Now that we're talking about it... after cooling down from the fight, I'm starting to realize..."
    player "It was a tough one, though. My body's still buzzing with adrenaline."
    show rebecca c2 neutral with Dissolve(0.2)
    player "I could really use some... relaxation right now."
    rebecca "What do you mean?"
    narrador "I let my gaze drop meaningfully to my waist, then back up to her eyes."
    pause 0.5
    player "We really are close by now... we've been through so many things... and you really do feel good with me, right?"
    show rebecca c2 shame with Dissolve(0.2)
    rebecca "Ye... Yes.."
    player "Then... I can think of one perfect way you could help me unwind... as a victor's reward."
    pause 0.5
    rebecca "Y-you mean... With my... mouth?"

    player "Exactly!. You've already shown me how grateful you can be. One more time wouldn't hurt, right?"
    rebecca "B-but... we're in the palace now. Anyone could walk in..."
    rebecca "And I... I'm so embarrassed..."
    player "The door's locked. No one's coming. And You'll do amazing. Don't doubt yourself."
    rebecca "I... I don't know if I can. My heart's pounding just thinking about it."
    player "[rebecca.n], look at me."
    player "I fought for you today. I won for you. All I'm asking is a little... personal celebration."
    player "Just between us. It'll be our secret."
    pause 0.5
    narrador "She bites her lip, glancing away, then back at me. Her hands fidget at her sides."
    pause 0.5
    rebecca "I do want to reward you properly... You deserve it more than anyone."
    rebecca "It's just... I... I don't have much experience at all."
    player "That's fine. I'll guide you... I know you'll learn quickly."
    narrador "She slowly drops to her knees in front of me, face burning red, eyes fixed on the floor at first."

    menu:

        "Ask her sweetly and romantically":
            player "[rebecca.n]... after everything we've been through together, just looking at you fills my heart with warmth."
            player "I want to feel even closer to you, in the most tender and intimate way..."
            player "Would you let me guide you gently? I want to feel your soft lips on me... because it would bring us even nearer to each other."
            player "Only if your heart wants it too, my brave princess."
            player "It would be the most beautiful gift you could ever give me."

            $ rebecca_love += 1
            narrador "[rebecca.n] love +1"

        "Ask her in a more direct and lustful way":
            player "[rebecca.n], seeing you on your knees like this is already driving me insane..."
            player "I need that sweet, shy mouth of yours wrapped around me."
            player "Suck me slowly, tease me with that curious little tongue..."
            player "Be my good girl and take every inch until I can't hold back anymore."
            player "I promise I'll return the favor and make you feel incredible afterward."

            $ rebecca_lust += 2
            narrador "[rebecca.n] lust +2"

    pause 0.5
    rebecca "O-okay... It's not just because you won, or because you're a hero..."
    rebecca "It's because... my heart beats differently when you're near me, [player.n]."
    rebecca "Every time I look at you, I feel something warm growing inside me..."
    rebecca "I want to do this... because I'm starting to fall for the man who changed my life."
    rebecca "So please... let me show you how much you already mean to me."
    rebecca "Just... tell me what to do, [player.n]. I want to make you feel good after your victory."
    

    $ _window_hide()
    jump event_dr_h14_rebecca_blowjob



