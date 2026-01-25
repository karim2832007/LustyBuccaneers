# Version event: 2
# Version game: 0.27

label elegia_church_inside():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "elegia_church_inside"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_elegia_church_inside

label m_elegia_church_inside():
    if Elegia.h == 11:

        nami "Pss Pss..."
        player "Shhh!"
        robin "{size=20}What beautiful architecture! It's quite old...{/size}"        
        nami "{size=20}Beautiful?!?! This place is so gloomy...{/size}"
        nami "{size=20}I'm seriously starting to doubt your taste [robin.n]! Always the same...{/size}"
        yamato "{size=20}Do you see anything captain? From back here we can't see or hear a thing.{/size}"
        yamato "{size=20}Why are we sneaking in silently and hiding? We should be more direct!!!{/size}"

        player "Shhh!!! Look..."

        $ ui_interface = False

        show uta with dissolve

        player "(It's [uta.n]!!!)"

        show eboshi with dissolve:
            xalign 1.2
            yalign 1.0

        show uta with dissolve:
            xalign 0.5
            yalign 1.0

        show kaginote with dissolve:
            xalign -0.05
            yalign 1.0

        eboshi "{size=40}Damn it!!!{/size}"
        eboshi "{size=40}I knew this was a damn idea!!{/size}"

        eboshi "This wasn't part of the damn plan, [uta.n]!!!"
        eboshi "The Navy surrounded the island. We're cornered..."
        eboshi "They already have several squads around and even a Captain present!"
        eboshi "That other group is also after us..."

        uta "And what did you expect!? You knew there would be risks when you agreed... We have to push forward, it's necessary!"

        eboshi "What you call necessary is leading us straight to the grave!"

        kaginote "Eboshi is right!"  
        kaginote "Those pirates... The ones looking for you [uta.n]... They almost killed me. I barely escaped!"
        kaginote "That Captain is insane!! And he's really strong!"  
        kaginote "Our tricks won't work again... There won't be second chances!"  

        kaginote "We can't go on like nothing happened. We need a new plan... Now!"

        uta "No! You can't do this to me, we had a deal. We were doing this so He would come..."
        uta "We'll be safe here, this place is really hard to find... We just need to think calmly about our next move!"
        uta "We only need more time... Once the news of my capture spreads He surely will..."

        eboshi "{size=40}Enough, damn girl!!{/size}"
        eboshi "The island is completely surrounded... We're out of time!"
        eboshi "That deal we talked about means nothing to me now..."
        eboshi "Even if you were the daughter of the Pirate King himself, I wouldn't care anymore!!"
        eboshi "The situation changed... Do you get that?!? But it's all clear to me now..."
        eboshi "The plan failed... There are too many enemies... And now they're hunting us!"
        eboshi "We have only one option left..."

        show kaginote:
            xalign -0.05
            yalign 1.0
            linear 0.5 xalign 0.05

        show eboshi:
            xalign 1.2
            yalign 1.0
            linear 0.5 xalign 1.0

        pause 0.5

        uta "No... Wait, I know I can fix this..."
        eboshi "Too late, sweetheart..."
        eboshi "{size=40}Now we'll be real pirates!{/size}"
        eboshi "And we're kidnapping you for real!"
        uta "... What did you say?"
        eboshi "Grab her [kaginote.n]!!!"
        kaginote "Excellent Captain!!"
        kaginote "No time to waste!"

        show kaginote:
            xalign 0.05
            yalign 1.0
            linear 0.5 xalign 0.15


        pause 0.5

        uta "No! Wait! You can't do this!"
        uta "You're not thinking clearly..."
        eboshi "We're pirates, or did you forget? We can do whatever we want..."
        uta "You're making a terrible mistake!!! Don't come closer!!"

        "The pirates grab her tightly. [uta.n] struggles, but is quickly restrained."

        show uta anger with Dissolve(0.2)

        uta "LET ME GO! YOU'RE INSANE!"
        uta "When He arrives, He'll kill you all!"
        kaginote "He's never coming, girl, we're the only ones here!... I'll treat you real nice... if you don't resist...."
        eboshi "Easy [kaginote.n]!!!"
        eboshi "Bring her here, and follow me..."
        eboshi "Let's head to the tunnels! No one will find us there. We'll figure out how to handle this..."
        eboshi "Even the Navy has to deal with this carefully..."
        eboshi "This girl is still extremely valuable..."
        eboshi "If anything happens to her, we're dead anyway... So keep a close watch!"
        kaginote "Yes Captain!"
        eboshi "Good... Let's go!"
        uta "Let me go you filthy pirates!!! Even knowing who you're messing with you treat me like this!!!"
        uta "You're digging your own graves!!!"

        hide uta
        hide eboshi
        hide kaginote
        with dissolve

        "The footsteps fade. The echo of [uta.n]'s screams bounce off the dark walls."

        player "(So this was all part of a plan?!?)"
        player "(But now she's really been kidnapped...)"
        player "(Nothing's changed if I think about it...)"
        player "Girls! They're taking her into the tunnels... Under the church."

        show yamato with dissolve:
            yalign 1.0
            xalign 0.5

        show robin with dissolve:  
            yalign 1.0  
            xalign 0.05  

        show nami with dissolve:  
            yalign 1.0  
            xalign 0.95  

        yamato "There may not be any other exits... This might actually make our job easier!"
        robin "It's a possibility..."
        show nami c1 serious with Dissolve(0.2)
        nami "What surprises me is that everything was planned from the beginning..."
        nami "Everything that happened in the auditorium was just a show..."
        robin "They mentioned Him several times... I don't know who they could be referring to, but it was someone they deeply respect!"
        nami "That was really strange too... Even the Navy should respect he..."
        robin "It could be a relative of [uta.n] or someone very important or influential..."
        player "Well, it is strange... But if we want to learn more, we just have to follow them and ask ourselves..."
        yamato "That's the spirit, Captain!"
        robin "I won't deny I'm curious to see how these events unfold..."
        show nami c1 berries with Dissolve(0.2)
        nami "If she has important relatives, we might be able to get something valuable out of this..."

        player "Hahaha that's the spirit, girls!"
        player "No time to lose! Let's go, follow them!"

        $ nami_love += 2
        $ robin_love += 2
        $ yamato_love += 2
        narrador "[nami.n], [robin.n] and [yamato.n] Love +2"    


        window hide
        window auto
        hide robin 
        hide yamato
        hide nami
        with dissolve

        $ ui_interface = True
        $ Elegia.h = 12

    menu:
        "Go down into the tunnels":
            #narrador "Event not available in this version, please wait for v0.28"
            #jump m_elegia_church_inside
            jump el_church_tunnels

        "Back":
            jump elegia_church
