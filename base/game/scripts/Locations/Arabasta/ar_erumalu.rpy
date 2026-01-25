# Version event: 4
# Version game: 0.31

label ar_erumalu():
    if Arabasta.h <= 3:
        jump ar_erumalu_coast

    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True        
    $ game.location = "ar_erumalu"
    $ arabasta_location = "Erumalu"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_erumalu


label m_ar_erumalu():
    if Arabasta.h == 4:

        window hide
        pause 1.5
        window auto

        show yamato serious at center with dissolve  
        yamato "Eh... Are we here already?!?"
        player  "Hahaha, what are you talking about? This place is a mess... Looks like it's been abandoned for a while..."

        show yamato:
            linear 0.4 xalign 0.15
        pause 0.5
        show nami serious at center with dissolve
            
        nami "Doesn't look like there's anyone around here..."

        show nami:
            linear 0.4 xalign 0.90  
        pause 0.5

        show vivi serious at center with dissolve  
        vivi "Unfortunately... It's just as you say..." 
        vivi "It's a shame, but this is Erumalu."

        player "What are you saying!?! This is really Erumalu?"
        player "Things don't seem to be going well here..."

        show nami anger

        nami "Shut up, Captain..."

        show nami serious with Dissolve(0.2)

        nami "Forgive him [vivi.n], our Captain is a bit insensitive..."
        vivi "Don't worry [nami.n], [player.n] is right... This is truly tragic..."   
        vivi "Erumalu used to be known as the Green City."
        show yamato serious with Dissolve(0.2)
        yamato "The Green City?!?"
        vivi "That's right... Years ago, this town was bustling with people and trade..."
        vivi "This place served as a meeting point or a rest stop between villages."
        vivi "But this is the reality now..."
        vivi "The constant sandstorms never stopped battering this city, and so its citizens fled, and the canals dried up."

        show vivi annoyed at center with Dissolve(0.2)  

        vivi "I don't know what they're doing or planning, but all of this is the fault of the Baroque Works!!"
        vivi "This is what Baroque Works is doing to my country..."
        vivi "And what the people of Alabasta are suffering every single day!!"
        vivi "Now Erumalu looks like a ghost town!!"

        show nami anger with Dissolve(0.2)

        nami "This is terrible!!"
        nami "We have to stop them as soon as possible!"     

        show vivi serious with Dissolve(0.2)

        vivi "That's right, [nami.n]!"
        show nami annoyed with Dissolve(0.2)  
        vivi "I'm sure that together we can do it!!"

        hide yamato with dissolve

        show robin neutral with dissolve:
            yalign 1.0
            xalign 0.1 

        robin "But there's something I don't understand..."
        robin "How could such a prosperous city end up like this...?"

        vivi "That is the heart of the matter... And this isn't something that has only happened here, it's happening all over the kingdom..."      
        vivi "Not long ago, as I was saying, Erumalu was a prosperous city full of vegetation..."
        vivi "It has never rained much in these lands, but with its water reserves, Erumalu had enough..."
        show vivi annoyed at center with Dissolve(0.2) 

        vivi "This is where [crocodile.n] and his group, somehow, come into play..."         
        vivi "It hasn't rained a single drop in three years!!"
        vivi "Though rain is becoming scarcer throughout the kingdom..."
        vivi "There's one place where the rain falls more than usual!"
        vivi "And that is in the kingdom's capital, Alubarna, the city where the royal palace is, my family's home."
        player "What a luck!!"
        vivi "Well, it's not... Some people called it the king's miracle..."
        vivi "But that's not true... As you said [player.n], there are those who don't believe it, who think there's something behind all this... And to top it off..."
        vivi "Recently, large shipments of Dance Powder were discovered arriving in the kingdom!"

        player "Dance Powder?!?"

        nami "I think I've heard about this..."
        robin "Dance Powder is also known as the powder that produces rain..."
        robin "When it turns into smoke, it creates rain wherever it passes..."
        robin "That's why the country that created it danced with joy after seeing rain fall following years of drought. That's where its name comes from..."
        robin "While this might sound good, its use has severe unintended consequences..."
        robin "Dance Powder artificially affects clouds..."
        robin "This way, while it does create rain, it steals it from the surrounding areas, causing severe droughts."
        robin "The neighboring country of its creators suffered massive droughts as a result, which led to a war between the two nations."
        robin "After a great massacre, the World Government imposed a ban on its use."
        robin "Its production and possession are illegal..."
        vivi "That's right, everything [robin.n] said is true."
        player "Always so well-informed, my [robin.n]!!"
        player "So... Does that mean the king brought in this shipment illegally?"
        
        show nami anger with Dissolve(0.2) 
        nami "Of course not, Captain!!! Let her finish the story!"
        show vivi serious at center with Dissolve(0.2) 
        vivi "My father is a wise and kind person, he would never use tools that harm others..."

        show nami serious with Dissolve(0.2)

        vivi "Going back to the case of my kingdom..."       
        vivi "When the people discovered these shipments..."
        vivi "They blamed my father, the king, for causing the droughts in all the other cities by using this powder for his own benefit..."
        vivi "But my father was not the one who ordered it!"
        vivi "We didn't know who was responsible... But while we were investigating..."      
        vivi "Not long after, a massive amount of Dance Powder was found inside the palace."

        robin "Were there infiltrators in the palace?"

        vivi "It seems so... They wanted to frame the royal family for the droughts!"
        vivi "Since this incident, the people's distrust in the king has been growing daily..."
        vivi "Obviously, this was all orchestrated, but the discontent keeps rising..."
        vivi "There are more and more uprisings... I want to prevent a civil war!"
        vivi "Many towns are being ruined by the droughts, and the rain never comes!!"
        vivi "{size=35}It's as if the skies have abandoned us, and the sandstorms keep coming one after another!{/size}"
        pause 0.5
        robin "Mnmnm... It's really strange..."        
        vivi "Many people have left in search of other oases or more humid lands..."
        vivi "And that's how the Green City withered away!"
        vivi "We have to move on to Yuba now!"

        nami "That's where the rebel army is, right?"

        vivi "That's what I believe. I will convince their leader to stop the revolt."
        vivi "[crocodile.n] is behind all of this, I have no doubt... His plan is already in motion, we have to uncover it and stop him!!"
        vivi "I will tell him the whole truth and everything I've discovered to prevent more bloodshed."

        player "Understood, let's get moving!"

        $ Arabasta.h = 5
        hide robin with dissolve
        hide nami with dissolve
        hide vivi with dissolve
        pause 0.5

    menu:
        "Map" if map_arabasta and not game.clock.night:
            jump map_arabasta

        "Back":
            jump arabasta


label ar_erumalu_coast():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "ar_erumalu_coast"
    $ arabasta_location = "Erumalu"
    scene BG locations:
        blur 3

    show expression enemy_dugong.image with Dissolve(1.0):
        xalign 0.5
        yalign 0.5
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    if Arabasta.h == 2:
        narrador "As you were heading to your destination, you came across a strange creature..."
        yamato "What the hell is that?"

        window hide
        pause 1.5
        window auto

        nami "Is it a turtle?!?"
        player "It looks more like a seal..."
        nami "Look at it, how cute! It looks like it's dancing!"
        robin "I think it has bad intentions..."
        yamato "Hahaha, what are you talking about?"
        vivi "It's a Kung Fu Dugong!"
        vivi "They're always looking for a fight, as if they were training..."
        vivi "It could be dangerous, don't get too close! It might be looking for trouble!!"
        player "So you want to fight!"
        player "Don't worry, ladies, I'll take care of this!"

        $ Arabasta.h = 3

    call fight_start pass (enemy_pass = enemy_dugong) from _fight_erumalu_coast
    
    if not fight_return:
        jump arabasta

    hide expression enemy_dugong.image with Dissolve(0.8)

    $ music_arabasta()

    vivi "Wow, you defeated it with your bare hands! You're really strong..."

    $ vivi_love += 1
    narrador "[vivi.n] Love +1"

    player "It was tough, but nothing special..."
    vivi "It seems to be unconscious, which is good..."
    vivi "When defeated, Kung Fu Dugongs become your disciples, so it's better if it stays unconscious."
    robin "How interesting..."
    vivi "The desert is dangerous, and we still have a long journey ahead."
    vivi "We should leave before it wakes up."
    nami "Let's continue our journey!"
    player "See you, buddy! Better luck next time!"

    $ Arabasta.h = 4

    jump ar_erumalu
