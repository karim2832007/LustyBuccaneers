# Version event: 3
# Version game: 0.26

label el_castle_room():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "el_castle_room"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_el_castle_room

label m_el_castle_room():
    if Elegia.h == 7:

        show gordon with dissolve:
            yalign 1.0
            xalign 0.5
        
        pause 1.0  
        unknown "What the hell!!"  
        unknown "How dare you barge into my office like this!"  
        unknown "Do you want to be punished?!"  
        pause 0.5  
        unknown "Mnmnmnm?!?"  
        unknown "But... But you're not even students here... Who are you?!?"  
        pause 1.0  
        gordon "I am Gordon, the general director here! And the King of this whole island..."  
        gordon "How can just anyone walk in like this... I need to review all the castle's security..."  

        show yamato with dissolve:  
            yalign 1.0  
            xalign 0.05  

        yamato "Yeah, you really should! If you knew what just happened under your nose..."  
        gordon "What are you implying?!?"  
        gordon "You strangers, who are you?"  
        gordon "Why are you here? And why did you enter my office without speaking to my secretary first..."  
        player "I'm here to solve your security problems, so watch your tone!!!"  
        gordon "What the hell?!?"  
        yamato "You heard him right! We're here to bring order to your castle!"  
        gordon "How disrespectful! Are you implying there's no order in my castle?!"

        show robin with dissolve:  
            yalign 1.0  
            xalign 0.90  

        robin "Forgive us, sir! I apologize for the rude behavior of my subordinates..."  
        robin "They're impulsive and don't understand formalities... They don't know how to address royalty!"  
        robin "Nor do they know when they can or can't speak..."  
        yamato "(Mnmnm?!? what's she planning...)"  
        player "What are you saying! what are you..."  

        robin "{size=50}Silence, recruit!!{/size}"  
        player "Recruit?!?!"  
        robin "If you speak again, you'll be scrubbing latrines all weekend!"  
        player "...."  
        player "(Ahhh, she's acting! She's got a plan...)"  
        robin "Back to the main point... Forgive us for this terrible scene, and I apologize for the intrusion, Mr. Gordon..."  
        robin "But the matter that brought me here requires swift, joint action from everyone present, including yourself!"  
        gordon "I see... So finally I'm talking to someone decent... Someone who knows how to discuss matters."  
        gordon "Tell me... Who are you, young lady?"  
        gordon "How can I be of service?"  
        robin "Allow me to introduce myself, your majesty. I am... I am Olvia, lieutenant of Marine Headquarters."  
        gordon "The Marines?! You're here for the festivities?!?... And where's your uniform..."  
        robin "We're on an undercover mission... We came following a tip-off, but unfortunately, we arrived too late..."  
        gordon "A tip-off! What happened... Why wasn't I informed about this?!?"  
        robin "It's a long story, my subordinates will brief you on the details later."  
        robin "Time is of the essence... While undercover during one of the rehearsals, we witnessed a kidnapping!"  
        gordon "A kidnapping!!!"  
        robin "That's right... Unfortunately, the criminals moved too fast... We couldn't stop them, they got away."  
        gordon "This is terrible..."  
        robin "Indeed... They were pirates..."  
        robin "The victim was a young girl, we need you to provide us with some information..."  
        player "Yes!!! A beautiful young girl... We need to know who she is!!!"  
        gordon "?!?!?"

        robin "{size=50}Silence, recruit! I won't allow another meaningless interruption!!{/size}"  
        robin "Now, back to the matter at hand..."  
        robin "The pirate who captured her had a Jellyfish symbol on his clothes..."  
        player "(How did she notice that... [robin.n] is really amazing...)"  
        gordon "A Jellyfish..."  
        gordon "Oh, must be one of the Jellyfish Pirates..."  
        robin "You're well-informed... It just happened, they must still be escaping. We can still catch them..."  
        robin "But first... Regarding the victim, we need you to help identify her."  
        gordon "There are thousands of students... It's unlikely I can help with that."  
        robin "You're mistaken... This young lady was clearly a prodigy, surely one of the best..."  
        robin "With half-red, half-white hair... Quite a particular hairstyle and outfit."  
        gordon "Red and white hair!!"  
        gordon "..... [uta.n]!!"  
        gordon "It can't be true!!"  
        gordon "If anything happens to her... HE would never forgive me!"  
        yamato "Mnmnm?!?... Who do you mean by HE?!?"  
        gordon "That's not important right now... We must act immediately!!"

        hide yamato with dissolve  

        show gordon:  
            yalign 1.0  
            linear 0.5 xalign 0.2  

        show robin:  
            yalign 1.0  
            linear 0.5 xalign 0.8  

        gordon "Contact your ship immediately and block the port..."  
        gordon "If this just happened, like you say, they can't be far!!"  
        player "(That's a great idea!... But we're not Marines hahaha!)"  
        robin "Don't worry, we'll handle it right away... In fact, we're already working on it..."  
        player "(Hahaha what a great liar you turned out to be, [robin.n]!)"  
        gordon "I beg you, help me find [uta.n]!"  
        robin "Don't worry, we're on our way — every minute counts!"  
        robin "With your permission."
        robin "On my way Marines, let's go urgently to the city... We have some pirates to capture!"

        hide robin 
        hide gordon
        with dissolve

        $ Elegia.h = 8

    menu:

        "Back":
            jump el_castle_corridor
