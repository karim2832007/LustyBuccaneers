# Version event: 2
# Version game: 0.28

label el_church_tunnels():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "el_church_tunnels"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_el_church_tunnels

label m_el_church_tunnels():
    if Elegia.h == 12:

        $ ui_interface = False
        pause 0.3

        show eboshi c1:
            xalign 1.2
            yalign 1.0

        show kaginote c1:
            xalign -0.05
            yalign 1.0

        with dissolve

        eboshi "These tunnels are like a damn labyrinth...."
        eboshi "This could play in our favor for a while."
        eboshi "[hanagasa.n] and I will go explore them... I don't know why we didn't do it earlier..."
        eboshi "[kaginote.n], you'll be in charge of watching over [uta.n]."
        eboshi "Wait for us in that room over there."
        kaginote "Understood. I'll take good care of her."
        eboshi "Don't be an idiot [kaginote.n]... I mean it, take good care of her!"
        eboshi "You know damn well who her father is, right?!?... Use your upper brain for once!"
        eboshi "Wait for us in that room, we won't be long... Don't fail me again like you did with the pirates!"
        kaginote "He..."
        kaginote "Understood, Captain! I'll take good care of her..."
        kaginote "(What a golden opportunity!!!)"
        kaginote "(I'll be alone in charge of this beauty...)"
        kaginote "([uta.n] is perfect... I'm sure she'll never forget me!!)"
        kaginote "(Any woman who tries this [kaginote.n]... never goes back!)"

        hide eboshi 
        hide kaginote
        with dissolve
        window hide
        window auto
        pause 1.0

        narrador "A brief moment later..."
        show nami c1 neutral with Dissolve(0.2)
        nami "What do we do, Captain?"
        nami "They've split up... But now [uta.n] is alone with that fool!"
        player "Yes... That worries me too..."
        player "(I don't trust leaving her alone with that [kaginote.n] guy...)"
        nami "They're in this room, right?!"
        player "Yes, I think the other two have already moved away... We could try to rescue her now..."
        hide nami with Dissolve(0.2)
        player "!!!!!"
        uta "{size=40}What are you implying?! Get out of here, you creep... Stay awayyyy!{/size}"  
        player "That bastard! I knew it!"

        window hide
        show screen screen_basic_black with Dissolve(0.6)
        $ game.location = "el_c_tunnels_room"
        #scene BG locations

        show kaginote c1:
            xalign 0.3
            yalign 1.0

        show uta anger c1:
            xalign 0.85
            yalign 1.0

        hide screen screen_basic_black with Dissolve(0.3)
        window auto

        narrador "You quickly enter the room after hearing [uta.n]'s screams"
        narrador "Upon entering, you find [kaginote.n] harassing [uta.n] while tearing the top she was wearing into pieces..."
        
        show screen screen_black with Dissolve(0.8)
        show events uta h1 uta_h1
        hide screen screen_black with Dissolve(0.8)

        uta "{size=40}Kiaaaaaaaaaaaaaa!{/size}"

        show uta c1_bra
        hide events uta with Dissolve(0.8)
        player "Get away from her, you bastard!"
        kaginote "What the hell...."
        kaginote "You again?! How did you find us?!?"
        player "This time you've got nowhere to run!!"
        player "We'll settle this right here and now!"
        uta "Please help me!!!"
        uta "This disgusting guy is a monster!!"
        player "Don't worry, I've got this!"

        hide uta with dissolve

        show kaginote:
            xalign 0.3
            yalign 1.0
            linear 0.5 xalign 0.5


        call fight_start pass (enemy_pass = enemy_kaginote, no_run = True, enemy_location = "el_c_tunnels_room", hp_porcent = 0.5) from _fight_tunnels_room
        
        $ music_elegia()

        show kaginote:
            xalign 0.5
            yalign 1.0

        hide kaginote with dissolve

        pause 0.2

        show uta c1_bra with dissolve:
            xalign 0.5
            yalign 1.0

        pause 0.3

        show uta happy with Dissolve(0.2)    
        uta "That's more like it!!!"
        uta "I hope you've learned your lesson, you filthy scoundrel. Don't ever mess with a woman again!!"

        $ uta_love += 3
        narrador "[uta.n] Love +3"
        pause 1.0
        narrador "With [kaginote.n] defeated, the girls quickly restrain, tie, and gag him."

        uta "Thank you so much, everyone!"
        show uta shame with Dissolve(0.2)    
        uta "Especially you, young man!"
        uta "I remember seeing you at the auditorium... Right before all of this started..."
        uta "I'm sorry this happened, I have so much to explain... I dragged you all into this mess..." 
        uta "I-I can explain! It all started when..."
        player "Don't worry! There's nothing to explain..."
        player "I can understand the situation a bit so far... That's not important right now anyway..."

        player "I am [player.n]..."

        if player_goal == "Swordsman":
            player "And I will be the greatest swordsman in the world!"
        elif player_goal == "Harem":
            player "And I will have the largest harem in the world!"
            uta "..."
            uta "A harem?"
            uta "Heheh, well, I guess everyone has their own dream, even if it's a bit strange..."
        elif player_goal == "King":
            player "And I will be the King of the World!"
        else: # player_goal == "Pirate"
            player "And I will be the King of the Pirates!"

        show uta happy with Dissolve(0.2)    
        uta "Haha you're quite interesting, [player.n]!"
        uta "It's kind of a crazy idea honestly..."
        show uta shame with Dissolve(0.2)
        uta "But you're strong and brave, I'm sure you'll make it..."

        player "Heh!"          

        player "Alright! [yamato.n], grab that pirate and take him outside. If you see [kalifa.n], hand him over to her."
        yamato "But Captain, I'm going to miss the rest of the fun!"
        player "Hahaha do as I say, there'll be other chances."
        yamato "Yes, Captain!"    
        player "[nami.n], you take [uta.n] to the exit to keep her safe."
        nami "And you, Captain?"

        player "I'll go deal with the rest of the pirates..."
        player "...with [robin.n] of course! That way I don't miss out haha!"
        show uta serious with Dissolve(0.2)
        uta "Wait! I know you've saved me, and I owe you so much... But..."
        uta "I can't leave just yet!!"
        uta "The pirate named [eboshi.n], he's the leader of this group... And he has something very precious to me!"
        uta "I can't leave without getting it back!"
        player "What did he take from you?"        
        uta "He has my father's vivre card!"
        player "I see, it must be really important to you..."
        player "Don't worry and go with [nami.n], I'll get your father's vivre card."
        player "You can count on me!"
        show uta shame with Dissolve(0.2)
        uta "!!!"
        uta "...you saved me, so I think I can trust you!"

        $ uta_love += 1
        $ uta_lust += 2
        narrador "[uta.n] Love +1 and Lust +2"

        show uta neutral with Dissolve(0.2)
        uta "I'll do as you say... Please take care of it!"
        player "(If I manage this, she'll owe me big time. I can't let this unique opportunity slip by!)"

        player "Alright [nami.n], take care of her. Get her something to cover up, poor girl..."

        show uta shame with Dissolve(0.2)
        uta "!!!"
        uta "How embarrassing!!! I can't believe that the first time I meet [player.n], he sees me like this!"

        nami "Hahah don't worry, the Captain is probably very happy to see you like this, even if he won't admit it..." 
        nami "Alright! We're heading out, take care!"

        hide uta with dissolve
        
        player "Let's go [robin.n], we have to keep moving too!"
        robin "Yes, Captain!"


        window hide
        show screen screen_basic_black with Dissolve(0.6)
        $ game.location = "el_church_tunnels"
        #scene BG locations

        hide screen screen_basic_black with Dissolve(0.3)
        window auto

        $ ui_interface = True
        $ Elegia.h = 13

    menu:
        "Advance through the tunnel":
            jump el_church_tunnels2

        "Back":
            jump elegia_church
