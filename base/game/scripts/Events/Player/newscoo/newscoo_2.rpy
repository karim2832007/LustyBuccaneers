# Version event: 3
# Version game: 0.32

default obj_newcoo_2 = False

label newcoo_2:
    
    narrador "You unfold the newspaper and begin to read aloud."

    player "[Dressrosa.n], the land of love and passion, opens its doors to all the most famous warriors from across the seas, and invites them to visit its lands to take part in a unique event!"  
    yamato "That sounds interesting!!"
    player "Hahaha Yes it is!! it was a good introduction..."
    nami "Hahaha, go on, Captain, don't kill the vibe!"  
    player "Hahaha sorry, sorry... okay, where was I..."  
    pause 0.5     
    player "This year, the king of these lands is eager to see great battles, and therefore invites anyone who reads this to join a grand fighting tournament at the Corrida Coliseum!"  
    player "The winner of the tournament will receive a unique prize, an opportunity never seen before — the winner will be rewarded with the Hana Hana Fruit!!"  
    robin "The Hana Hana Fruit!?!"  
    player "Blah blah blah... Too much text..."  

    show robin at center with dissolve

    robin "The Hana Hana Fruit... That's a fruit I've researched quite a lot..."  
    robin "I've always been very interested in getting it..."  
    robin "The fruit gives its user a wide range of possibilities and uses."  

    show nami with dissolve:  
        xalign 0.10  
        yalign 1.0  

    nami "Wow [robin.n], I didn't know you had so much interest in Devil Fruits..."  

    show yamato with dissolve:  
        xalign 0.90  
        yalign 1.0  

    yamato "I don't know about that Devil Fruit, [robin.n], but if you're interested, it must really be powerful!"  
    yamato "What kind of power does it give its user? Anything that makes you a better fighter is a positive thing!"  

    show robin happy with Dissolve(0.2)  
    robin "Hahaha, always with that one-track mind [yamato.n]! While the fruit can be used in combat, I don't think that's its main strength..."  

    show yamato serious with Dissolve(0.2)  
    yamato "Meh... Then I'm not interested anymore..."  

    player "Hahaha, you girls are so funny! [nami.n] is right, I didn't know you were so interested in Devil Fruits [robin.n]."  
    player "If it doesn't really grant many fighting abilities, what's its use? Why are you so interested in it?!?"  

    show robin neutral with Dissolve(0.2)  
    robin "The Hana Hana Fruit is a Paramecia-type Devil Fruit."  
    robin "It gives its eater the ability to 'bloom' any part of their body on any surface, whether inert or living."  

    player "!!?!?"  
    player "What are you saying?!?"  

    robin "That's right, it sounds really strange, but it offers endless uses and advantages, as well as elements of surprise or espionage..."  
    robin "It might not seem like it, but it would be very useful for my research..."  

    player "Now that you mention it, lots of uses for that fruit come to mind..."  
    player "(I can imagine all the perverted things that could be done!! Hahaha)"  

    show robin shame with Dissolve(0.2)  
    robin "I know what you must be imagining, captain, and I assure you that you could do all that and more..."  

    player "(Yes!!! [robin.n] is thinking more and more like I do!)"  

    robin "If you help me get it, then I could help you later..."  

    player "Hahaha, you're always so persuasive, my dear [robin.n]!!!"  

    show robin neutral with Dissolve(0.2)

    nami "Hahaha, you'll never change... Before we go on with this... I have a question!"  
    nami "There's something about this whole tournament thing that doesn't add up for me..."  
    nami "If the Devil Fruit is so useful and can really help anyone who has it..."  
    nami "Why would someone just give it away as a prize like that?!"  
    yamato "Well... if it isn't useful in battle, I'd give it away..."  
    nami "Hahaha don't say that, [yamato.n]... What I'm getting at is, who is this king of [Dressrosa.n]?!?"
    show yamato happy with Dissolve(0.2)    
    show nami berries with Dissolve(0.2)  
    nami "He must be extremely rich to give something like that away just like that..."  
    nami "Maybe we could get something out of all this!!"  
    robin "Well, I wouldn't really try to take advantage of him..."  
    yamato "Hahaha and why not? What are you afraid of..."  
    show robin annoyed with Dissolve(0.2)  
    robin "Well... The current king of [Dressrosa.n] is... {size=40}Donquixote Doflamingo!!{/size}"  
    show nami serious with Dissolve(0.2)  
    show yamato neutral with Dissolve(0.2)  
    yamato "Hahaha I didn't know that!! This could be fun..."  
    nami "W-what!?!... I didn't know that guy was a king... How can he even be a king to begin with... What is the World Government thinking?!"  
    player "Uh... and who's that?!?"  
    yamato "Hahaha it's so funny that you don't know anything, [player.n]. I didn't think there was anyone worse than me on these topics..."  
    yamato "[donflamingo.n] is a Shichibukai!! one of the seven warlords of all the seas!"  
    player "Uh... Shichibukai... why does that ring a bell..."  

    if Arabasta.h == 14:  
        player "Ah right, Shichibukai... That [crocodile.n] was one, wasn't he?!?"  
        player "That guy was really strong and troublesome..."  
        robin "Well, [donflamingo.n] is even more powerful... Or at least very similar in strength.."  
        robin "Let's remember we took advantage of the rain to beat him... I don't know if we could've done it any other way..."  
        player "He really was a problem..."  
        robin "There are many rumors about [donflamingo.n] and his connections to the underworld, to smuggling and arms trafficking..."  
        robin "Obviously none of this is confirmed..."  
        player "Are they all like that?! What a pain..."  

    yamato "All the Shichibukai are really strong! It's not for nothing that the Navy chooses them as one of the Seven Warlords!"  
    robin "Supposedly the Shichibukai were pirates before, but because of their enormous power and all the trouble they caused..."  
    robin "The Navy gave them a pardon for their crimes in exchange for being loyal to the government."  
    nami "Even if they have a pardon... For someone like that to become a king is pretty strange..."  
    player "And what happened to the former king?"  
    yamato "That's a good question!!"  
    player "Hehe! And you who doubted my intelligence, young [yamato.n]... you still have many years of experience to go!"  
    robin "As for their former king... there isn't much information available."  
    robin "It's said there was a big incident and he went mad and was imprisoned... Not much is known!"  
    nami "None of this sounds very logical..."  
    player "Hmm, strange... but interesting!"  


    player "This adventure could be full of fun..."
    show robin neutral with Dissolve(0.2)     
    player "Lots of fights, women, and new places to discover! What could possibly go wrong?!"  
    show yamato happy with Dissolve(0.2)  
    yamato "Hahaha, that's the spirit! I want to see how tough they are on that island..."
    show nami neutral with Dissolve(0.2)    
    nami "[Dressrosa.n] is a summer island, so we could sunbathe and relax through its beautiful streets while the Captain fights!"  
    nami "It could be a nice way to rest if we go there!"  

    player "Alright then, it's settled... Set the sails, we have a new destination!"

    nami "Alright! Don't forget to go buy the Eternal Pose at the shop in this city, there should definitely be one for sale!"    

    pause 0.5

    hide nami
    hide robin
    hide yamato
    with dissolve
    
    $ obj_newcoo_2 = True
    jump m_shells_town