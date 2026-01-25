# Version event: 3
# Version game: 0.28

label el_church_tunnels3():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "el_church_tunnels3"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_el_church_tunnels3

label m_el_church_tunnels3():
    if Elegia.h == 14:
        $ ui_interface = False

        narrador "Finally, after walking for a while, you reach a large room..."
        narrador "In the distance, you hear voices, so you stealthily approach with [robin.n]."
        narrador "With each step, the voices become clearer until you can see them."

        show eboshi c1:
            xalign 1.1
            yalign 1.0

        show hanagasa c1:
            xalign 0.10
            yalign 1.0

        with dissolve    

        eboshi "We finally made it. This is the door we were looking for..."
        eboshi "Now that we know the path is clear, there's nothing to worry about."
        eboshi "Everyone else must be in a lot of trouble up there... We have to hurry..."
        eboshi "We'll use them as bait and escape... There's no other alternative, but first..."
        eboshi "Let's go back before [kaginote.n] tries something stupid with [uta.n] and ruins everything."

        hanagasa "And what if the brat resists, Captain?"

        show cut_vivre_card_h1 with dissolve:
            xalign 0.5
            yalign 0.3

        eboshi "She won't dare. As long as I have this... Red Hair's Vivre Card, she'll do exactly as I say."

        robin "{size=20}That's the Vivre Card, Captain!{/size}"
        robin "{size=20}Did he say Red Hair?! Did I hear that right?!...{/size}"

        player "(So that's where it is. I can't let it stay in their hands!)"

        robin "{size=20}Captain, maybe we should analyze this more carefully, if we heard right, it could...{/size}"
        player "You, [eboshi.n]! Hand over that piece of paper right now!"

        hide cut_vivre_card_h1 with dissolve

        eboshi "Mnmnm?!?"
        eboshi "You again? You're the one from the auditorium... The bastard who defeated [kaginote.n]..."
        eboshi "What terrible timing... I don't know what you want, but I have no time to waste..."
        eboshi "[hanagasa.n], take care of him—make it quick."

        hanagasa "Gladly, Captain. Get ready, twig!"

        hide eboshi with dissolve

        show hanagasa c1:
            xalign 0.10
            yalign 1.0

            linear 0.5 xalign 0.5

        pause 0.5
        call fight_start pass (enemy_pass = enemy_hanagasa, no_run = True, no_interface = True) from _fight_enemy_hanagasa
        
        $ music_elegia()

        narrador "After a brief fight, you manage to take down [hanagasa.n]. His body drops like a sack of potatoes, lying unconscious on the damp rocks of the room."
        hanagasa "N-No... I don't believe it..."
        hide hanagasa with dissolve

        pause 0.5

        show eboshi c1 with dissolve:
            xalign 0.5
            yalign 1.0

        eboshi "Damn useless fools! One after another, they all fall..."
        eboshi "I'm surrounded by incompetents!"
        eboshi "I'll have to deal with this myself... I can't believe the Jellyfish Pirates have fallen this far!"
        eboshi "If I fall, you're coming with me, bastard!"

        pause 0.5
        call fight_start pass (enemy_pass = enemy_eboshi, no_run = True, no_interface = True) from _fight_enemy_eboshi

        $ music_elegia()

        narrador "The cunning of [eboshi.n] isn't enough to stop your advance. Eventually, he drops to his knees, gasping for breath."
        eboshi "Unbelievable... To end up like this, defeated by some rookies..."
        eboshi "All because of that damn bitch..."

        hide eboshi with dissolve

        narrador "With him defeated, you snatch the Vivre Card and carefully store it."
        narrador "+1 Vivre Card"

        show robin c1 happy with dissolve

        robin "Well done, [player.n]! It's amazing how you took care of both pirates. I'm truly impressed!"
        robin "With this, [uta.n] will be so happy."
        player "(And she'll owe me big time, hahaha I'm a genius!)"
        player "Thanks, [robin.n]. Now let's get outside, we have to return the Vivre Card to [uta.n]!"
        robin "(Maybe I should warn the captain... But he looks so happy, I guess I'll warn him later!)"

        window hide
        show screen screen_basic_black with Dissolve(0.6)
        $ game.location = "elegia_church"

        hide robin

        show kalifa c1:
            xalign 0.15
            yalign 1.0

        show uta c1_bra:
            xalign 0.85
            yalign 1.0

        hide screen screen_basic_black with Dissolve(0.3)
        window auto

        narrador "As you exit the church, you find [nami.n], [yamato.n], [uta.n], and [kalifa.n] discussing something."

        kalifa "Let's go over this again... This guy says something completely different from what I've been told."
        kalifa "[kaginote.n] claims that all this mess was orchestrated by [uta.n] herself..."
        nami "How can you trust this guy..."
        nami "Just look at his face, does he look trustworthy to you!"
        kalifa "Heh! he's really a loser... Not that I really care, but I do need to report something to [koby.n]."
        kalifa "!!!"
        kalifa "Well, look who we have here..."
        player "[kalifa.n], a pleasure to see you again! You're as gorgeous as always..."
        uta "!!!"
        show uta anger with Dissolve(0.2)
        kalifa "Not sure I'd say the same..."
        uta "Don't talk about [player.n] like that... He's kind, strong, and attractive..."
        uta "He just saved me from those filthy Jellyfish pirates"
        kalifa "Hahaha I didn't know you had a fan club, [player.n]..."
        kalifa "Too bad it's just little girls... They're no match for a woman like me..."
        uta "What did you just say?!?!"
        player "Calm down, girls, no need to fight!... There are more important things to focus on right now..."
        player "There are two more pirates back there, luckily there was another nearby exit..."
        player "One of them was really big..."
        kalifa "I'll deal with those losers later..."
        kalifa "Since you're here..."
        kalifa "Tell me, do you know if [uta.n] was involved in her own kidnapping?... What do you have to say"

        menu:
            "She's not involved":
                show uta c1_bra neutral with Dissolve(0.2)
                player "What kind of question is that! Of course she's not involved."
                player "Just look at what they did to her clothes... Thank goodness my team and I got there in time!"
                player "Otherwise... who knows what [kaginote.n] might have done!"

                $ uta_love += 2
                narrador "[uta.n] Love +2"

            "Say nothing":
                show uta c1_bra anger with Dissolve(0.2)

                uta "Of course not, how can you say that!"
                uta "That pirate tried to rape me in the caves! Look at my clothes!"

        kalifa "I understand, as a Marine it's my duty to ask... I'll trust you all!"
        show uta c1_bra neutral with Dissolve(0.2)
        uta "[player.n]!"

        kalifa "I'm leaving now, I have no more questions and it seems you have things to discuss..."
        kalifa "I won't waste any more time here..."
        hide kalifa with moveoutleft
        uta "Yes, go far away better..."

        nami "Captain, the ladies are lining up for you!"
        pause 1.0
        show uta c1_bra at x_move(x_start=0.85, x_end=0.5, dur=0.3)

        uta "[player.n]!"
        uta "Did you get it?"
        uta "Please tell me you have it!"

        player "Of course, I gave you my word I'd get it!"
        player "Here, take it"

        narrador "You hand the Vivre Card to [uta.n]"
        narrador "-1 Vivre Card"

        show uta c1_bra happy with Dissolve(0.2)
        uta "Thank you [player.n]!"
        uta "I knew I could truly count on you!" 
        uta "..."
        show uta c1_bra shame with Dissolve(0.2)      
        uta "I know I'm asking a lot... Not only did you save me..."
        uta "But you also recovered my most precious possession."
        uta "But I have to ask you for one more favor!"

        player "Just say it, whatever you ask, I'll do it for you!"
        show uta c1_bra neutral with Dissolve(0.2) 
        uta "Great! Then..."
        uta "Let me join your crew!!!"
        uta "I want to become a pirate like my father, sail the seas, and find him myself!"
        uta "Please [player.n], help me reunite with my father!"

        menu:
            "Do you want [uta.n] to be part of the crew?"
            "Yes":
                $ uta_crew = True
                player "Hahaha!!!"
                player "There's no way I could turn down a request like that!"
                uta "Really?! Are you serious!?!"
                player "Of course, I'm a man of my word!"
                uta "You're the best [player.n]!"
                uta "I'm going to change clothes and get my things ready"
                player "The ship is at Elegia's port"
                player "We'll be waiting for you there"
                
            "I need to think about it":
                player "Being a pirate is dangerous..."
                player "I need to think it through, I don't want to put you at risk..."
                uta "I understand [player.n], you've already done so much for me... I know I might be asking too much..."
                uta "When you decide, you can find me at the castle's auditorium... Where we first met!"
                uta "I'll be waiting for you!"
                uta "Please think it through and come see me!"


        hide uta with moveoutright

        window hide
        window auto
        with dissolve

        $ ui_interface = True
        $ Elegia.h = 15
        jump elegia_church

    menu:
        "Back":
            jump el_church_tunnels2
