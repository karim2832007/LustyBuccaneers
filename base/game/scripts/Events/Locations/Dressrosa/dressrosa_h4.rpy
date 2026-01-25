# Version event: 3
# Version game: 0.33

label dressrosa_h4():
    show police1:
        yalign 1
        xalign 1.1
        
    show police2:
        yalign 1
        xalign -0.1

    with dissolve


    police1 "That toy soldier causing trouble again..."
    police1 "He won't give up... We'll catch you, toy soldier!!"
    unknown "Hahah I'd like to see you try!!"
    police2 "Stay away from the colosseum and come back here!!"
    police2 "Stop right now!!"

    show cut_colosseum_toy with Dissolve(0.3):
        yalign 0.05
        xalign 0.5
    
    pause 0.3
    
    kyros "Hahaha you're too slow!!"
    kyros "Look... I've got one foot in the colosseum, and you know the law here well!"
    kyros "From this point on it's completely forbidden for the Marines or the police to enter!"
    kyros "It doesn't matter if a criminal goes in... you can't!"
    kyros "No matter how much you want to, you won't be able to go in after him!"
    kyros "You already know that inside the colosseum only the Donquixote family is in charge."
    kyros "If you enter or dare to fire, you'll be hunted down and sent to prison, so leave now!"
    police1 "Damn it... We'd better go for now..."
    police2 "You won't be so lucky next time..."

    hide police1
    hide police2
    with dissolve


    yamato "What a strange island... the police chasing a toy is something I never would've believed I'd see..."
    yamato "Though I have to admit that toy's got some attitude!!"
    yamato "He made those cops look completely ridiculous!"
    pause 0.3
    narrator "A moment later, the police officers walk away furious and frustrated."
    narrator "Then the toy soldier jumps, landing right in front of you."

    $ _window_hide()

    hide cut_colosseum_toy with Dissolve(0.3)

    show kyros toy with dissolve:
        yalign 1.0
        xalign 0.5

    pause 0.5

    kyros "Damn it... Those cops made me waste my time, she's surely already registered... I should've stopped her!"
    player "Hahah you did great, kid!! You made those cops look ridiculous hahaha!"
    kyros "Mnm?! Who are you calling kid!! I'm a grown man, you know!!"
    player "Hahah sorry, sorry! You're very small and I assumed wrong..."
    player "We're still not used to seeing so many toys walking around here!"
    kyros "So you're tourists!! Sorry for scaring you—do you need me to guide you or recommend somewhere to go?!"
    
    show nami with dissolve:  
        xalign 0.10  
        yalign 1.0  

    nami "Hahaha suddenly he's very polite!"
    player "Hahaha you're very funny!!"
    kyros "Well of course I am!!! I seem funny to you, don't I?!"
    kyros "I'm a toy after all!! And toys are for making people smile!"
    player "Hahaha well, you sure are!"

    show yamato with dissolve:  
        xalign 0.90  
        yalign 1.0

    yamato "Tell us, sir... Are you part of the colosseum? You seemed very well informed about the rules..."
    kyros "Well... let's say I was once part of all this, but it's been a long time, you know... I'm away from the administration now."
    yamato "Uh, what a shame—the captain just signed up, a bit of information would be useful to us."
    kyros "You, kid, you signed up for the tournament?!?"
    kyros "Don't you know what's at stake?!? A large number of strong fighters from all over the world have come..."
    kyros "It's really dangerous for you to take part!!"
    kyros "You should rethink it right now while you still can..."
    nami "Hahah don't worry, soldier, our captain is really strong!!"
    player "Hahaha that's right, I've got it under control!"
    kyros "Mnmnm... Well, I suppose there's nothing I can do to stop it..."
    kyros "Please be careful—there are very dangerous people, don't overexert yourself!"
    kyros "Ah... and one more thing, if I may ask you..."
    kyros "If you see a pink-haired gladiator, please tell her the same thing!"
    kyros "She has nothing to prove or to push herself for... the main thing is that she takes care of herself!"
    player "(A pink-haired girl... Could that be [rebecca.n]?!?)"
    player "Alright... No problem, I'll pass along your message!"
    player "Well then, that's all—see later girls, toy soldier... I'm going in!"
    show nami happy with Dissolve(0.2) 
    nami "Alright, Captain, you can do it!"
    nami "We'll be watching and cheering for you from the stands! The rounds will probably start soon!"
    show yamato happy with Dissolve(0.2)
    yamato "Hahaha, good luck, Captain, show everyone here how strong you are!"
    yamato "And don't forget, [player.n], don't draw too much attention..." 
    yamato " {size=25}Remember we're pirates!{/size}"
    player "Don't worry, when you come back you'll see me with the Devil Fruit for [robin.n]!!"



    $ _window_hide()
    hide kyros
    hide yamato
    hide nami
    with dissolve
    pause 0.2
    $ Dressrosa.h = 5
    jump dr_ac_colosseum
