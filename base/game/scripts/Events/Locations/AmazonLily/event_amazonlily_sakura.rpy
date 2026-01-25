# Version event: 3
# Version game: 0.10

label event_amazonlily_sakura:

    player "Kuja Pirates, hold on a moment and listen to us!"

    unknown "Hahaha, a man dares to speak here!"

    unknown "A man won't tell us what to do! Turn around or face the consequences..."

    player "(Damn it, I didn't think the hatred towards men was this intense on this island...)"

    player "(What [robin.n] told us was true, there's a lot of xenophobia towards men...)"

    robin "We have the [SakuraFlower.n]!!"

    unknown "Mnmnm!?!?"

    unknown "What did you say, woman?!?"

    robin "That's right!! We have what you're looking for!!"

    unknown "And how do you know we need that flower?"

    robin "During our stay at [ThrillerBark.n], we happened to cross paths with your empress, [hancock.n]..."

    robin "And we overheard that you needed the [SakuraFlower.n]..."

    robin "That's why we came here!!"

    unknown "Mnmn... I see, wait a moment..."

    unknown "Call the captain, it's urgent!!..."

    player "(Excellent, well said, [robin.n]!!)"

    window hide
    window auto
    pause 0.5

    show screen screen_basic_black with Dissolve(0.8)
    narrador "A few moments later..."

    hide screen screen_basic_black with Dissolve(0.8)


    unknown "Pirates!!! The captain has granted you entry... You may proceed to discuss the matter!"

    unknown "Open the gate!!!"

    robin "Excellent, let's move forward!"

    nami "That was too easy... right?"

    yamato "It seems they really need this flower, but let's stay alert anyway!!"

    player "Forward, to the island of women!!"

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    $ game.location = "amazon_lily_city"
    scene BG locations:
        blur 3
    stop ambient fadeout 2.0
    hide screen screen_black with Dissolve(0.8)
    

    robin "Wow, such extravagant and beautiful architecture..."
    pause 0.5
    yamato "There are weapons and warrior women everywhere!!... I didn't think there would be so many!!"

    player "I don't see a single man!..."

    player "(Everywhere I look, I only see women!!! And they're all beautiful!!)"

    player "All eyes are on me..."

    nami "Captain!! Someone's coming!!"

    window hide
    window auto

    show marguerite at center with dissolve

    pause 1

    call set_name_marguerite from _call_set_name_marguerite

    marguerite "I'am [marguerite.n], a member of the Kuja Pirates..."

    marguerite "Most of my senior sisters left with [hancock.n] a few days ago..."

    marguerite "I'm currently in charge here!"

    player "Hello, I am [player.n]"

    if player_goal == "Pirate":
        player "And I will be the King of the Pirates!"
    elif player_goal == "Swordsman":
        player "And I will be the greatest swordsman in the world."
    elif player_goal == "Harem":
        player "And I will have the largest harem in the world."
    elif player_goal == "King":
        player "And I will be the King of the World."

    marguerite "What a strange man..."

    marguerite "As I mentioned, the Empress isn't here at the moment."

    marguerite "She's still searching for the flower, we urgently need it to cure a strange illness..."

    marguerite "The guards told me you have the [SakuraFlower.n] with you..."

    player "We have several samples too!"

    marguerite "I should verify that..."

    marguerite "I need you to give me the [SakuraFlower.n] please..."

    player "Mnmnmnm, I'd like to discuss it directly with [hancock.n]... When will she return?"

    marguerite "As I said, she's on a very important mission... We can't just call her back so easily..."

    marguerite "If you show me the flowers you have, and I can confirm their authenticity..."

    marguerite "If they're real... I could summon her here as soon as possible..."

    player "That's a good point! We'll trust you... Show her the plants, [robin.n]."

    robin "Sure, Captain! Here you go, you can easily verify they're real..."
    
    $ sakuraflower -= 1

    narrador "-1 [SakuraFlower.n]"

    marguerite "I never imagined it would look like this..."

    marguerite "I can't tell if it's real or not, our medics will need to examine it..."

    player "Perfect, we'll wait for the results... Maybe we could explore the area in the meantime... Perhaps..."

    marguerite "Wait right there, man!!"

    marguerite "I might not know about the plant... But I'm very clear on the rules here, and I know that in [AmazonLily.n], we do NOT accept MEN!"

    marguerite "Ladies, surround them!!!"

    pause 0.5
    
    narrador "In an instant, without any warning, your entire crew was surrounded by dozens of Amazons."

    narrador "With no chance to fight or explain..."

    narrador "The Amazons took you all as prisoners!"

    show screen screen_black with Dissolve(0.8)
    hide marguerite
    $ game.location = "amazon_lily_prision"
    scene BG locations:
        blur 3

    show layer_prison_bars zorder 5
    hide screen screen_black with Dissolve(0.8)

    show nami anger at center with dissolve

    nami "Damn it, Captain, what are we going to do now!!!"

    show yamato anger with dissolve:
        yalign 1.0
        xalign 0.10
    
    yamato "I knew it was a bad idea to go in so deep... The location was horribly disadvantageous for us!"
    yamato "I'll try to find some weakness in this cell back here!!"
    
    hide yamato with dissolve
    pause 0.5

    show nami anger:
        linear 0.4 xalign 0.90

    pause 0.4

    show robin at center with dissolve

    robin "Calm down, [nami.n], this is just a misunderstanding. Once they discover the flower is real, they'll let us go."

    robin "If not, maybe we could negotiate something... Or in the worst case..."

    nami "We'll be Amazon food!!!!"

    yamato "They're not cannibals!!!!... They're just Amazons!!!..."

    nami "And how do you know?... How many times have you been here before!?!"

    player "Calm down, girls!! Let me think of something!!"   

    window hide
    window auto
    pause 0.5

    show screen screen_basic_black with Dissolve(0.8)

    narrador "One day later..."

    $ game.clock.sleep()

    hide robin

    show nami anger at center

    show yamato anger:
        yalign 1.0
        xalign 0.90

    hide screen screen_basic_black with Dissolve(0.8)

    pause 0.5

    nami "How long are we going to be here!?!"

    yamato "The bars seem too strong, but we could destroy the roof or a wall!!"

    nami "Wait!! Don't do anything, it's the woman from [ThrillerBark.n].... [hancock.n]!!!"

    show hancock annoyed zorder 6 with dissolve:
        yalign 1.0
        xalign 0.10

    hancock "WHAT IS THIS?!?!"

    hancock "Why are my guests still locked up here!?!"

    hancock "After all my travels, I couldn't find that damn flower anywhere..."

    hancock "I was losing hope..."

    hancock "And then they came all the way here and brought it..."

    hancock "And you repay them by locking them up in prison!?! This is unforgivable!!!"

    player "(She's truly a beauty, even when she's angry!!!)"

    hancock "Release them immediately!!!"

    show layer_prison_bars zorder 5: 
        linear 0.6 yoffset -1080
    
    pause 0.4

    show nami happy with Dissolve(0.2)
    show yamato happy with Dissolve(0.2)
    with dissolve

    nami "We're finally free..."

    yamato "They've finally come to their senses..."

    show hancock neutral with Dissolve(0.2)

    hancock "I apologize for what happened..."

    hancock "Please, follow me to the castle... This way, follow me!"

    hide layer_prison_bars

    show screen screen_black with Dissolve(0.8)
    $ game.location = "amazon_lily_palace"
    scene BG locations:
        blur 3
    hide screen screen_black with Dissolve(0.8)

    player "(Wow, what a luxurious place!!)"
    player "(I wouldn't mind if this were one of my summer homes...)"
    
    show screen screen_black with Dissolve(0.8)
    $ game.location = "al_palace_room"
    scene BG locations:
        blur 3

    show hancock neutral at center
    hide screen screen_black with Dissolve(0.8)

    hancock "First of all, thank you very much for your help... I'm really very grateful!!!"
    show hancock happy with Dissolve(0.2)  
    hancock "It's really difficult to find the [SakuraFlower.n], and you managed to do it!!!"

    player "(Well... Actually, it wasn't that hard...)"

    hancock "With the samples you brought, we were able to make the right medicine!!"

    hancock "I'm eternally in your debt!!"

    player "(I can think of several ways to settle that debt, hehe!)"

    player "No need to thank us! But what was the problem?"
    show hancock neutral with Dissolve(0.2)
    hancock "During one of our trips, one of my sisters came across a strange flower..."

    hancock "She quickly developed a fever, and we couldn't find a solution!"

    hancock "She's been in that state for nearly a month, and it was getting harder and harder to control the illness..."
    show hancock happy with Dissolve(0.2)
    hancock "But now, thanks to you, my sister is recovering quickly from her illness!!"

    hancock "I'm eternally in your debt!!"

    player "(What a beautiful smile she has!! It's no wonder she's a pirate empress!)"

    player "We're glad we could help then!!"
    show hancock neutral with Dissolve(0.2)
    hancock "I apologize again for what happened... Someone wants to say something to you..."

    hancock "[marguerite.n], come in right now!!!"

    show hancock:
        yalign 1.0
        linear 0.4 xalign 0.15

    pause 0.4

    show marguerite with dissolve:
        yalign 1.0
        xalign 0.85

    marguerite "I-I'm so sorry!"

    marguerite "Please, I ask for your forgiveness!"

    marguerite "I acted recklessly!"

    hancock "......"
    show hancock serious with Dissolve(0.2)
    pause 1.0
    player "(So scary!! She doesn't seem angry, but my instincts tell me to stay alert!!)"

    hancock "It's alright now... My honest [marguerite.n]..."

    hancock "If there's something I value highly, it's honesty..."

    hancock "Tell me... Do you want me to forgive you too???"

    marguerite "Y-yes..."

    hancock "......"

    $ renpy.music.set_volume(0.0, delay=2, channel='music')

    hancock "Mero Mero Mellow"

    window hide
    window auto

    show marguerite c1_stone with flashHancock

    show marguerite:
        yalign 1.0
        xalign 0.85
        linear 0.1 xalign 0.855
        linear 0.1 xalign 0.845
        linear 0.1 xalign 0.855
        linear 0.1 xalign 0.845

    pause 0.6

    $ renpy.music.set_volume(1.0, delay=2, channel='music')

    player "(W-what, what just happened!?!?!... A statue?... Is that [marguerite.n]??)"

    player "But how...."

    robin "It's the power of a Devil Fruit, Captain!!... The [MeroMeroFruit.n]!! It can petrify its opponents!"

    player "Wow... That explains everything..."

    player "(So it's a Devil Fruit...)"

    player "(This woman is truly dangerous...)"

    pause 0.5
    hancock "Now that's taken care of... Take her away, I'll return her to normal later..."
    pause 0.5
    hide marguerite with dissolve

    show hancock:
        yalign 1.0
        xalign 0.15
        linear 0.4 xalign 0.5

    show hancock neutral with Dissolve(0.2)
    hancock "In [AmazonLily.n], the entry of men is forbidden, not even I can break that rule..."

    show hancock happy with Dissolve(0.2)
    hancock "But you were really brave to come here, [player.n]... And I'm in your debt for saving my sister..."   

    hancock "For now, I'll allow you and your group to enter and leave the island..."

    hancock "You're free to explore the city until further notice..."

    show hancock neutral with Dissolve(0.2)
    hancock "Later on, we'll see if you're not only brave, but if you can show me something more!!"

    player "(You'll love it!! You'll be mine!!!)"

    hancock "If there's nothing else you want to say, you can go."

    $ AmazonLily.h = 1
    jump al_palace_room



