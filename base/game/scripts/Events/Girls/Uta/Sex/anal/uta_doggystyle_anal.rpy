# Version event: 4
# Version game: 0.33

default uta_doggystyle_anal = 0

image movie_uta_doggystyle_anal_ass = MovieFallback(play="movie/uta/doggystyle/anal/ass.webm", image="movie/uta/doggystyle/anal/ass.webp", character="uta")

image movie_uta_doggystyle_anal slow = MovieFallback(play="movie/uta/doggystyle/anal/1.webm", image="movie/uta/doggystyle/anal/img.webp", character="uta")
image movie_uta_doggystyle_anal fast = MovieFallback(play="movie/uta/doggystyle/anal/2.webm", image="movie/uta/doggystyle/anal/img.webp", character="uta")
image movie_uta_doggystyle_anal cum  = MovieFallback(play="movie/uta/doggystyle/anal/3.webm", image="movie/uta/doggystyle/anal/img.webp", character="uta")

image movie_uta_doggystyle_anal_ass_cum = MovieFallback(play="movie/uta/doggystyle/anal/ass_cum.webm", image="movie/uta/doggystyle/anal/ass_cum.webp", character="uta")

image uta_doggystyle_anal_cum = "movie/uta/doggystyle/anal/cum.webp"


label uta_doggystyle_anal:

    if uta_doggystyle_anal == 0:

       
        player "[uta.n]... I can tell you're a little uneasy today."
        show uta shame with dissolve
        uta "[player.n]... it's just that you make me nervous when you look at me like that..."
        uta "My heart is beating so fast..."
        player "You know we can take it slow, no rush. Step by step. But this time I want to try something new..."
        uta "Slowly... I like how that sounds. I've never been this close to anyone, you know that..."
        uta "I've never shared anything as intimate as what we did last time... It feels strange, but I really liked it."
        show uta happy with dissolve
        uta "I feel weird... but at the same time happy."
        player "I just want you to smile."
        uta "And what if I don't know what to do...? What is it you want to try this time?!?"
        player "You don't have to know anything. I'll guide you, and we'll only go as far as you want."
        show uta shame with dissolve
        uta "If it's with you... I want to try it."
        player "Alright. Slowly... and if you say stop, we stop. Deal?"




    else:
        player "Do you want to try again?"
        player "Slowly... If you say stop, we stop. Deal?"
        uta "I'll love it!"

    call uta_check pass (check_love = 50, check_lust = 50) from _uta_check_doggystyle_anal
           
    pause 0.5
    window hide
    show uta neutral c1_underwear with dissolve
    pause 0.5
    show uta neutral c1_naked with dissolve

    uta "I know you like my physique..."
    uta "But I hope I'm ready for this... "
    uta "You really are someone important for me..."

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show movie_uta_doggystyle_anal_ass
    hide screen screen_black with Dissolve(0.8)

    pause 2.5

    if uta_doggystyle_anal == 0:

        player "(Look at this... Fuuuck, this is sooooo fucking good...) "
        player "(Her ass is so soft and bouncy!)"        
        player "(It's a marvel... A work of art)"
        player "(How did I get here... How lucky am I?!)"
        uta "(Mmnmnm, i'm getting wet...)"
        uta "(Only the thought of [player.n] touching me like that... Is turning me on so much...)"
        uta "Please start now [player.n], I'm getting a little nervous... Do you like what you see?"

    else:
        player "(Will there ever be a day when I get tired of looking at this?)"
        uta "My pussy is dripping right now..."
        uta "I've been a naughty girl, haven't I?"
        uta "I think i deserve to be punished...."
        uta "Please don't make me wait any longer..."

    show screen screen_black with Dissolve(0.8)
    play sound "footjob_1" loop
    play gems ["<silence 0.8>","gem_02","<silence 0.8>"] loop
    #play sound "titjob_1" loop
    hide movie_uta_doggystyle_anal_ass
    show movie_uta_doggystyle_anal slow

    hide screen screen_black with Dissolve(0.8)

    $ uta_doggystyle_anal += 1

    uta "(Mmnmnm, i'm getting more and more wet...)"
    uta "(He's grabing my ass... And thrusting deep inside me)"
    uta "(He's moving his hips too fast... It's driving me crazy!)"
    uta "Mmm... Ughh... Mmm"
    uta "(It's painful, but it feels so good...)"
    uta "Oh my god! i love it!"
    uta "(Mess up my Ass...)"
    uta "(I love this...)"
    pause 1.0
    uta "(I'm about to lose it...)"
    uta "(My mind is goind to fly away....)"

    jump uta_doggystyle_anal_slow

#doggystyle_anal
label uta_doggystyle_anal_slow:
    window hide
    window auto
    show movie_uta_doggystyle_anal slow

    pause 2.0

    uta "Oh my god!"
    uta "[player.n]... you're being so rough!"
    player "Do you want me to stop?"
    uta "No... NO!"
    uta "(I can't let him get mad, he has to be just mine)"    
    uta "Please... Keep fucking me like that!"
    uta "It feels sooo good!"
    uta "Your cock is such a perfect fit for my ass!"
    uta "Fuck me faster, please!!!"
    uta "I want to be your little slut!"
    player "Are you sure you don't want to be a slut for other men?!"
    uta "Ahhh!?!?"
    uta "Nooo! No! No! No! My sluty ass only... wants... your cock!"
    player "Take it them!!"
    player "Take it like a good little slut!!"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_uta_doggystyle_anal slow
            pause
            jump uta_doggystyle_anal_slow

        "Faster":
            player "Faster!!"
            jump uta_doggystyle_anal_fast
    

label uta_doggystyle_anal_fast:
    window hide
    window auto
    show movie_uta_doggystyle_anal fast

    pause 3.0
    #dia rep
    
    uta "I... love... it!"
    uta "[player.n]... Use me!!!"
    uta "Make me yours!!!"
    uta "Tonight.. you can do whatever you want with me!!"
    uta "I need more!"
    uta "I want to feel you deep inside of me!"
    player "Fuck!!"       
    uta "Oh my god!!!"
    uta "Yes... This is soo strange... I'm close!!!"

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump uta_doggystyle_anal_slow

        "Keep going":
            show movie_uta_doggystyle_anal fast
            pause
            jump uta_doggystyle_anal_fast

        "Cum":
            jump uta_doggystyle_anal_cum


label uta_doggystyle_anal_cum:

    show movie_uta_doggystyle_anal cum

    uta "Are you going to cum too [player.n]?!?"
    uta "Cum for me!!!"    
    
    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    play gems "gem_01"
    show uta_doggystyle_anal_cum at vibration  with flash
    hide movie_uta_doggystyle_anal

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    uta "(I'm cuming!!!)"
    uta "(Cumming! Cumming! Cumming!)"   
    uta "Ahhh Ohhhh..... Ughhh ha ha ha ha"   
    uta "(I can't stop cumming...)"
    uta "My Juice Keeps flowing out more and more..."
    uta "(He made me cum so many times...)" 
    uta "(I'am her woman now...)"      
    uta "(This is the paradise...)"            

    window hide
    window auto

    show screen screen_black with Dissolve(0.8)
    show movie_uta_doggystyle_anal_ass_cum
    hide screen screen_black with Dissolve(0.8)

    pause 2.0

    uta "You sure poured a lot inside me today..."
    uta "How about it? Do you like what you see..."
    uta "It's all yours... You'll have it whenever you want, [player.n]!"     
    uta "I did feel really good..." 
    uta "I don't mind doing it from time to time!" 


    window hide
    window auto
    pause 1.0
    jump uta_doggystyle_anal_end


label uta_doggystyle_anal_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    stop gems
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_uta_doggystyle_anal
    hide uta_doggystyle_anal_cum
    hide movie_uta_doggystyle_anal_ass_cum
    hide screen screen_black with Dissolve(0.6)

    $ music_time_day()

    show uta happy with dissolve
    
    uta "I hope you call me soon [player.n]!" 

    $ uta_lust += 2
    $ uta_love += 2
    narrador "[uta.n] Lust +2 and Love +2" 

    window hide
    show uta c1_underwear with dissolve
    pause 0.2
    show uta c1 with dissolve

    #jump uta_bye

    window hide
    hide uta with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location