# Version event: 3
# Version game: 0.9

label di_castle_room():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "di_castle_room"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto


    $ music_drumisland()
    jump m_di_castle_room

label m_di_castle_room():
    if DrumIsland.h == 7:

        show kureha at center with dissolve
    
        
        unknown "Hold on there! Who are you..."
        unknown "I didn't see any bad intentions, which is why I let you get this far... But it's time you tell me what you want!"

        show kureha:
            linear 0.4 xalign 0.15
        
        pause 0.4

        show robin with dissolve:
            yalign 1.0
            xalign 0.85

        robin "Hello! We've come here because of some rumors... it's said that a doctor lives here, are you Doctorine?"

        hide robin with dissolve

        show kureha:
            linear 0.4 xalign 0.5

        unknown "That's me, but don't call me that, it's too familiar... My real name is..."

        call set_name_kureha from _call_set_name_kureha

        kureha "I'm Doctor [kureha.n]. What brings you here? No one climbs a mountain without something important to do..."

        player "(Wow, she's gorgeous... Crazy? No way, she's really sexy!!)"

        show kureha:
            linear 0.4 xalign 0.15

        pause 0.4    
        
        show robin with dissolve:
            yalign 1.0
            xalign 0.85

        robin "We're looking for the [SakuraFlower.n]."

        robin "We've gathered information, and the only lead we have is you... That's why we're here."

        kureha "Haha, searching for the [SakuraFlower.n] in a cold biome... It's impossible to think a sakura tree could grow in such a harsh environment... with all this cold!"

        robin "Thanks to a book, we found out that you have knowledge about this tree and its connection to this island."

        robin "We're aware of the climate issue... But we truly believe you can help us."

        kureha "You seem like a smart girl. Why are you so keen on finding the [SakuraFlower.n]?"

        robin "We met a young woman who needs it..."

        player "(And what a beautiful young woman!!)"

        robin "She's desperate because of a sick family member... She believes the [SakuraFlower.n] can help, and so do we."

        kureha "I see... I usually don't help strangers... but for some reason, you give me a sense of trust and calm..."

        kureha "If it can help others, I won't stand idly by... I'll tell you the truth..."

        kureha "I'm not the expert on this subject..."

        kureha "The truth is, a long time ago, there was a foolish doctor who spent years researching sakura trees..."

        kureha "He had a rather unusual approach to treating diseases... But that didn't make him any less of a genius!"

        kureha "He tirelessly researched until he figured out how to make a sakura tree grow on this island!"

        kureha "He said it would heal the hearts of the people on this island... hehe, he really was a fool..."

        kureha "So it seems you've come to the right place, as that fool managed to do the impossible."

        robin "So he actually made sakura trees bloom on this winter island?!?"

        kureha "He made it possible!... I can tell you where to find it..."

        kureha "I would have my assistant guide you, but they're not here right now... and I'm quite busy myself..."

        kureha "But first, you must promise me you'll take only what's necessary without harming the tree..."

        player "We have a deal, we'll only take what we need..."

        kureha "It would be a shame not to have access to its fruits anymore..."

        kureha "You'd be harming yourselves if you broke your promise and wanted to return later..."

        kureha "After passing the village, head into the forest before climbing up to the castle."

        kureha "From there, walk east without stopping, even though it may seem like there's no path, you'll reach the sakura tree."

        robin "Thank you so much. If you ever need anything, don't hesitate to ask!"

        kureha "We'll meet again... Now, go on with your business!"

        player "(We'll definitely meet again, my sexy doctor...)"  

        $ DrumIsland.h = 8

        window hide
        hide robin
        with dissolve
        window auto
        
        show kureha:
            linear 0.4 xalign 0.50

        pause 0.4    

    show kureha at center with dissolve
        
    menu:        
        "Back":
            jump di_castle_mid
