# Version event: 3
# Version game: 0.31

label ar_yuba():
    if Arabasta.h <= 6:
        jump ar_yuba_desert

    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True        
    $ game.location = "ar_yuba_entrance"
    $ arabasta_location = "Yuba"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_yuba_entrance

label m_ar_yuba_entrance():
    if Arabasta.h == 7:
        window hide
        pause 1.5
        window auto

        show vivi anger at center with dissolve
        vivi "No, this can't be..."  

        player "Another village buried in sand..."  
        player "Is this the base of the Rebel Army?... There doesn't seem to be much movement..."

        vivi "Although I haven't been here for many years, it should be impossible for the city to be in these conditions."
        vivi "I don't understand how this is possible... I haven't been away from the kingdom for that long..."
        vivi "The situation is much worse than I thought..."         
        vivi "The sandstorms have devastated the city of Yuba."

        show nami serious at left with dissolve

        nami "This is terrible..." 
        nami "It looks very similar to how Erumalu was..."  

        show robin annoyed at right with dissolve

        robin "[vivi.n], didn't you say this was an oasis city?"  

        vivi "That's right... Let's go in, I need to see the oasis!" 

        $ Arabasta.h = 8

    menu:
        "Go to the Oasis":
            jump ar_yuba_oasis

        "Map" if map_arabasta and not game.clock.night:
            jump map_arabasta

        "Back":
            jump arabasta


label ar_yuba_desert():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "ar_desert"
    $ arabasta_location = "Yuba"
    scene BG locations:
        blur 3

    if Arabasta.h != 5:
        show expression enemy_sandoradragon.image:
            xalign 0.5
            yalign 0.5
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    pause 1

    if Arabasta.h == 5:
        player "I'm burning up!!!"
        player "This is really tough to cross!!"   

        if DrumIsland.h > 3:
            player "Right now, it would be great to feel the cold of an island like [DrumIsland.n]."  

        robin "The heat is really intense at this hour!"  
        robin "I think you're the only one not affected by this, [vivi.n]."

        vivi "I was born and raised here, so it doesn't affect me much… I guess it's just what I'm used to!"  
        
        nami "There are too many dunes! It would be much better to be sunbathing with a cool drink on a beach chair."

        vivi "Some of these dunes are 300 meters high! This is a desert with many years of history..." 

        player "Wow, 300 meters? That's like climbing a mountain!!"  

        vivi "Hahah, maybe a small one!!"
        vivi "It would be good to rest, but it is dangerous."    
        vivi "We have to stay alert, there are many dangers in the desert..."  

        window hide
        show BG locations at v_earthquake:
            blur 3

        pause 1.5
        window auto

        nami "What's happening? What's that tremor?"  

        window hide
        show BG locations:
            blur 3

        show expression enemy_sandoradragon.image with Dissolve(0.6):
            xalign 0.5
            yalign 0.5

        pause 1.5
        window auto

        nami "It's huge!!! Come protect me Captain!!"  

        vivi "It's a Sandora Dragon!!!"  
        nami "What is that?!?"  
        vivi "It's the largest reptile living in the desert… We're really unlucky today!"  
        vivi "It waits in the sand, lying in wait for its prey..."  
        vivi "It has incredibly sharp fangs and claws!!!"  
        player "Stay behind me, girls. I'll handle this!"  
        vivi "Be careful!" 

        $ Arabasta.h = 6


    call fight_start pass (enemy_pass = enemy_sandoradragon) from _fight_ar_yuba_desert
    
    if not fight_return:
        jump arabasta

    $ music_arabasta()

    hide expression enemy_sandoradragon.image with Dissolve(0.8)

    player "Phewww, it's tough to fight in this heat!"  
    vivi "You're so strong, [player.n]! With you, we can travel safely through these lands!"
    
    $ vivi_love += 1
    narrador "[vivi.n] Love +1"

    player "Hahaha, no need to worry, princess. On another note… can we eat it?"  

    vivi "Haha, of course! The Sandora Dragon is a highly prized source of meat in [Arabasta.n]!"

    menu:
        narrador "Do you want to keep the Sandora Dragon meat?"  
        "Yes":
            $ food += 6
            narrador "+6 Food"
            player "Great! Now we have more meat for the journey."


        "No":
            player "I changed my mind. Let's just keep moving!"  


    vivi "Despite everything, it looks like we got lucky. Sandora Dragons usually hunt in pairs." 
    
    yamato "Maybe it ran away after seeing [player.n]'s strength."  

    player "Hahaha, of course!"  

    vivi "Guys, the border of Yuba is just behind those big rocks."  
    vivi "Let's make one final push, and we'll be there!!"  
    player "Excellent, let's move out!"  

    $ Arabasta.h = 7

    jump ar_yuba