# Version event: 3
# Version game: 0.39

image movie_dr_h14_rebecca_blowjob slow = MovieFallback(play="movie/rebecca/dr_h14_blowjob/1.webm", image="movie/rebecca/dr_h14_blowjob/img.webp", character="rebecca")
image movie_dr_h14_rebecca_blowjob fast = MovieFallback(play="movie/rebecca/dr_h14_blowjob/2.webm", image="movie/rebecca/dr_h14_blowjob/img.webp", character="rebecca")
image movie_dr_h14_rebecca_blowjob cum  = MovieFallback(play="movie/rebecca/dr_h14_blowjob/3.webm", image="movie/rebecca/dr_h14_blowjob/img.webp", character="rebecca")

image dr_h14_rebecca_blowjob_cum = "movie/rebecca/dr_h14_blowjob/cum.webp"

label event_dr_h14_rebecca_blowjob:

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    $ _window_hide()
    show screen screen_black onlayer master with Dissolve(0.8)
    #play sound [ "blowjob_mid_01","<silence 0.2>","blowjob_02","blowjob_03","blowjob_01","<silence 0.2>","blowjob_01"] loop
    play sound "footjob_1" loop
    show movie_dr_h14_rebecca_blowjob slow
    hide screen screen_black onlayer master with Dissolve(0.8)


    rebecca "(I.. I can't believe we're doing something like this...)"
    player "Easy now, [rebecca.n]. Just relax and take it slow—start by licking gently."
    player "This will relieve all my tension, I promise."
    rebecca "This is all new to me... I've never been this close to a man before. But for you, I'll do my best—tell me if I'm doing it right."
    rebecca "Your... it's so warm and firm..."
    player "You're a natural already. Keep going."
    rebecca "The scent is overwhelming... but strangely, it's not unpleasant."
    rebecca "(My heart's racing... Is this what gratitude feels like?)"

    $ _window_hide()
    pause 2.0

    player "That's it, [rebecca.n] your mouth feels amazing."   
    rebecca "I've only fought in the arena before... never imagined I'd be doing this."  
    player "And how does it feel? Do you like having me so close?"  
    rebecca "It's throbbing so much... and the taste is salty, but intriguing."  
    rebecca "(Why does this make my body feel so hot?)"  
    rebecca "I... I think I'm starting to enjoy it."  
    player "Haha, I knew you would. Don't stop now—use your tongue more."   
    rebecca "Like this? Am I pleasing you?"  
    player "Perfectly. You're making me forget all about the battles."  
    
    $ _window_hide()
    pause 2.0
    jump event_dr_h14_rebecca_blowjob_slow


label event_dr_h14_rebecca_blowjob_slow:
    $ _window_hide()
    show movie_dr_h14_rebecca_blowjob slow
    pause 0.5

    rebecca "Does this feel good to you?" 
    rebecca "Is [rebecca.n]'s touch making you relax?"  
    player "It's paradise... don't change a thing."   
    rebecca "Your skin is so smooth... I can feel every vein."  
    rebecca "I never thought I'd be so bold..."  

    $ _window_hide()
    pause 0.5

    menu:
        "Keep going":
            show movie_dr_h14_rebecca_blowjob slow
            pause
            jump event_dr_h14_rebecca_blowjob_slow

        "Faster":
            player "Go faster [rebecca.n]!!"
            jump event_dr_h14_rebecca_blowjob_fast
    

label event_dr_h14_rebecca_blowjob_fast:
    $ _window_hide()
    show movie_dr_h14_rebecca_blowjob fast

    pause 3.0
    
    player "Your wet mouth is driving me crazy!"
    player "(I won't last much longer at this rate!)"
    rebecca "The aroma is intensifying... it's making me dizzy."   
    rebecca "My saliva is everywhere... I can't control it."  
    rebecca "I love how you fill my mouth..."  
    player "(She's opening up so fast— from gladiator to this?)"  
    rebecca "I don't want to stop sucking!"  
    rebecca "Deeper... let me take more of you."  
    player "Yes— just like that!"  
    rebecca "Am I doing it right?"  

    $ _window_hide()
    pause 2.0

    menu:
        "Slower":
            jump event_dr_h14_rebecca_blowjob_slow

        "Keep going":
            show movie_dr_h14_rebecca_blowjob fast
            pause
            jump event_dr_h14_rebecca_blowjob_fast

        "Cum":
            jump event_dr_h14_rebecca_blowjob_cum


label event_dr_h14_rebecca_blowjob_cum:

    rebecca "Your dick is pulsing, [player.n]!"
    rebecca "It smells so strongly of... release."
    player "(This innocent princess has a wild side buried deep!)"
    rebecca "You're rock hard now... twitching like it's ready to explode."
    rebecca "Do you want to finish inside my mouth?!"
    player "Yesss... Take every drop, [rebecca.n]!"

    show movie_dr_h14_rebecca_blowjob cum
    
    $ _window_hide()
    pause 2.4

    play sound "cum_01"
    show dr_h14_rebecca_blowjob_cum  with flash
    hide movie_dr_h14_rebecca_blowjob

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    player "Damn, that was intense!"
    rebecca "So much came out..."    
    rebecca "I'm not experienced at this yet, but I'll improve for next time!"

    window hide
    window auto
    pause 1.0
    jump event_dr_h14_rebecca_blowjob_end


label event_dr_h14_rebecca_blowjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_dr_h14_rebecca_blowjob
    hide dr_h14_rebecca_blowjob_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_dressrosa()


    player "You were incredible, [rebecca.n]... seriously."
    rebecca "R-really? My heart was pounding the whole time... I was so nervous I'd disappoint you."
    player "Disappoint me? You just made me see stars."
    player "The way you looked up at me... that shy little smile even while... yeah, it's burned into my memory."
    show rebecca c2 shame with Dissolve(0.2)
    rebecca "Don't say such embarrassing things..."
    rebecca "But... I'm glad it felt good for you. Knowing that makes me happy too."
    rebecca "If this is how I can support you... how I can be close to you... then I want to get better at it."
    player "We'll have plenty of time to practice, don't worry."
    rebecca "Promise?"
    player "Promise."
    pause 0.5
    show rebecca c2 neutral with Dissolve(0.2)
    rebecca "So..."        
    rebecca "Did I help relieve your stress?"  
    player "More than you know."

    $ RPGPlayer.full_heal()

    rebecca "Good... Anything for you [player.n]..."     

    $ rebecca_lust += 2
    $ rebecca_love += 1
    narrador "[rebecca.n] Lust +2 and Love +1" 

    narrador "A distant trumpet sounds from the arena, announcing the final match is about to start."
    rebecca "That sound... the finals are about to start. You should go."
    player "Right. It's time."
    rebecca "Be careful [player.n]... Don't underestimate your opponent, I know you'll be able to defeat him!"
    rebecca "You're just one step away from the grand final vs Diamante, you have to win!" 
    rebecca "Please take care of yourself and come back to me safe and sound."
    player "Don't worry! With everything you've done for me today, I feel stronger than ever!"
    rebecca "Good luck! I'll head out first. I'll be cheering you on and watching your fight! We'll talk later, take care!"


    $ _window_hide()
    hide rebecca with moveoutright
    pause 0.5
    
    $ game.clock.next()
    $ ui_interface = True
    $ Dressrosa.h = 15
    jump expression game.location
