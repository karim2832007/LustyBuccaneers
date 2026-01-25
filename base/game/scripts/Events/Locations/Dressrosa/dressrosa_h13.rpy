# Version event: 2
# Version game: 0.38

label dressrosa_h13():
    $ ui_interface = False

    $ _window_hide()
    show screen screen_black with Dissolve(0.6)
    show events dressrosa h6 h6_gatz
    play ambient "ring" fadein 1.0
    hide screen screen_black with Dissolve(0.3)

    gatz "{size=40}Weeeeeeeeeelcome back, ladies and gentlemen, toys and dolls!{/size}"
    gatz "{size=40}Welcome everyone once again to the Corrida Coliseum!{/size}"

    gatz "Tonight, two warriors will clash in an earth-shaking duel!"
    gatz "In the west corner, a brave newcomer who's captured all our hearts with his incredible victories!"
    gatz "A champion of the people, undefeated so far, give it up for the fearless [player.n]!!!"

    pause 0.5
    unknown "{size=40}[player.n]!! [player.n]!! [player.n]!!{/size}"

    gatz "And in the east corner, a fearsome veteran from the Majiatsuka Kingdom!"
    gatz "A man with a reputation as a bone-crushing brute, who leaves only broken bodies in his wake!"
    gatz "He's big, he's bad, he's hungry for glory, the one and only {size=40}{outlinecolor=#8b0000}{color=#ff6666}Roooollin Loooogan{/color}{/outlinecolor}!!!{/size}"
    pause 0.5   
    unknown "[logan.n]!! [logan.n]!! [logan.n]!!"
        
    $ game.location = "dr_ac_co_arena"
    show BG locations
    hide events dressrosa h6 h6_gatz with dissolve
    

    $ enemy_figth.hp = enemy_figth.max_health
    show expression enemy_logan.image with Dissolve(0.5):
        xalign 0.5
        yalign 0.5

    pause 0.5

    gatz "[logan.n] versus [player.n]!!!"
    gatz "Our Colosseum shakes with excitement! Two titans, one arena, this is what we've been waiting for!"
    gatz "Only one will walk out victorious and claim eternal glory this day!"
    gatz "So without further ado..."
    gatz "Let the battle... BEGIN!!!"
    pause 0.5
    logan "Heh heh... Look at you, all fired up. Enjoy the cheers while they last, kid."
    logan "These people love a hero now, but just wait till they see me snap you like a twig!"
    pause 0.5
    player "Big talk for someone who's about to eat dirt."
    pause 0.5
    logan "Oh? The little hero has some bite! I remember seeing you earlier... sneaking around with that pretty little girl, [rebecca.n]."
    logan "You two looked cozy in the hallway. What were you whispering, sweet nothings before the big fight?"
    player "Leave her out of this, [logan.n]! I'm warning you..."
    pause 0.5
    logan "Heh heh..."
    logan "Why? Afraid the crowd will learn how soft you really are? That you're fighting for a girl's favor?"
    logan "Pathetic! A real warrior should focus on the fight, not on pretty dolls."
    player "[rebecca.n] is twice the warrior you'll ever be! And she's got more honor in her little finger than you do in your whole body!"
    logan "Ha! Honor won't save her or you. After I'm done here, maybe I'll pay dear [rebecca.n] a visit."
    logan "She'll be heartbroken seeing you in pieces... but don't worry. I'll console her for you."
    logan "Perhaps I'll wrap these arms around her delicate frame, the same way I'm about to crush you!"
    pause 0.5
    player "He... You bastard...!"
    player "Look, I wasn't going to forgive you anyway... but it seems you want to suffer."
    player "Say another word about [rebecca.n], and I swear you won't leave this arena conscious!"
    pause 0.5
    logan "Heh heh heh..."
    logan "Hit a nerve, did I? Good! Get mad! It won't help you, but at least you'll scream loud before I break you."
    logan "I can already see it... you on the ground, begging for mercy, while [rebecca.n] watches."
    logan "Maybe I'll make her watch up close. I'll have her kneel by your broken body as I finish you off!"
    player "[logan.n], you're digging your own grave."
    logan "Bold words from a dead man walking."
    logan "Face it, 'hero', you're outmatched. I'm going to enjoy every second of this."
    player "The only one who'll be broken today is you."
    logan "Talk is cheap. Let's see you try! I'll throw you around like a rag doll."
    player "I've heard enough. You're going to regret every word."
    logan "Hah! Show me what you've got, little champion! I'll show [rebecca.n] who the real man is!"
    player "I'm going to shut that filthy mouth of yours right here and now!"
    logan "Come on then! Let's dance, hero!"
    player "With pleasure!"

    call fight_start pass (enemy_pass = enemy_logan, no_run = True, no_interface = True) from _fight_enemy_logan

    gatz "[player.n] won't stop hitting [logan.n]!"
    gatz "{size=40}This is a massacre!{/size}"
    pause 0.5
    logan "Gahh—!" 
    logan "You little... I'll crush you! Rolling Cradle!"
    player "Ha! Not today!"
    logan "OOGH!" 
    player "Get up, [logan.n]. I'm not done making you pay."
    gatz "Another direct hit!! It looks like [logan.n] can't take it anymore!"
    logan "W-wait... I—"
    logan "Please stop!"
    player "What's wrong? Weren't you going to break me? Show me that 'strength' of yours!"
    logan "I surrender... I can't go on..."
    player "..."
    player "{size=40}This is for [rebecca.n]!{/size}"
    logan "OOF—!"
    logan "N-no more... I... I surrender!"
    logan "I quit! I QUIT!!"

    $ black_to_img("events dressrosa h6 h6_gatz")

    gatz "This battle seems to be over!"
    gatz "Even though [logan.n] has begged for mercy repeatedly, [player.n] doesn't want to let him go and keeps punishing him!"
    gatz "!!!"    
    gatz "But wait! With his last bit of strength, [logan.n] tries to escape!"
    gatz "He's running toward the edge of the platform!"
    gatz "[logan.n] is desperate and it looks like he wants to jump into the water with the Little Fighting Fish!!"
    logan "(He'll kill me if I don't jump)"

    $ black_to_img("events dressrosa h13 h13_1")
    pause 1.0
    gatz "Desperate and with no chance at all..."
    gatz "[logan.n] just jumped into the water!!"
    player "(Damn... He runs fast for such a big guy...)"
    pause 0.5    
    gatz "{size=40}He's definitely not thinking straight!!{/size}"

    play sound ["<silence 0.8>","water_boom"]
    $ black_to_img("events dressrosa h13 h13_2")
    pause 1.0
    player "Get back here, you coward, don't run away!!!"
    gatz "Hahaha, look at the dive he just took!"
    gatz "As small waves start to form, the Little Fighting Fish surround him quickly!!"

    $ black_to_img("events dressrosa h13 h13_3")
    pause 1.0
    gatz "The waters look calm... but from here you can see what's happening down below!!"
    gatz "There's no way [logan.n] should've done that!"
    gatz "Send the guards in right now!!"
    gatz "[logan.n] can't go on anymore!!!"
    gatz "[player.n] has done the impossible again!! [player.n] is truly unstoppable!!!"
    unknown "{size=40}[player.n]!! [player.n]!! [player.n]!! [player.n]!!{/size}"

    #$ _window_hide()
    ##hide expression enemy_logan.image with Dissolve(0.8)
    #pause 0.5
    
    $ black_to_img("events dressrosa h6 h6_gatz")

    gatz "While we try to recover [logan.n]... Or what's left of him..."
    gatz "Don't go anywhere, we'll be back soon! We're reaching the tournament's climax!!!"
    gatz "We'll be right back with more!"
    pause 0.5
    player "(Alright... I've done my part... Now it's time for my reward!)"


    stop ambient
    $ Dressrosa.h = 14
    $ _window_hide()
    $ ui_interface = True
    jump dr_ac_co_fighters_preparations
