# Version event 2
# Version game 0.38

label dressrosa_h12():
    $ ui_interface = False


    narrador "After [rebecca.n]'s defeat, she is escorted out of the arena by the tournament staff."
    narrador "When you return to the warm-up room, you manage to hear that she was seen crying as she walked away toward one of the Coliseum’s storage rooms."
    pause 0.5
    narrador "After searching for her for a few minutes, you finally manage to find her."

    pause 1.0

    narrador "The air is dusty and stifling, lit only by faint rays of light filtering through the window bars."
    narrador "She sits on the cold ground with her back against a crate, trying to make herself small."
    narrador "A streak of blood runs down her forehead. Her sword lies on the ground beside her."
    narrador "When she sees you come in... she decides to slowly stand up and approach you, staying silent..."


    show rebecca c2 serious c2_wounds at center with Dissolve(0.8) 
    pause 1.0

    player "[rebecca.n]! There you are..."
    player "Are you okay?!"
    pause 0.5
    rebecca "[player.n]..."    
    rebecca "What... What are you doing here...?"
    rebecca "You should be in the arena."
    rebecca "The next match is about to start in a few minutes..."
    pause 0.5
    player "I was looking for you."
    player "You ran off after your fight."
    player "I was worried."
    rebecca "Worried...?"
    rebecca "I'm fine."
    rebecca "You shouldn't concern yourself with me."

    narrador "Even as she says this, her voice is unsteady."
    narrador "In the dim light, you can see tears clinging to her lashes and the pained expression she can't quite hide."

    player "[rebecca.n], you're hurt."
    player "Let me help you."
    rebecca "No."
    rebecca "Stay back!"
    pause 0.5
    player "Please, you shouldn't be alone right now."
    player "You need medical attention."
    rebecca "I don't need anything."
    rebecca "Especially not your pity."
    narrador "Her words are sharp, but her trembling voice betrays her despair."
    rebecca "I... I don't want you to see me like this."
    player "Like what? Defeated?"
    pause 0.5
    rebecca "Yes... defeated."
    rebecca "I lost..."
    rebecca "And I ruined everything."
    player "The tournament isn't over yet."
    player "This isn't the end."
    rebecca "For me, it is."
    rebecca "All those people in the stands... they were cheering for [logan.n] to crush me."
    rebecca "They hate me..."
    rebecca "They've always hated me."
    rebecca "And now I've proven them right."
    rebecca "I'm nothing but a disappointment."
    player "Don't say that."
    rebecca "It's true."
    rebecca "I failed..."
    rebecca "I failed everyone who was counting on me."
    rebecca "I'm so weak..."
    rebecca "All of it was for nothing."
    player "[rebecca.n]..."
    pause 0.5
    rebecca "I... I... I trained every day."
    rebecca "I fought so hard to get this far."
    rebecca "I wanted to restore my family's honor..."
    rebecca "To protect the people important to me."
    rebecca "And in the end, I couldn't do it."
    rebecca "I threw away my only chance!"
    narrador "She hugs her arms around herself, shoulders shaking. You can hear her begin to sob, each one muffled as she tries to keep her composure."
    
    menu:
        "Try to encourage her":

            player "[rebecca.n], you fought bravely out there."
            player "You have nothing to be ashamed of."
            player "One loss doesn't erase everything you've accomplished."
            player "I've seen you fight... you're incredible."
            narrador "[rebecca.n] lifts her head slightly at your words, meeting your eyes for just a second before turning away again."
            rebecca "Incredible? I could barely fight back at all."
            rebecca "All I did was dodge his attacks..."
            rebecca "Run and hide, just like the coward they all say I am."
            player "You're not a coward."
            player "You were strategizing."
            player "You knew you couldn't match [logan.n]'s raw strength head-on, so you used your speed."
            player "There's nothing shameful about that."

            $ rebecca_love += 1
            narrador "[rebecca.n] love +1"
            pause 0.5
            rebecca "Call it whatever you want..."
            rebecca "It ended the same."
            rebecca "He overpowered me completely."
            rebecca "I couldn't even scratch him."
            rebecca "Don't you get it?"
            rebecca "All my training, all my hopes... it was all useless in the end."




        "Stay silent and let her vent":
            narrador "You stay quiet, giving her a moment to release her feelings."
            rebecca "Say something..."
            rebecca "Don't just stand there."
            player "I'm... I'm sorry, [rebecca.n]."
            player "I can't imagine how you feel right now."
            pause 0.5
            rebecca "How could you?"
            rebecca "You didn't lose everything in a single moment like I did."
            rebecca "You don't know what this loss means to me..."
            player "You're right."
            player "I don't know."
            player "But... maybe you could help me understand."
            player "Please, [rebecca.n]. Tell me what this means to you."
            narrador "[rebecca.n] opens her mouth as if to speak, but for a moment nothing comes out. She chokes on a sob as fresh tears roll down her face."
    
    
    pause 0.5
    rebecca "When I lost out there, I didn't just lose a match."
    rebecca "I lost the only chance I had..."
    rebecca "The only hope for... for saving anyone."
    pause 0.5
    player "The only hope for what?"
    pause 0.5
    rebecca "Do you know what the prize of this tournament is?"
    player "Yes... the {outlinecolor=#a85d74}{color=#ffc0cb}Hana Hana Fruit!{/color}{/outlinecolor}"
    player "Power like that could make someone incredibly strong."
    rebecca "Strong enough to possibly challenge [donflamingo.n]..."
    narrador "She nearly spits out the name, hatred and fear mingling in her tone. At the mention of it, you feel a chill, the air seems heavier with that name spoken aloud."
    player "[donflamingo.n]... Several times you told me that you wanted to defeat him."
    rebecca "I had to win that fruit."
    rebecca "It was my only chance to gain the power I need."
    rebecca "I wanted it so I could... to save someone I care about."
    rebecca "And to take that tyrant down."
    player "Save someone? Who?"
    pause 0.5
    rebecca "The person who trained me."
    rebecca "He's... more than just a teacher."
    rebecca "He raised me, protected me when I had no one else."
    rebecca "And now he's planning to do something reckless..."
    rebecca "To fight [donflamingo.n] on his own."
    rebecca "If he goes through with it, he'll die."
    narrador "Her voice trembles violently. You've never seen her so scared."
    rebecca "I thought if I had the {outlinecolor=#a85d74}{color=#ffc0cb}Hana Hana Fruit!{/color}{/outlinecolor}, I could fight by his side..."
    rebecca "Or at least stop him from sacrificing himself."
    rebecca "I wanted to be strong enough to protect him, just this once."
    rebecca "He always told me I could do it."
    rebecca "I wanted so badly to prove him right..."
    rebecca "But instead, I failed."
    rebecca "I lost."
    rebecca "And now all of it was for nothing."
    rebecca "I let everyone down..."
    rebecca "The people of this country..."
    rebecca "My family..."
    rebecca "And him..."
    pause 1.0
    player "[rebecca.n], listen to me."
    player "You haven't let anyone down."
    player "You're not the one at fault here."
    player "[donflamingo.n] is the one who set this cruel game up."
    player "He's the one hurting people."
    player "You tried to help, to fight for what's right."
    player "That's more than most people would dare to do."
    pause 0.5
    rebecca "But it wasn't enough."
    rebecca "Trying isn't enough."
    rebecca "I'm still too weak..."
    rebecca "If I can't even defeat one arena brute like [logan.n], how am I ever going to defeat a monster like [donflamingo.n]?"
    player "You won't have to fight him alone."
    rebecca "..."
    pause 0.5
    player "I'll help you!!!"
    rebecca "What...?!?"
    player "I'm going to take down [donflamingo.n], [rebecca.n]."
    player "One way or another, his reign ends here."
    narrador "[rebecca.n] stares at you, eyes wide in disbelief."
    rebecca "Why would you... Why would you even say that?"
    rebecca "[donflamingo.n] is unbelievably powerful."
    rebecca "Do you have any idea what he's done?"
    rebecca "What he's capable of?"
    pause 0.5
    player "I know exactly what he's done."
    player "And I refuse to stand by and let it continue."
    player "I promise you, I will stop him."
    narrador "She shakes her head, fresh tears falling as she does."
    pause 0.5
    rebecca "Stop it..."
    rebecca "Just stop."
    rebecca "Don't make promises you can't keep."
    rebecca "Do you know how many people have tried to fight him and paid with their lives?"
    rebecca "For ten years he's terrorized [Dressrosa.n]."
    rebecca "He's destroyed families..."
    rebecca "He destroyed my family."
    rebecca "He... he killed my mother in cold blood."
    rebecca "He turns people into his puppets and playthings."
    rebecca "He takes away everything they love, everything they are!"
    rebecca "He took everything from me..."
    rebecca "And I couldn't do anything to stop it."
    rebecca "So please... don't throw your life away too."
    pause 0.5
    player "He..."
    player "I'm not throwing my life away."
    player "And I'm not leaving."
    player "Maybe I haven't been here as long as you have, but I can see how much pain he's caused."
    player "I won't let it go on any longer."
    player "You're not alone in this fight anymore."
    player "I meant it: {size=40}I'll help you defeat him!{/size}"
    pause 0.5
    narrador "[rebecca.n] presses her lips together, as if fighting back the urge to hope."
    rebecca "You... you sound just like him."
    player "Him?"
    rebecca "The soldier... The one who trained me."
    player "(???)"
    rebecca "He may look like just a toy soldier to everyone else, but to me he's the bravest man I know."
    player "(Is he the one who was outside the coliseum causing trouble with the police?!?)"
    rebecca "He also said he'd stop [donflamingo.n], no matter what."
    rebecca "He's been fighting alone all this time, carrying that burden."
    rebecca "I don't want to lose him."
    rebecca "I don't want to lose you, too."
    pause 0.5
    rebecca "Now you're going to fight [logan.n] in just a few minutes, and I..."
    rebecca "I don't think you can win."
    rebecca "[logan.n] was too strong for me."
    rebecca "I saw you fight out there, and you're strong... but [logan.n] is on a different level than anyone you faced so far."
    rebecca "Even if by some miracle you beat [logan.n]..."
    rebecca "[donflamingo.n] is on a completely different level above that."
    rebecca "I... I'm sorry..."
    rebecca "But I just don't see how we can do this."
    player "I know you're scared, [rebecca.n]."
    player "I know you have every reason to doubt."
    player "But I need you to trust me right now."
    player "I won't lose. Not to [logan.n], and not to [donflamingo.n]."
    pause 0.5
    rebecca "I... I can't."
    rebecca "I can't watch someone else get hurt because of me."
    rebecca "Please... just walk away."
    rebecca "Leave the island, forget this fight."
    rebecca "If you stay and face him... he'll kill you."
    rebecca "And I... I can't..."

    menu:

        "Give a cocky grin":
            player "Heh. You're underestimating me."
            player "[logan.n]? I'll wipe the floor with that guy."
            player "I've fought far worse monsters than him, trust me."
            player "By the time I'm done, [logan.n] will wish he never stepped into that ring."
            pause 0.5
            rebecca "I can't tell if you're incredibly brave..."
            rebecca "Or just completely crazy..."
            player "Maybe a little of both."
            player "But crazy or not, I know what I can do."
            player "And I'm telling you: [logan.n] is going down."
            player "He'll pay for what he did to you."
            player "That's a promise."

        "Reassure her confidently":
            player "I'm not going to die, [rebecca.n]."
            player "I have too much to fight for."
            player "And I'm a lot tougher than I look."
            player "I promise you, I will win."

            $ rebecca_love += 1
            narrador "[rebecca.n] love +1"
            pause 0.5

            rebecca "You... you really mean that?"
            player "Every word."
            player "I've faced long odds before and somehow made it through."
            player "This won't be any different."
            rebecca "I... I want to believe you."
            rebecca "I really do."
            rebecca "You sound so sure of yourself..."
            rebecca "It's almost convincing."
            player "Believe it."
            player "I'll show you I can keep that promise."


    narrador "[rebecca.n] falls silent, She's unsure how to respond to your unwavering resolve."
    narrador "The crowd's cheers rumble through the walls, impatient for the fight to resume."
    narrador "You hear the announcer calling for the next contestants to enter the arena."
    pause 0.5
    rebecca "That's... the starting bell..."
    player "Sounds like they're calling me."
    player "I have to go."
    player "But before I do..."
    narrador "You step closer to her, gently lifting her chin with your hand so she meets your gaze."
    player "I'll win this fight, [rebecca.n]."
    player "I promise."
    player "And when I do, I'll come back for you."
    player "When I return victorious, I want you to tell me everything."
    player "No more holding back."
    player "Can you do that for me?"
    narrador "She gazes up at you, stunned. Her lip trembles as she searches your eyes."
    rebecca "I... I..."
    player "Do you trust me?"
    narrador "[rebecca.n] swallows hard and finally nods, fresh tears spilling over."
    rebecca "Alright."
    rebecca "If... if you win, I'll tell you everything."
    rebecca "I promise."
    player "Good."
    pause 0.5
    rebecca "Here, take this. It might be useful."

    $ minorpotion += 2
    narrador "+2 Minor Potions"

    player "Thank you... You're so kind!"
    player "Wait for me here."
    player "This won't take long."
    player "This victory will be for you, [rebecca.n]!!"
    pause 0.5
    rebecca "..." 
    rebecca "...Please, come back alive."


    $ _window_hide()
    stop ambient fadeout 1.0

    $ Dressrosa.h = 13
    $ _window_hide()
    $ ui_interface = True
    jump dr_ac_co_fighters_preparations
