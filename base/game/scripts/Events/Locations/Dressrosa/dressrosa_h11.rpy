# Version event 2
# Version game 0.37

label dressrosa_h11():
    $ ui_interface = False


    narrador "While you were wandering around the Colosseum after your last battle, you ran into an old acquaintance who was gravely injured."

    show riku riku_c2_wounded with Dissolve(0.5):
        xalign 0.5
        yalign 1.0

    player "[riku.n]!!!"
    player "But what the hell happened to you!!"
    player "It looks like a train ran you over!"
    riku "Hehe... Cough cough, koff— splurt..."
    riku "I don't think I look as bad as I actually feel..."
    riku "I can barely remember the times I've ended up in this state!"
    player "Well, you look... really bad..."
    riku "I tried to give it my all... but it still wasn't enough..."
    riku "Hahaha no one can't say this old man didn't try!!"
    pause 0.5
    riku "My rival... A grumpy, pointy-headed old man I met long ago... He gave me a good beating..."
    riku "He showed no mercy, he was pretty angry about something involving his grandkids apparently..."
    riku "Either way, if I can't even beat someone like that... How far out of my reach is [donflamingo.n]..."
    player "You're after [donflamingo.n] too?!"
    player "Looks like this guy has a fan club, and not the good kind..."
    riku "Anyone who knows what this guy did to the kingdom should be displeased with him, to say the least!"
    riku "Guhh—koff... koff... koff..."

    narrador "You see [riku.n] wobble and lose his balance for a few seconds, but he recovers quickly."

    riku "Damn... These wounds seem worse than I thought..."
    player "Why don't you rest a bit, man..."
    riku "Heh... There'll be time for this old man to rest later..."
    player "You should eat a lot, that's how I usually heal my wounds"
    riku "Hahaha... I don't know what kind of medicine you trust in, but I don't think that'll work for this old body..."
    player "If not, I think I heard there's an infirmary in the basement, maybe they could give you a quick check-up"
    riku "Mnmn... Koff... koff... The infirmary..."
    riku "I should investigate a bit... But I haven't had the chance, they don't let anyone in unless they're hurt."
    riku "I've heard strange things from the gladiators about that place... Apparently something weird is going on there..."
    player "Strange things?! What are you implying?"
    riku "I don't know, it doesn't matter now... I was heading to the arena, someone important to me should be about to fight!"
    pause 0.5
    narrador "You see [riku.n] stumble again, almost collapsing to the floor; he's gravely injured..."
    player "Hey hey, you'd better rest a bit in a corner... You won't last much longer..."
    riku "Ufff... You might be right..."
    pause 0.5
    riku "..."
    riku "Tell me [player.n]... you're a good person, I'm sure you can help me"
    player "Of course, we're friends remember..."
    riku "Good... The next fight... You must stop it, or at least try..."
    player "Why? Is something specific about to happen?"
    riku "One of the fighters is a gladiator named [rebecca.n]... She's a young girl taking on way more responsibility than she should..."
    player "(My warrior angel!)"
    riku "She's taking responsibility for things that aren't hers, it's a long story... But you have to stop her."
    riku "She's come very far and has proven her worth... But we're at the end now, the opponents are fearsome..."
    riku "Look at how this old man ended up..."
    riku "I'm afraid I can't protect her anymore... All I can do now is try to stop her..."
    riku "We have to make her listen to reason..."
    player "Mnmm... I've run into [rebecca.n] before, she's a good girl... Very determined."
    player "I doubt I can convince her to stop..."
    player "She has a clear goal to fulfill!"
    riku "I know! I know it well!!"
    riku "But she's young, it's an old man's duty to try to guide our young ones, you understand?!"
    riku "Her next opponent is a brute, a disgusting person, a monster!!"
    pause 0.5
    riku "I've seen what this criminal does to his opponents, he enjoys others' pain..."
    riku "[rebecca.n] could get seriously hurt... Or worse..."
    player "..."
    player "I can't promise anything, but I'll try!"
    player "I'll go look for her right now!"
    pause 0.5
    riku "Good... Koff, koff... Hraaagh!"
    riku "I'm counting on you, please try to make her listen to reason!"
    riku "I'll see if I rest here or head to the infirmary!"
    player "Get better old man, see you!"
    pause 0.5


    show screen screen_black with Dissolve(0.6)
    hide riku c2_wounded
    $ game.location = "dr_ac_co_fighters_preparations"
    scene BG locations:
        blur 3
    hide screen screen_black with Dissolve(0.3)

    narrador "You run toward the arena entrance and manage to catch up to [rebecca.n] just in time."

    player "[rebecca.n]!!!"

    show rebecca c2 helmet with Dissolve(0.8)

    rebecca "!!!"
    rebecca "[player.n] It's great to see you safe! I saw your last fight, you're really incredible..."
    player "Heh thanks, I'm glad to see you're alright too, looks like I made it in time."
    rebecca "In time for what?"
    player "You're about to fight, right... I was asked to talk to you and make you reconsider..."
    player "It's not something I'd normally say, but I understand the old man..."
    player "You need to stop, don't face your next opponent..."
    rebecca "!!!"
    rebecca "You know very well I can't do that..."
    player "I know, and you know I'm not the one who'd try to stop you..."
    rebecca "Hehe... I don't know you much, but I understand what kind of person you are... I know this isn't your idea..."
    rebecca "Alright then, tell me... Who asked you to do that?"
    player "An old gladiator... [riku.n]!"
    rebecca "[riku.n]?? I don't know anyone by that name... And besides, I know every gladiator here..."
    rebecca "I've been here for years, and there's no one who goes by that name..."
    rebecca "It's pretty strange, I haven't seen him in the locker rooms either..."
    player "Well... that does surprise me..."
    player "He talked like he was close to you..."
    rebecca "Heh... Well, that doesn't matter, because my answer wouldn't have changed anyway..."
    rebecca "I've already told you, [Dressrosa.n] is wrapped in a cold darkness that's slowly devouring the nation..."
    rebecca "There's little time left before the last of us still fighting finally fall..."
    rebecca "There are many others like me who are sacrificing themselves to save [Dressrosa.n]... And to save ourselves..."
    rebecca "I can't let them down now... I have to win and obtain the [HanaHanaFruit.n]..."
    rebecca "Become stronger and defeat [donflamingo.n]"
    player "(This guy... I should discuss this with the girls...)"
    rebecca "This isn't the time to lower our guard... No matter how hard the challenge, I have to keep going for them..."
    rebecca "For me..."
    rebecca "I'm sorry to go against you [player.n], but I can't listen to you... I must fight!"

    menu:
        "I understand there's no way to convince you":
            player "I understand there's no way to convince you..."  
            rebecca "No... I have an objective to fulfill, and I'll give everything I have to reach it!"

        "That's the spirit!":
            player "That's the spirit [rebecca.n]!"
            player "There's no reason to doubt... Give it your all!"
            player "No matter what happens, I'll be supporting you."
            rebecca "Thank you, really, thank you [player.n]!"
            rebecca "Your words give me strength for what's coming!"

            $ rebecca_love += 1
            narrador "[rebecca.n] love +1"

    pause 0.5
    rebecca "Alright, everything's been said then!"
    pause 0.5

    narrador "In the distance, a bell rings, calling a new round of fighters..."

    player "The bell rang..."
    rebecca "Looks like it's time..."
    player "Good luck [rebecca.n], I'll be watching from the barracks!"
    player "I'll be cheering for you, you know you can count on me!"
    rebecca "Thank you [player.n], we'll see each other again!"



    $ _window_hide()
    show screen screen_black with Dissolve(0.6)
    show events dressrosa h6 h6_gatz
    play ambient "ring" fadein 1.0
    hide screen screen_black with Dissolve(0.3)


    gatz "{size=40}Weeeeeeeeeelcome back, ladies and gentlemen, toys and dolls!{/size}"
    gatz "{size=40}Welcome everyone once again to the Corrida Coliseum!{/size}"

    pause 0.5
    player "Fiuuu... good thing I made it just in time..."
    player "Being a competitor, there are plenty of good places to watch the battle in the barracks..."
    player "From here I'll be able to see [rebecca.n]'s fight perfectly."
    player "It'll be the first fight of hers I get to see!"
    pause 0.5
    player "I'm sorry I didn't keep my promise to the old man…"
    player "But she's a determined woman, I couldn't clip her wings… I'll make sure to step in if anything is about to happen."
    pause 0.5
    gatz "Welcome once again, everyone, to the battlefield..."
    gatz "Only a few fights remain before we reach the grand final... And today we have a rather special one..."
    gatz "Although, judging from the crowd... there's a clear favorite today!!"
    gatz "On one side, we have the obvious favorite... One of the most violent competitors in the entire tournament..."
    gatz "A big brute who captures everyone's attention whenever he fights."
    gatz "He's the commander of the army of the Southern Kingdom of Majiatsuka, {size=40}{outlinecolor=#8b0000}{color=#ff6666}Roooollin Loooogan{/color}{/outlinecolor}!!!{/size}"
    unknown "[logan.n]!! [logan.n]!! [logan.n]!!"
    gatz "{size=40}Listen to the crowd... What an incredible atmosphere, such a strong support!!!{/size}"
    gatz "Is it due to his own merit... or because of who he's facing?..."
    pause 0.5
    player "What is he talking about... What is he insinuating about [rebecca.n]?!"
    pause 0.5

    gatz "On the other side we have a woman... whose fame precedes her..."
    gatz "Some say bad weeds grow high, and here's the proof..."
    gatz "{size=40}It's the Phantom Princess... [rebecca.n]!!!!{/size}"
    pause 0.5
    player "Phantom Princess?!... [rebecca.n]?!"
    pause 0.5
    gatz "[logan.n] versus [rebecca.n]!!!"
    gatz "{size=40}What an incredible fight we're going to have today!!!!{/size}"
    pause 0.5
    $ black_to_img("events dressrosa h11 h11_1")

    unknown "Booooooo.... Get out!!!"
    unknown "Booo... Rot in hell... You should die, [rebecca.n]!"
    unknown "Get loooost... You disgust me... Make her pay..."
    pause 0.5
    player "{size=40}What did you say, bastard? Come here, I'll kick your ass!!{/size}"
    pause 0.5
    unknown "Just give up already!!"
    pause 0.5
    player "..."
    player "Again and again... these people just won't stop booing her."
    player "Once again, people are attacking [rebecca.n]... Same thing happened in the locker room with the gladiators..."
    pause 0.5
    unknown "You're a complete disgrace... I hope they kill you... We hate you and your whole family!"
    unknown "You're the shame of [Dressrosa.n]... Burn her alive just like her grandfather did to our kingdom!"
    player "?!?!"
    player "The shame of [Dressrosa.n]... And her grandfather burning and attacking [Dressrosa.n]..."
    player "Don't tell me... The story [riku.n] told me!!!"
    pause 0.5
    player "... Don't tell me [rebecca.n] is part of the former royal family... The Phantom Princess!"
    pause 0.5
    gatz "I've never heard boos this loud."
    gatz "The crowd grows furious as they welcome the Phantom Princess [rebecca.n] with contempt."
    player "Now it all makes a bit more sense but... If that story is real... People don't know the truth!"
    pause 0.5
    gatz "While the crowd continues to boo..."
    gatz "[rebecca.n] takes an offensive stance, ready for battle!"
    gatz "Look at that focus!!"
    pause 0.5
    rebecca "(Sir Soldier, you never gave up and I won't either.)"
    rebecca "(I can't afford to lose today...)"
    rebecca "(I have to win no matter what!)"
    rebecca "(I'll get the [HanaHanaFruit.n] and I'll kill [donflamingo.n]!)"
    rebecca "{size=25}Alright... This won't be easy... But I won't back down!!{/size}"
    rebecca "..."
    rebecca "(Sir Soldier... Today it will be me who protects you... I promise you!!!)"

    $ black_to_img("events dressrosa h11 h11_2", hide="events dressrosa h11 h11_1")

    unknown "{size=40}[logan.n]!! [logan.n]!!{/size}"

    gatz "The crowd roars with excitement as the young fighter faces such a fearsome opponent as [logan.n]."
    gatz "The size difference between them is obvious, but [rebecca.n] doesn't seem intimidated."
    player "(That guy... he's a damn giant!)"


    $ _window_hide()
    show events dressrosa h11 h11_2:
        xalign 0.5
        yalign 1.0
        linear 3.0 yalign 0.0

    pause 3.0

    show events dressrosa h11 h11_2:
        xalign 0.5
        yalign 0.0

    pause 1.0

    logan "You're pretty attractive... But it seems the whole country hates you..."
    logan "Poor thing, hahahaha, everyone despises you."
    rebecca "..."
    logan "Time to tear you to pieces..."
    logan "How about I snap your neck first?"
    logan "Or maybe your spine would be better?"
    player "{size=40}Don't be afraid, [rebecca.n]!!! Face him, there's nothing to fear!!{/size}"
    logan "You've got such a sexy body... You're like a little doll..."
    logan "Maybe I could have some fun with you first..."
    logan "You know... enjoy that beautiful body of yours..."
    unknown "Yesss!!! Humiliate her first!!"
    player "{size=40}What did you say!! If you touch her with those intentions, you'll have to deal with me!!{/size}"
    pause 0.5
    player "(Damn, he doesn't even blink... he probably can't even hear me with all the crowd noise and the distance.)"
    pause 0.5
    logan "Heh... Let's not make this complicated, why choose just one..."
    logan "I say I should break you completely... like the beautiful doll you are."
    unknown "Yesss!!! Tear her apart! Make her regret being born!"

    $ black_to_img("events dressrosa h11 h11_3", hide="events dressrosa h11 h11_2")

    pause 1.0

    gatz "Despite how intimidating the enemy is... [rebecca.n] bravely charges toward him!!"
    pause 0.5
    gatz "{size=40}What an impressive sight!{/size}"
    pause 0.5
    gatz "!!!"
    gatz "But watch out..."
    gatz "[logan.n] launches a powerful attack toward [rebecca.n]!"


    #sound of burst

    $ black_to_img("events dressrosa h11 h11_4", hide="events dressrosa h11 h11_3")

    pause 1.0

    gatz "{size=40}Amazing!{/size}"
    gatz "[rebecca.n] dodges her opponent's attack with lightning speed!"
    gatz "The Phantom Princess is quite lucky!!"
    gatz "They say [logan.n]'s grip strength is over 500 pounds..."
    gatz "If [logan.n] catches her... That will be the end!"
    pause 0.5
    rebecca "(I can't let him catch me... I have to dodge at all costs!)"

    $ black_to_img("events dressrosa h11 h11_5", hide="events dressrosa h11 h11_4")

    pause 1.0

    logan "Little doll... You've got good moves. I'm going to enjoy it so much when I catch you..."
    logan "The sweet sound of bones cracking..."
    pause 0.5
    logan "Why don't you just surrender already and stop fighting... You might even enjoy it..."
    rebecca "In your dreams!! I'll defeat you..."

    $ black_to_img("events dressrosa h11 h11_6", hide="events dressrosa h11 h11_5")

    pause 1.0

    gatz "{size=40}And there goes the Phantom Princess!!!{/size}"
    gatz "[rebecca.n] scurries across the sand like a sewer rat!"
    gatz "Strike after strike crashes into the hard arena floor without hitting its target..."
    gatz "But [logan.n] doesn't lose track of her..."

    if Haki.h >= 2:
        player "Incredible... That feeling... That aura around [rebecca.n]'s body..."
        player "It's like [rayleigh.n] explained... The speed she's dodging with isn't coincidence..."
        player "She must be using some level of {outlinecolor=#00BFFF}{color=#ffffff}Observation Haki{/color}{/outlinecolor}..."

    pause 0.5
    gatz "The storm of blows continues..."
    gatz "How long will this hateful woman hold out... I don't think she can keep up!!!"
    pause 0.5
    gatz "[logan.n] easily keeps up with her pace across the arena, not letting her escape."
    pause 0.5
    player "Damn it... This isn't looking good... [rebecca.n] is slowing down..."
    player "And she can't get close either... If this keeps up..."
    pause 0.5
    gatz "{size=40}Fiiiiiinally!!!{/size}"
    
    $ black_to_img("events dressrosa h11 h11_7", hide="events dressrosa h11 h11_6")

    pause 1.0

    gatz "{size=40}A direct hiiiiit!!!{/size}"
    gatz "[logan.n] cornered the infamous Princess and struck her full on..."
    gatz "And sent her flying!!!"
    pause 0.5
    gatz "Even though [rebecca.n] managed to guard... The damage must be serious... And not only that... Look to the side of the arena..."

    $ black_to_img("events dressrosa h11 h11_8", hide="events dressrosa h11 h11_7")

    rebecca "My sword!!!!"
    gatz "The impact sent [rebecca.n]'s weapon flying..."
    gatz "{size=40}[rebecca.n] is now unarmed, what will become of her now!?!?{/size}"
    pause 0.5
    gatz "Without hesitation, [rebecca.n] decides to rush to retrieve her weapon!!"

    $ black_to_img("events dressrosa h11 h11_9", hide="events dressrosa h11 h11_8")

    pause 1.0

    logan "Stop right there!"
    rebecca "!!!!"
    gatz "{size=40}But [logan.n] won't allow it!!!{/size}"

    $ black_to_img("events dressrosa h11 h11_10", hide="events dressrosa h11 h11_9")

    pause 1.0

    logan "When I've got my prey in sight, I never let her escape! Heh heh heh"
    gatz "Now that [rebecca.n] is without her sword, she's completely defenseless!!!"
    gatz "She has to face a much taller and heavier opponent head-on... with bare fists..."
    gatz "This doesn't look good for the Phantom Princess..."
    gatz "And by trying to retrieve her weapon, she ended up in a very bad position..."

    $ black_to_img("events dressrosa h11 h11_11", hide="events dressrosa h11 h11_10")

    pause 1.0

    gatz "It's like a snake cornering its prey..."
    gatz "{size=40}[rebecca.n] has nowhere to run!!!{/size}"

    $ black_to_img("events dressrosa h11 h11_12", hide="events dressrosa h11 h11_11")

    pause 0.5

    gatz "This is it—[rebecca.n] has been caught!!!"
    pause 0.5
    unknown "{size=40}[logan.n]!! [logan.n]!!{/size}"
    pause 0.5
    gatz "{size=40}The crowd erupts in cheers... This will be over soon!!{/size}"
    
    $ black_to_img("events dressrosa h11 h11_13", hide="events dressrosa h11 h11_12")

    pause 1.5

    logan "Heh heh heh"
    pause 1.5
    logan "Such beauty!!!"
    logan "I've never held such a beautiful trophy in my hands!!!"
    logan "How soft and tender your body is... That gorgeous waist..."
    logan "And these huge, obscene breasts you have..."
    pause 0.5
    gatz "All that's left is to wonder which move [logan.n] will use to finish his opponent..."

    $ black_to_img("events dressrosa h11 h11_14", hide="events dressrosa h11 h11_13")

    pause 1.5
    logan "What a delight... what a deliiciiious treat... Just thinking about the things I'd do to you excites me..."
    logan "Such a delight... I'm tempted by so many things!!!!"
    player "(That bastard... When I get my hands on him...)"
    logan "What should I do?!?!"
    logan "Maybe I'll crush you like a bug..."
    logan "Or maybe my favorite method..."

    $ black_to_img("events dressrosa h11 h11_15", hide="events dressrosa h11 h11_14")
    show events dressrosa h11 h11_15 at vibration
    pause 1.5

    rebecca "{size=40}Aaaaaahhhhh.... Mnnnnnnn.... Aaaaaah{/size}"
    logan "Great scream, keep going, don't stop..."
    player "(Nooooo... that bastard... Should I jump in now!?!)"
    logan "Heh heh heh"
    logan "I'm going to squeeze the life out of you little by little... Don't you dare die too fast..."
    pause 0.5
    gatz "Could this be the end of her undefeated streak... and of her life as well!!!"

    $ black_to_img("events dressrosa h11 h11_16", hide="events dressrosa h11 h11_15")
    show events dressrosa h11 h11_16 at vibration
    pause 1.5

    logan "That blood... those tears... They excite me so much, keep going... Cry, beg for mercy..."
    rebecca "{size=15}Aaahhh...{/size}"
    pause 1.0
    rebecca "(Sir soldier... I'm sorry... I... I failed...)"
    logan "!!!"
    logan "Hey, don't stop... You're fainting, damn it... You need to suffer for a good while longer..."
    logan "{size=40}Come on, screeeeam!!{/size}"
    pause 1.0
    rebecca "..."
    pause 0.5
    logan "Ugh, how annoying... so boring... looks like she died already..."

    $ black_to_img("events dressrosa h11 h11_17", hide="events dressrosa h11 h11_16")

    pause 1.5

    gatz "Very disappointed, [logan.n] decides to finish it and slams her hard against the ground!"

    $ black_to_img("events dressrosa h11 h11_18", hide="events dressrosa h11 h11_17")

    pause 1.5

    gatz "{size=40}The gladiator [rebecca.n] has been defeated!{/size}"
    gatz "{size=40}Justice has once again triumphed in this beautiful Coliseum!!!{/size}"
    unknown "{size=40}[logan.n]!! [logan.n]!! [logan.n]!! [logan.n]!!{/size}"
    pause 0.5
    player "(This won't end like this!!! But I need to go find [rebecca.n] first!)"


    $ _window_hide()
    stop ambient fadeout 1.0

    $ Dressrosa.h = 12
    $ _window_hide()
    $ ui_interface = True
    jump dr_ac_co_fighters_preparations
