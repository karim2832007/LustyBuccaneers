# Version event: 5
# Version game: 0.31

label ar_alubarna_h():
    $ ui_interface = False
    
    show vivi serious at center with dissolve

    vivi "Well, we've finally arrived. This is Alubarna, the capital of the Kingdom of Arabasta."
    vivi "Like any capital, it's a big place full of people."
    vivi "It's easy to get lost, so stay close to me... We must take the fastest route possible..."

    if not ar_rebel_army:

        vivi "Chaos seems to be spreading everywhere already..."
        vivi "The rebels must have started clashing in the streets with the royal forces..."
        vivi "I have to stop the bloodshed no matter what... We must hurry!"

    vivi "We need to go to the royal palace."
    vivi "I know a shortcut I used as a child with [koza.n]."
    vivi "It's the fastest way to get there while avoiding detection."

    player "Alright!! On our way, let's go defeat [crocodile.n]!"

    vivi "I'm glad to see you so confident... He's a very difficult enemy, please don't underestimate him..."
    vivi "I've been thinking about this day for a long time... And I came prepared..."
    vivi "Before the fight, I need to tell you something."
    vivi "When I infiltrated the Baroque Works organization, I tried to gather all the information I could about its leader."
    vivi "And my efforts paid off..."
    vivi "I discovered one of [crocodile.n]'s secrets, and it's that his strength doesn't just come from his intelligence, violence, and leadership..."
    vivi "[crocodile.n] is a Devil Fruit user..."

    player "One of those fruits that give you supernatural powers?"

    vivi "Exactly..."
    vivi "[crocodile.n] is a user of the Suna Suna no Mi fruit."
    vivi "This isn't just any fruit, it has a strange power that allows him to control sand at will."
    vivi "His body turns into sand, and he can manipulate it as he pleases. In these deserts, he's nearly invincible..."
    vivi "But even though he's very dangerous, I discovered that he has a weakness..."
    vivi "Water!"

    player "Water?!"

    vivi "Yes, water is his weakness."
    vivi "If we manage to get him wet, he'll lose much of his power and become vulnerable, making the fight easier."
    vivi "So if it were to rain when we face him, the water would weaken him."

    show robin:
        yalign 1.0
        xalign 0.05

    robin "The Dance Powder!"

    vivi "Exactly, that's precisely my plan... With Dance Powder, we can make it rain."
    vivi "With the terrain in our favor, we'll have the advantage..."

    show nami serious:
        yalign 1.0
        xalign 0.95

    nami "Captain!! The situation is too delicate to be thinking about that..."
    player "Mnmnm... I'll do it only because [vivi.n] is asking for it..."

    vivi "Thank you, [player.n], I really appreciate everything you're doing!"
    
    $ vivi_love += 2
    narrador "[vivi.n] Love +2"    
    
    nami "Alright, back to the topic..."
    nami "Where can we find Dance Powder?"

    vivi "Do you remember when they tried to frame my father with a shipment of Dance Powder?"
    vivi "According to information [igaram.n] obtained recently..."
    vivi "Part of that shipment is stored in the Royal Palace as confiscated goods."

    player "Perfect, then lead us to where the Dance Powder is."
    vivi "Alright!! Follow me."
    
    window hide
    show screen screen_basic_black with Dissolve(0.6)

    narrador "[vivi.n] leads you through different alleys and passageways."
    narrador "Until reaching a secret entrance to the royal palace."
    narrador "Upon entering the palace, [vivi.n] takes you to a room with the confiscated shipment."

    $ game.location = "ar_alubarna_palace_room"
    scene BG locations:
        blur 3

    hide screen screen_basic_black with Dissolve(0.3)
    window auto

    show vivi serious at center with dissolve

    vivi "We've arrived. Here is the Dance Powder."

    vivi "Besides that, I'd like to give you these 10 Minor Potions. They'll be useful in battle."

    $ minorpotion += 10
    narrador "+10 Minor Potions"

    vivi "I know it's not much, but it's all I have."

    player "Thank you so much, [vivi.n]! This will be more than enough!"

    player "Now let's go outside, prepare the rain, and defeat [crocodile.n]."

    narrador "After a few minutes of planning, they gathered what they needed and prepared the battlefield for the confrontation."

    window hide
    show screen screen_black with Dissolve(0.6)

    $ game.location = "ar_alubarna_shortcut"
    scene BG locations:
        blur 3

    hide screen screen_black with Dissolve(0.3)
    window auto

    robin "Do you hear that?!?"

    show vivi anger at center with dissolve

    vivi "It's the voice of [crocodile.n]!"
    vivi "He's already here, we must hurry!"

    vivi "You prepare the rain, I'll handle distracting him."

    player "It's dangerous, you shouldn't face him alone."

    vivi "Don't worry, I just need to buy some time."

    player "Understood, we'll take care of preparing the rain."


    show vivi anger:
        linear 0.5 xalign 1.1
        linear 0.5 yalign 1.0

    show cobra c1_wounded with dissolve:
        xalign -0.3
        yalign 1.0

    show crocodile at center with dissolve

    with dissolve

    vivi "Father!"

    crocodile "Well, well, well, I didn't expect to see you here, Miss Wednesday."

    vivi "Don't ever call me that again!"
    vivi "I'm no longer part of your horrible criminal organization!"

    crocodile "Ahahahahah"
    crocodile "What a shame... I didn't want you to suffer, you should've stayed as a prisoner in peace..."
    vivi "And watch as you get away with everything?!?... Never!"
    vivi "What did you do to my father!?!"
    vivi "Why is he in that terrible state?"
    crocodile "You didn't think it was easy to capture him, did you...?"
    crocodile "Don't worry, princess, the king will live... For now..."
    crocodile "Obviously, someone warned him about the situation, and he was already prepared... It was probably [pell.n], who mysteriously escaped from my grasp..."
    crocodile "You being here makes me think..."
    crocodile "You're probably responsible for all of this..."
    crocodile "Either way, it was of little use..."
    crocodile "Ever since you escaped from [CactusIsland.n], I knew you'd be a problem..."
    crocodile "Now I understand why there have been so many setbacks in my plans lately..."
    
    if ar_rebel_army:

        crocodile "The fact that chaos hasn't erupted in the city must be your doing..."
        crocodile "I thought I had that [koza.n] dancing in the palm of my hand, seems I was overconfident..."
        crocodile "Anyway, that's not a problem, I'll deal with the rebels later..."

    cobra "I'm sorry, [vivi.n], I couldn't take advantage of the opportunity you gave us, despite the fact that you risked your own life."

    crocodile "Ahahah, what a sad reunion!"
    crocodile "Let me make it clear that I don't intend to let either of you live."
    crocodile "When a kingdom dies, it's normal for its royal family to perish as well."
    crocodile "This palace will soon be my home."

    vivi "Why are you doing this? I don't think you're just interested in the royal palace."

    crocodile "Ahahahahah"
    crocodile "You're a smart girl, obviously this isn't just about social status..."
    crocodile "Before you die, king, you must tell me something..."
    crocodile "All of this, this civil war I orchestrated, serves only my greater objective."
    crocodile "[cobra.n]..."
    crocodile "Where is Pluton?"

    cobra "You scoundrel..."
    cobra "How do you know that name?!?"

    crocodile "Ahahahahah"

    vivi "What are you talking about?"
    vivi "What the hell is Pluton?"

    crocodile "They say a single shot from that weapon can destroy an entire island."
    crocodile "And that it's the most destructive weapon of ancient times, which is why it bears the name of a god."
    crocodile "It must be hidden somewhere in [Arabasta.n]."

    vivi "An ancient weapon?"
    vivi "(It must be a secret of the royal family... My father never spoke to me about this, does he really know where to find it?)"

    crocodile "With this weapon, my influence will expand across the world"
    crocodile "And over time, I will have more power than even the world government"

    cobra "The world government will not allow a criminal like you to have that power"

    crocodile "Ahahahahah"
    crocodile "That's probably true, which is why I need Pluton"

    cobra "I have no knowledge of its whereabouts"
    cobra "I don't even know if such a powerful weapon truly exists in this country"
    cobra "I have nothing to help you with, you have already defeated me... I am telling you the truth!"

    crocodile "I see, it doesn't seem like you're lying"
    crocodile "I thought this might happen"
    crocodile "I also know that its existence is widely doubted"
    crocodile "Obviously, even less is known about its whereabouts..."

    crocodile "Then... I'll change my question"
    crocodile "Where is the Poneglyph?"

    cobra "The Poneglyph?!?"
    robin "(!!!!)"
    robin "(The Poneglyph of Alabasta... Is it real? I knew it!!)"

    $ show_rain()

    crocodile "Rain?"
    crocodile "How is this possible... What is happening..."

    hide cobra
    hide vivi
    with dissolve

    player "Crocodile... We finally face each other!"

    crocodile "Mnmmnm... And who are you..."
    player "I am [player.n]"

    if player_goal == "Pirate":
        player "And I will be the King of the Pirates!"
    elif player_goal == "Swordsman":
        player "And I will be the greatest swordsman in the world."
    elif player_goal == "Harem":
        player "And I will have the largest harem in the world."
    elif player_goal == "King":
        player "And I will be the King of the World."

    crocodile "Hahahaha how ridiculous... You don't even know what you're saying, rookie." 
    crocodile "You must be the one who helped the princess escape..."
    crocodile "It's unbelievable that my subordinates allowed this... I need to review the lower ranks..."
    crocodile "I understand what you're trying to do with all this... This rain must be artificial..."
    crocodile "But unfortunately, you are underestimating me..."
    crocodile "You're a complete rookie who doesn't know the power of your rivals at sea..."
    crocodile "Mr.1, Mr.2, get rid of him... I have no time to waste on him..."

    hide crocodile with dissolve

    show expression enemy_mr1.image:
        xalign 0.2
        yalign 0.5
    
    show expression enemy_mr2.image:
        xalign 0.8
        yalign 0.5

    with dissolve

    player "Damn it, looks like you didn't come alone"

    if ar_rebel_army:
        call ar_alubarna_h_army from _ar_alubarna_h_army

    else:
        call ar_alubarna_h_noarmy from _ar_alubarna_h_noarmy


    window hide
    show screen screen_black with Dissolve(0.6)

    hide crocodile
    hide koza

    $ enemy_figth.reset()
    show expression enemy_mr0.image:
        xalign 0.5
        yalign 0.5

    hide screen screen_black with Dissolve(0.3)
    window auto

    crocodile "Damn bastard, looks like it's just you and me now!"
    player "Hhehe, it seems so!"
    crocodile "All the reports from my subordinates have told me a lot about you..."
    crocodile "You've been facing me since [CactusIsland.n]... Meddling in every step I take..."
    crocodile "Freeing the princess, fighting my subordinates, infiltrating my casino..."
    crocodile "Saving this damn kingdom..."
    crocodile "I have to admit that I underestimated you... But I want to understand..."
    crocodile "What do you want... Why do you keep fighting?!"
    player "You still haven't returned what you took..."
    crocodile "What I took?"
    crocodile "The money?!?..."
    crocodile "The fame?!?!..."
    crocodile "The trust?..."
    crocodile "The lives?!"
    crocodile "Ahahahahah"
    crocodile "The rain!"
    crocodile "Ahahahahah"
    crocodile "What do you want me to return? There are too many things I took!"
    player "The kingdom..."
    crocodile "The kingdom, you say? Hahahaha, you're so funny... I am practically the king of this kingdom already..."
    crocodile "It's only a matter of time..."
    player "When we arrived here, the kingdom of [Arabasta.n] was already gone..."
    player "Erumalu, Yuba, Katorea, you've ruined so much..."
    player "If this is [vivi.n]'s kingdom, she should be happy here!"
    player "Here and now, I will defeat you!! This ends here!!"
    vivi "([player.n]... Thank you!!)"

    crocodile "You may have managed to get in my way..."
    crocodile "But not even the rain will help you defeat me"
    crocodile "Ahahahahah"
    crocodile "When you know the level of these seas... Dreams are left behind..."
    player "I don't care who you are!! I will surpass you!"

    pause 0.5

    call fight_start pass (enemy_pass = enemy_mr0, no_run = True, no_interface = True) from _fight_enemy_mr0

    $ music_arabasta()
    
    crocodile "Incredible... Really..."
    crocodile "A rookie has really surpassed me..."

    window hide dissolve
    window auto

    hide expression enemy_mr0.image with Dissolve(0.8)
    pause 0.8

    jump ar_alubarna_h_end


label ar_alubarna_h_army():
    window hide
    show screen screen_black with Dissolve(0.6)

    hide expression enemy_mr1.image
    hide expression enemy_mr2.image

    show koza c1_hurt at center with dissolve

    hide screen screen_black with Dissolve(0.3)
    window auto

    koza "And you're not alone either [player.n]!"

    player "[koza.n]!?!"
    koza "[vivi.n]!!"
    koza "Are these the guys who stole the rain from the kingdom?"
    vivi "All of this was..."

    show koza:
        linear 0.5 xalign 0.10
        yalign 1.0

    show crocodile with dissolve:
        xalign 0.85
        yalign 1.0

    crocodile "It was me, [koza.n]"
    crocodile "Everyone thought it was the king's fault, but it was a trap created by my organization"
    crocodile "You've all been dancing to our tune this whole time"
    crocodile "Ahahahahah"
    crocodile "You would have been happier dying without knowing... But well, it's too late for that now..."
    koza "Damn you...."
    koza "But not all is lost... Your plan will fail!"
    crocodile "Ahahahahah"
    crocodile "I'd like to know how..."
    koza "I will save as many as I can... The people will not suffer anymore!"
    koza "We'll take care of these two, you go after Crocodile, [player.n]!"

    hide koza with dissolve

    show crocodile:
        xalign 0.85
        linear 0.5 xalign 0.5
        yalign 1.0
    
    pause 0.3

    return


label ar_alubarna_h_noarmy():

    mr1 "Mr. 2, go first!"
    mr1 "See what the enemy has to show..."
    mr2 "My name is [mr2.n], you should have stayed home today..."
    mr2 "Now I'll have to take you out..."
    mr2 "I'm sorry for you, but I have no choice..."

    hide expression enemy_mr1.image with dissolve

    show expression enemy_mr2.image:
        xalign 0.8
        yalign 0.5
        linear 0.5 xalign 0.5

    pause 0.5
    
    call fight_start pass (enemy_pass = enemy_mr2, no_run = True, no_interface = True) from _fight_alubarna_h_mr2
    

    hide expression enemy_mr2.image with dissolve

    show expression enemy_mr1.image with dissolve:
        xalign 0.5
        yalign 0.5

    
    mr1 "Pufff, how incredible... Number 2 being defeated so easily..."
    mr1 "I saw you were holding back [mr2.n], what are you up to... Lately, you haven't been trustworthy"
    mr1 "I suppose I'll have to take care of this personally"
    mr1 "I must not make MR0 angry"


    call fight_start pass (enemy_pass = enemy_mr1, no_run = True, no_interface = True) from _fight_alubarna_h_mr1  


    mr1 "T...This is incredible, I've really been defeated..."

    hide expression enemy_mr1.image with dissolve

    return


label ar_alubarna_h_end():

    show vivi at center with dissolve

    vivi "You did it... You really did it..."
    vivi "You're amazing [player.n]!!"
    vivi "You've saved [Arabasta.n]!"

    if ar_rebel_army:
        $ vivi_love += 3
        narrador "[vivi.n] Love +3"  
    
    else:
        vivi "Now that the enemy has been defeated..."  
        vivi "I have to stop the rebels, they need to know the truth!"  

        narrador "[vivi.n] runs off" 

        $ vivi_love += 5
        narrador "[vivi.n] Love +5"   

        window hide
        show screen screen_black with Dissolve(0.6)

        $ game.location = "ar_alubarna_war"
        scene BG locations:
            blur 3

        hide screen screen_black with Dissolve(0.3)
        window auto

        narrador "When [vivi.n] arrived at the central plaza..."  
        narrador "To her surprise, only the sound of rain and a few murmurs could be heard..."  
        narrador "The rain had momentarily calmed the battle!"  
        narrador "This was not the rain generated by Dance Powder, it was real rain..."  
        narrador "With the fall of the tyrant, as if by magic, incredibly, the drought had also ended"  

        unknown "It's raining!"  
        unknown "It's raining for the first time in three years!"  

        vivi "{size=+16}Stop!! Never fight again!!!{/size}"  

        narrador "After her shout, only the sound of the rain could be heard"  
        narrador "The soldiers slowly lowered their weapons"  
        narrador "And everyone turned to listen to their princess..."  

        unknown "Vivi! It's the princess..."  
        unknown "I thought the princess was missing..."  

        vivi "I will explain everything that happened!"  
        vivi "This rain you're witnessing will be a regular sight from now on!!"  
        vivi "This horrible nightmare is finally over"  

        narrador "And so, under the rain... The kingdom's long years of suffering came to an end!" 

    window hide
    show screen screen_basic_black with Dissolve(0.6)

    $ hide_rain()
    $ game.location = "ar_alubarna_palace"
    scene BG locations:
        blur 3

    narrador "After the long battle, now recovered, you meet with King [cobra.n] and [vivi.n] inside the royal palace"

    hide screen screen_basic_black with Dissolve(0.3)
    window auto

    show vivi neutral:
        xalign 0.85
        yalign 1.0

    show cobra with dissolve:
        xalign 0.15
        yalign 1.0

    cobra "Thank you for saving my life, [player.n]!"
    cobra "You possess truly astonishing strength"
    cobra "I saw how you fought against [crocodile.n]... You're incredible!"
    cobra "All my strongest warriors were easily defeated... But you fought fiercely and won!"
    cobra "Thanks to you, the kingdom is safe, and not only that, you've saved my daughter multiple times!"
    cobra "I will be forever in your debt!"

    vivi "Thanks to your help, the kingdom of [Arabasta.n] will be able to prosper again"
    vivi "You've done so much for us! Since I met you, you haven't stopped helping..."
    vivi "I'm indebted for everything you've done for me..."
    vivi "That's why I wanted to ask you a favor"

    vivi "Would it be possible for me, Princess [vivi.n], to join your crew?"

    cobra "[vivi.n]!"

    vivi "Father, I've thought about it, and I want to be part of [player.n]'s crew"
    vivi "With their determination, I'm sure they'll achieve great things"
    vivi "Even [Arabasta.n] could benefit from this!"
    vivi "I want to be by their side to help in whatever they need"

    cobra "[vivi.n]... I understand you..."
    cobra "You've been through so much lately... I suppose it's natural to want to leave the nest..."
    cobra "I truly understand, I leave my daughter in your hands"
    cobra "You decide, [player.n]"

    menu:
        "Do you want [vivi.n] to be part of the crew?"
        "Yes":
            $ vivi_crew = True
            player "Yes, come with us, [vivi.n], you were already part of the crew before you even said it!!"
            player "Everyone will be happy to have you in the crew, especially me!"
            vivi "Thank you for everything, [player.n]"
            
        "I need to think about it":
            player "I need to think about it"
            vivi "I understand, if you change your mind, I'll be here in the palace waiting"  
            vivi "Whether I'm officially part of the group or not, you'll always have a place in my heart!"  


    $ ui_interface = True
    $ Arabasta.h = 14
    jump ar_alubarna
