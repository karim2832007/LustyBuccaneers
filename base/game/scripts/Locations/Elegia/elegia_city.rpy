# Version event: 3
# Version game: 0.26

label elegia_city():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "elegia_city"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_elegia()
    jump m_elegia_city

label m_elegia_city():
    if Elegia.h == 2:
        pause 1.0

        show nami with dissolve:
            xalign 0.15
            yalign 1.0

        nami "Wow! This city is incredible..."
        nami "It's so elegant... And everything is so clean and tidy around here!"
        player "(Okay, yes... very nice and all. But what I want to see is...)"
        player "(Where are those sexy singers!!?)"
        nami "Look at that fountain. It's like the whole city is singing in unison..."
        player "Yeah, yeah... very artistic and all. But tell me... isn't there a place with, you know, live music?"
                    
        show robin with dissolve:
            xalign 0.85
            yalign 1.0
        
        robin "Actually, yes. The king of Elegia is a music lover."
        robin "It's said that his castle has special rooms where the kingdom's top singers rehearse and hold private performances."
        robin "Some of those voices have gained fame even beyond the New World!"
        robin "Admission is really strict at this academy... They're very selective about who they allow to attend!"
        robin "But that probably changed after the newspaper news... They should be a lot more flexible if we go..."
        player "(That's my destiny!)"
        player "(A secret room full of beautiful singers... This place might be paradise!)"

        show nami serious with Dissolve(0.5)

        nami "That pervy face... You're only thinking about one thing, Captain..."
        nami "Just don't cause trouble, okay? We're here as tourists."
        player "Got it! I just want to enjoy the local art."
        nami "Yeah... The art..."
        player "Looks like we already have a destination! Let's head for the castle!"
        
        hide nami with dissolve
        hide robin with dissolve        
        $ Elegia.h = 3

    elif Elegia.h == 9:

        nami "Wait Captain, you're rushing too much!! You're leaving me behind!"
        player "Come on girls, run!! We have to hurry!"
        robin "Watch out! Look ahead Captain!"
        robin "You're about to bump into that man... From his uniform..."
        robin "He looks like a captain from Marine Headquarters!"


        if not koby_debut:
            player "(Eh?!?!... A Captain?)"

            show koby with dissolve:
                yalign 1.0
                xalign 0.5
            
            pause 2.0
            nami "{size=20}Pss.. Pss..{/size}"            
            nami "{size=20}Let's go Captain!! Why are you staring at him... There's no reason he'd suspect us...{/size}"
            player "Mnmnm !?!"
            player "Hahahah I can't believe it!"
            player "[koby.n]!?!.... Is that you?"

            #Koby happy face

            koby "[player.n]! Hahaha what a coincidence!... With the sea being so vast, we meet again here in Elegia..."
            player "It really is a pleasant surprise..."
            player "I can't even remember the last time we saw each other..."
            koby "Yeah, it's been years... We were kids last time..."
            koby "I was a Chore Boy, and you were obsessed with becoming a pirate..."
            player "(With women [koby.n], with women!)"
            koby "Good times..."
            player "Now we know who made the wrong decision!"
            koby "Hahaha I could say the same [player.n], I could say the same!"
            player "I can't believe it! You, a captain? Since when do nerds climb that high?"
            koby "Ha! I guess growing up helps..."
            koby "You, on the other hand, haven't changed much..."
            koby "Still trying to be surrounded by girls... And now by beautiful ladies..."
            player "(Damn, he even looks more formal... since when did I hang out with such responsible people?)"
            player "You know me well..."
            player "Glad to see you!"
            koby "Glad to see you too! And I hope you're not up to anything shady pirate... Or else... Heh!"

            $ koby_debut = True

        else:
            yamato "Look captain it's [koby.n]!"

            show koby with dissolve:
                yalign 1.0
                xalign 0.5
            
            player "Wow! [koby.n]... We keep running into each other... What are you doing here?"

            koby "I came to visit the island now that its gates are open..."
            koby "And what about you?"


        player "I'd love to tell you about my adventures, but I'm coming from the castle for an emergency"
        player "A singer was kidnapped, a beautiful woman named [uta.n]"

        show koby serious with Dissolve(0.3)
        
        koby "!!!"
        koby "A singer was kidnapped on the island... And on top of that, the famous [uta.n]?"

        player "Yeah, you know her?"

        koby "I've heard her name several times since I got here, she seems to be a very promising singer..."
        koby "Also I have some information... But never mind..."

        show koby neutral with Dissolve(0.3)

        koby "They picked a bad day to cause trouble..."
        koby "With me and my squad here..."
        player "You sound really confident in your abilities... What happened to the scrawny [koby.n] Hahaha..."
        koby "That [koby.n] is long gone..."
        koby "But let's get back to the important stuff..."
        
        show koby serious with Dissolve(0.3)

        koby "Do you have any clue who could have kidnapped her?"

        player "Yes, the kidnappers seem to belong to an organization called the Jellyfish Pirates"
        player "Have you seen anyone with a jellyfish symbol on their clothes?"

        koby "No, I haven't seen anyone like that. I'm sure I'd remember..."
        koby "They're known pirates in this area... I would've already arrested them..."

        player "That's strange... We could've sworn one came this way..."

        koby "I haven't seen him here... But if pirates are involved I have no choice..."
        koby "I'll have to order the island to be sealed. No one leaves without being checked. If that pirate group is still here, we'll catch them."
        koby "We can't allow them to escape this island"

        player "Understood... you can count on me."

        show koby neutral with Dissolve(0.3)

        koby "Ha! A pirate helping us?"
        koby "That's not something you see every day..."
        koby "It's not that I doubt your skills... But this is an official case now... 'Civilians' can't get involved..."
        koby "It's too dangerous, let the Marines handle it, I assure you, [uta.n] will be safe."

        player "Got it, thanks [koby.n]... I'm counting on you!"
        robin "!!!"
        yamato "!!!"
        nami "!!!"
        koby "... Alright!"
        koby "Then I'll take my leave, if you find any more clues don't hesitate to talk to me... I'll be organizing everything at the port!"
        koby "Goodbye!"
        koby "And I repeat... Don't get involved in this [player.n]!"

        hide koby with dissolve

        player "(Don't think for a second I'll let you take the credit for rescuing the damsel in distress...)"
        player "(I'll find her first and be the hero... And she'll owe me big time!)"

        show nami with dissolve:
            yalign 1.0
            xalign 0.5

        show yamato with dissolve:  
            yalign 1.0  
            xalign 0.05  

        show robin with dissolve:  
            yalign 1.0  
            xalign 0.90  

        nami "Well looks like the Marines will handle it..."
        yamato "I don't think so!"
        robin "Heh... I thought the same as [nami.n] at first, but seeing the Captain's face right now..."
        player "Well you're not the only one who learned to act today, [robin.n]"
        yamato "Captain was very direct and convincing... It wasn't very like you..."
        player "I trust [koby.n], but if [kaginote.n] didn't go down to the town... Maybe he escaped into the forest, down the previous path!"
        yamato "That's very possible... He tried to make us think he ran into the city, but he was staring straight at the forest before crossing!"
        robin "That's an interesting theory..."
        player "Either way... We've got [koby.n] handling the hard part..."
        player "The Marines will make sure they can't escape the island..."
        nami "That's right Captain! These low-tier pirates won't be able to do much... Their hands are tied!"
        player "Exactly... But the Marines might take too long to find her, so we'll go search first."
        robin "You're right about that Captain!"
        yamato "That [kaginote.n] got a good beating... Maybe he didn't even make it back to his group..."
        robin "If he escaped through the forest he can't be far, we need to hurry."
        player "(That bastard can't hide from me...)"
        player "Let's go back to the mountain path!"


        hide robin 
        hide yamato
        hide nami
        with dissolve

        $ Elegia.h = 10
        
    menu:
        "Climb the mountain trail":
            jump elegia_road

        "Shop":
            call shop_default from _call_shop_elegia_city
            jump m_elegia_city

        "Back":
            jump elegia_dock