# Version event: 2
# Version game: 0.9

label drum_island_village():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "drum_island_village"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    play ambient "market" fadein 1.0
    $ music_drumisland()
    jump m_drum_island_village

label m_drum_island_village():
    if DrumIsland.h == 3:

        player "Alright, here we are... this seems to be Bighorn Village!"

        show robin at center with dissolve
    
        robin "We need to ask someone about this doctor, or maybe they know directly about the [SakuraFlower.n]..."

        player "Alright, let's start with that guy over there... Not much of a crowd anyway..."

        player "Heeyy you, over there!"

        unknown "Mmm? Are you talking to me?"

        robin "Hehe... Let me handle this, Captain..."

        robin "Hello, nice to meet you, sir! We just arrived and we're looking for directions... Maybe you have some information about the [SakuraFlower.n]..."

        unknown "Hello miss! Lately, there have been several travelers asking the same thing..."

        unknown "It's not common to find that flower, I wouldn't know where to find it... As you can see, this island has a pretty harsh climate for any kind of plants!"

        robin "That's quite apparent!... Maybe you could point us to a doctor or a flora specialist in the village?"

        unknown "There are no doctors here!... Only the Isshi-20, but that group wouldn't help you even if you asked... They only serve the king..."

        robin "How can there be no doctors on the island!?!... That's serious!"

        unknown "It really is... But that's the current situation... Maybe... There is someone who could help."

        player "Who are you referring to!?!"

        unknown "A crazy old woman, a doctor, retired, I think... But I don't know if she'd help you..."

        robin "Are you talking about Doctorine?"

        unknown "Yeah, that's the one, hahaha, it's strange that outsiders know her... I didn't know she was that famous..."

        robin "Do you know where we could find her?"

        unknown "Unfortunately for you, she doesn't live in the village..."

        unknown "Look over there, at the top... You'll have to head that way, through the forest, until you reach her castle..."

        unknown "She's probably there, ever since the king left, she's taken over the place according to rumors..."

        unknown "But be careful, there are wild animals in the forest, and the weather won't make the climb easy..."

        robin "Don't worry, thank you very much for your help!"
        pause 0.5

        player "Alright, let's move! We're getting closer to finding the flower..."

        window hide
        hide robin
        hide yamato 
        hide nami       
        with dissolve
        window auto

        $ DrumIsland.h = 4
        
    menu:
        "Advance":
            jump drum_island_forest
        
        "Back":
            jump ship_mid
