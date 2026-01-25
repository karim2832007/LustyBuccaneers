# Version event: 3
# Version game: 0.26

label elegia_road():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "elegia_road"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_elegia_road

label m_elegia_road():
    if Elegia.h == 3:
        pause 1.0

        nami "It's a steep climb... But the view is amazing!"
        player "(This is incredible, and I haven't run into a single beauty yet!!)"
        player "(And this area seems even more deserted than the previous ones!)"
        nami "Why that face, Captain? Relax... From here we can already see the castle at the top!"
        player "Yeah, I'm just really eager to get there!"
        yamato "Don't complain, Captain! Walking these paths is good for the body, and the weather is perfect!"
        robin "That's right! We are tourists after all... Aren't we, Captain?"
        player "(Smart girl...)"

        $ Elegia.h = 4

    elif Elegia.h == 8:
        pause 1.0

        yamato "Look over there!"  
        yamato "Captain, that man looks suspicious, seems like he's watching the forest..."  
        robin "The shirt... It's the Jellyfish Pirates' symbol!"

        window hide  
        window auto  

        show kaginote with dissolve:  
            xalign 0.5  
            yalign 1.0  

        pause 1.0  

        nami "Could he be one of the ones who kidnapped [uta.n]?"  
        player "(He doesn't look like much... If I face him and win, maybe he'll lead me straight to her. And if I save her... that gorgeous woman will be forever grateful!)"  
        player "We're in luck!!"  
        player "Hey you! What are you doing here?"

        unknown "Heh... you talking to me?"

        player "Are you one of the Jellyfish Pirates?"

        unknown "And who's asking..."  
        unknown "Who the hell are you?"  
        player "Your worst nightmare... You better talk fast, I don't have time to waste on you..."  
        unknown "Hahaha looks like I ran into a big talker..."  
        pause 1.0  
        unknown "!!!"  
        unknown "A big talker surrounded by beautiful women..."  
        unknown "Why don't you girls come closer... And stop wasting your time with this loser..."  
        unknown "Let's have a little fun together... Hehehe"  
        player "You're digging your own grave, nobody..."  
        unknown "Hahaha nobody... Don't you see the symbol on my chest?!?... Clearly, you know nothing about these seas..."  
        kaginote "My name is [kaginote.n], a proud member of the Jellyfish Pirates..."  
        kaginote "Who the hell are you?"

        player "I'm [player.n], and I'll make you tell me where [uta.n] is..."

        kaginote "[uta.n]?!?... You must be talking about the leader's new toy..."  
        kaginote "So that's why you're after the Jellyfish Pirates..."  
        kaginote "Interesting... I guess I'll defeat you and take you to my boss..."  
        kaginote "And maybe give one of those girls who follow you to him..."  
        kaginote "Not before I have a little fun with them first, hehehe..."  
        kaginote "I'm sure he'll reward me greatly!"  
        kaginote "Come here, weakling!"


        window hide
        show screen screen_black with Dissolve(0.6)

        $ ui_interface = False
        $ game.location = "elegia_road_fight"
        scene BG locations:
            blur 3

        show enemy_kaginote:
            xalign 0.5
            yalign 0.5
        
        hide screen screen_black with Dissolve(0.3)
        window auto

        pause 1.0

        player "You're gonna regret those words!"

        call fight_start pass (enemy_pass = enemy_kaginote, no_run = True, enemy_location = "elegia_road_fight") from _fight_enemy_kaginote
        
        $ music_elegia()
        
        player "That was easy..."
        kaginote "Ufff... Shit man wtf..."  
        player "Talk! Where is [uta.n]?"

        kaginote "Damn you!"  
        kaginote "Who the hell are you... You're no nobody..."  
        kaginote "But you're a fool if you think I'll talk..."  
        kaginote "I'm not telling you anything, idiot!"

        window hide  
        show layer_smoke zorder 5 with Dissolve(0.6)  
        narrator "BOOM!"  
        hide enemy_kaginote  
        hide layer_smoke with Dissolve(1.4)  
        window auto  

        player "Damn it, the same trick again..."  
        player "I'm getting tired of this..."  
        robin "We lost him!"  
        yamato "He probably went down to the town, there's no other visible path."  
        yamato "Let's hurry, Captain!"

        $ Elegia.h = 9

    menu:
        "Keep going up":
            jump elegia_castle

        "Enter the Forest" if Elegia.h >= 10:
            #narrador "Event not available in this version, please wait for v0.27"
            jump elegia_forest

        "Back":
            jump elegia_city
