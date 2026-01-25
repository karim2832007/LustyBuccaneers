# Version event: 3
# Version game: 0.31

default oasis_yuba = False

label ar_yuba_oasis():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True        
    $ game.location = "ar_yuba_oasis"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_yuba_oasis

label m_ar_yuba_oasis():
    if Arabasta.h == 8:
        window hide
        pause 1.5
        window auto

        vivi "This is terrible..."  
        vivi "The sand hasn't stopped accumulating, and the oasis is buried..."  

        unknown "Travelers in Yuba?"  
        unknown "..."

        narrador "Paying closer attention, you can see a man digging a well in the oasis."  

        window hide
        show toto at center with dissolve
        pause 1.0
        window auto
        show toto pervert with Dissolve(0.2)  
        
        unknown "Wow, what is this?! I must be hallucinating from the heat..."  
        unknown "How is it possible for so many beauties to arrive here...?"  
        player "(Hahaha, this old man is just like me...)"  
        unknown "You must be exhausted from crossing the desert... It's a really hot day today..."  
        unknown "I'm sorry, but this city hasn't been what it once was for a long time..."  
        unknown "There aren't many luxuries, but you can stay and rest... I'd be delighted, hehe..."  

        show toto pervert:
            yalign 1.0
            linear 0.5 xalign 0.05

        pause 0.3

        show nami joke with dissolve:
            yalign 1.0
            xalign 0.90

        nami "Hahaha, what a kind gentleman..."  

        unknown "But of course, beautiful lady..."  
        unknown "There are many inns here."  
        unknown "Yuba will always offer a place to rest for such beautiful women as yourself."  


        show nami shame with dissolve
        
        pause 0.3

        hide nami with dissolve

        show vivi neutral with dissolve:
            yalign 1.0
            xalign 0.90

        show toto neutral with Dissolve(0.2) 

        vivi "Excuse me, good sir, we came because we heard that the rebel army was in this city!"  

        unknown "Mnmnm... You are too young and beautiful to be getting involved with those people..."  
        unknown "What do you want with the rebel army?"  
        unknown "If you're looking for those fools, they left here quite some time ago..."  


        player "{size=+16}What are you saying?!{/size}"

        show vivi serious with Dissolve(0.2)
        vivi "That can't be!"  

        unknown "The sandstorms are very frequent here."  
        unknown "It has been over three years of drought..."  

        show toto:
            yalign 1.0
            linear 0.5 xalign 0.5

        pause 0.3

        show nami serious with Dissolve(0.2):
            yalign 1.0
            xalign 0.05

        nami "That's terrible... How is that possible?!?"  

        unknown "That's what I wonder too, young lady..."  
        unknown "Little by little, these sandstorms buried the city..."  
        unknown "And now the oasis looks like this..."  
        unknown "People started leaving the city..."  
        unknown "{size=-5}Especially the women...{/size}"  
        unknown "After that, the city's supply flow disappeared..."  
        unknown "And because of that, the rebel army, unable to sustain itself, decided to move..."  
        unknown "I see you're good people, so I'll tell you..."  
        unknown "They decided to relocate their base to Katorea!"  

        show vivi annoyed with Dissolve(0.2)
        vivi "Katorea?!?"  

        player "Where is that?! Is it far from here, [vivi.n]?"  
        unknown "?!?"  
        vivi "It's an oasis near Nanohana... The port city where we started..."  
        player "Ugh, we have to go all the way back again..."  

        unknown "[vivi.n]?!?"  

        show vivi serious with Dissolve(0.2)

        unknown "Did you say [vivi.n]?!?"
        show toto happy with Dissolve(0.2)    
        unknown "Is that you, [vivi.n]?! I didn't recognize you!"  
        unknown "You're really alive, Princess! What a joy!!"  
        unknown "It's me, [vivi.n]!"  
        unknown "Don't you recognize this old man?!"  
        unknown "I'm not surprised... I lost some weight from all this digging and living like this..."  

        window hide
        window auto
        hide nami
        hide vivi
        with dissolve

        call set_name_toto from _call_set_name_toto

        #behind toto:

        pause 0.2
        show toto behind toto:
            yalign 1.0
            linear 0.5 xalign 0.10
            
        pause 0.3

        show vivi neutral behind toto:
            yalign 1.0
            xalign 0.90

        with dissolve
        vivi "Uncle [toto.n]?!?"  

        toto "That's right!!!"  

        vivi "It can't be..."

        show vivi serious with Dissolve(0.2)

        vivi "(This environment has really taken a toll on him... He looks quite worn out, poor thing...)"  
        toto "You've grown so big and so beautiful!"  
        toto "[vivi.n], I swear I still have faith in His Majesty!"  
        toto "That man would never betray his kingdom."  
        toto "Right?!?"  
        toto "I believe in the king..."  
        toto "I swear I tried to stop the rebels, but their strength is at its limit."  
        toto "They want to end everything in the next attack... They're tired of waiting..."  
        toto "They're desperate and willing to die!"  
        toto "Please, [vivi.n], you have to save those fools!"  


        show vivi serious with Dissolve(0.2)

        vivi "Calm down, Uncle [toto.n], don't worry!"  
        vivi "I promise we'll stop this war... With this group, we're already working on it!"  

        toto "Thank you! I trust that you will!"  
        toto "Feel free to rest at any inn with your friends."  
        toto "If you need me, I'll be here digging... I have to fulfill my dream... And also bring life back to this city..."  
        toto "I have to find water!"

        hide toto with dissolve

        show nami with dissolve:
            yalign 1.0
            xalign 0.10

        nami "What do we do now?!?"  

        vivi "I don't know... This complicates everything, and we don't have much time..."  
        vivi "My plan was to reveal the truth about [crocodile.n] to the rebel army..."  
        vivi "Trust that they would reconsider the situation, and then ask for their help on our way to Rainbase."  

        player "That's where [crocodile.n] is?!"  

        vivi "From the information I gathered while infiltrating, yes."  
        vivi "Rainbase isn't very far from here either..."  
        vivi "Help me, [player.n], I want everyone to be safe!"  

        player "(This isn't all bad...)"  
        player "(It's my chance to beat up [crocodile.n] without the help of the rebel army.)"  
        player "(That way, all the glory will be mine, and [vivi.n] will be in my debt forever!)"  
        player "(But... I don't know [crocodile.n]'s strength. Maybe some help is necessary to defeat him.)"  
        player "(The girls were really afraid of him... He can't be a nobody...)"  

        player "I understand, it's a tough choice."  
        player "But now we're nakamas!"  
        player "You're the one suffering the most and the one who wants to take down [crocodile.n] the most."  
        player "I've already made my decision, follow me."  
        player "We're going to..."  

        window hide
        window auto
        hide nami
        hide vivi
        with dissolve
        $ Arabasta.h = 9
        jump map_arabasta

    menu:
        "Go to [toto_name]'s house" if not game.clock.night and oasis_yuba:
            #narrador "This event is in development, try again in the next version."
            jump ar_y_toto_house

        "Go to bar" if not game.clock.night and Toto.h > 0:
            jump ar_y_bar

        "Dig the Oasis" if not game.clock.night and not oasis_yuba:
            if not tool_shovel:
                narrador "Shovel required"
                jump m_ar_yuba_oasis

            jump ar_yuba_dig

        "Back":
            jump ar_yuba