# Version event: 9
# Version game: 0.40

default hancock_missionary = 0

image movie_hancock_missionary slow = MovieFallback(play="movie/hancock/missionary/vaginal/1.webm", image="movie/hancock/missionary/vaginal/img.webp", character="hancock")
image movie_hancock_missionary fast = MovieFallback(play="movie/hancock/missionary/vaginal/2.webm", image="movie/hancock/missionary/vaginal/img.webp", character="hancock")
image movie_hancock_missionary cum  = MovieFallback(play="movie/hancock/missionary/vaginal/3.webm", image="movie/hancock/missionary/vaginal/img.webp", character="hancock")

image hancock_missionary_cum_in = "movie/hancock/missionary/vaginal/cum_in.webp"
image hancock_missionary_cum_out = "movie/hancock/missionary/vaginal/cum_out.webp"

label event_hancock_missionary_vaginal:

    if hancock_missionary == 0:


        player "[hancock.n]... there's something about the way you've been looking at me..."
        player "It's like you're holding something back..."
        show hancock shame with dissolve
        hancock "Maybe I am..."
        hancock "I never imagined I'd find myself in a moment like this—with someone who sees me, not just my title or beauty."
        player "You're not just a symbol, or a name. You're a woman I care about deeply."
        player "And right now, I want to share something real with you."
        hancock "You really know how to say the right things, don't you?"
        hancock "Careful... keep talking like that and I might start expecting kisses after every compliment."
        player "I could get used to that. You know I never hold back when it's you."
        show hancock happy with dissolve        
        hancock "Dangerous words... I might take you seriously."
        player "(She's playful, but her eyes are sincere. There's nervousness... and trust.)"
        player "No pretending. No masks. Just us."
        hancock "You always say things like that... like you're peeling away everything I hide behind."
        hancock "And somehow... I like it."
        player "Let me take care of you tonight. No pressure. Just what you want, when you want it."
        show hancock shame with dissolve
        hancock "And what if what I want is... you?"
        player "Then I'm right here."
        hancock "You make it so hard to stay composed..."
        player "I'm not trying to steal your composure. Just your breath."
        show hancock neutral with dissolve  
        hancock "Then come closer and earn it."
        player "May I?"
        hancock "Yes... I want to feel you close."
        hancock "Mmm... that's better. You're warm... steady... like a storm I actually want to be swept into."
        player "And you're everything I didn't know I needed."
        hancock "You're going to make me fall even harder if you keep talking like that..."
        player "Then let me fall with you. Together."
        hancock "I'm done pretending I don't want this."
        hancock "So, how about you stop asking for permission..."
        player "Oh?!?"
        hancock "And start showing me what you really came here for..."
        player "Is that a royal command?"
        hancock "He... Call it... an invitation."
        player "Then I won't make you wait any longer."
        hancock "Good. I hate waiting."

    

    else:
        hancock "[player.n]!! I've been waiting for you..."
        hancock "Start showing me what you really came here for..."
        hancock "Make me yours!!!"

    window hide
    call hancock_check pass (check_love = 25, check_lust = 25) from _hancock_check_missionary
    show hancock neutral with Dissolve(0.4)
           
    $ hancock_missionary += 1

    pause 0.5
    show hancock neutral c1_underwear with dissolve
    pause 0.5
    show hancock neutral c1_naked with dissolve
    window auto

    hancock "Tell me what you desire... right now."
    hancock "Don't leave your Empress waiting in this state!"
    player "So many things are running through my mind right now... You're so beautiful."
    hancock "My body burns for you... make me completely yours!"
    player "Then come to bed, [hancock.n]. Tonight I'll claim every inch of the world's most beautiful woman."

    window hide
    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "footjob_1" loop
    play gems ["<silence 0.8>","gem_02","<silence 0.8>"] loop
    #play sound "titjob_1" loop
    show movie_hancock_missionary slow
    
    window auto
    hide screen screen_black with Dissolve(0.8)

    pause 2
    
    hancock "Nnh... ahh... I'm already soaking the sheets..."
    hancock "Look at me... the proud Pirate Empress reduced to this trembling mess... all because of you, [player.n]."
    hancock "We can never go back to being 'just allies' after tonight, do you understand?"
    player "I never wanted to. You've been mine since the moment you fell for me, [hancock.n]."
    hancock "Hmph... arrogant man... but you're right."
    hancock "(It hurts... yet it feels like heaven... my mind is melting...)"
    hancock "(So this is what it means to surrender everything to the one you love...)"
    hancock "(My pride, my body, my heart... all yours...)"
    hancock "Ahn! So deep... [player.n]!"
    hancock "You're splitting me apart... and I love it!"
    player "Should I slow down?"
    hancock "{size=40}Never!{/size} Don't you dare show mercy!"
    hancock "Ruin me... break the Empress with that magnificent cock!"

    jump event_hancock_missionary_vaginal_slow

label event_hancock_missionary_vaginal_slow:
    window hide
    window auto
    show movie_hancock_missionary slow

    pause 1.0

    hancock "Your shape... it's perfect... molded for my pussy alone!"
    hancock "Every thrust scrapes that spot... I can't... I can't think straight!"
    hancock "My walls keep clinging to you... they never want to let go!"
    pause 0.5
    hancock "Look at me while you fuck me—watch the most beautiful woman in the world fall apart beneath you!"
    hancock "Harder [player.n]... deeper... I order you—yes, I'm begging you!"
    hancock "Mark me inside... brand your name into my womb!"
    pause 0.5
    hancock "I want to feel you for days... so I never forget who I belong to!"
    hancock "{size=40}Faster, my love... please... make me scream your name!{/size}"

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_hancock_missionary slow
            pause
            jump event_hancock_missionary_vaginal_slow

        "Faster":
            jump event_hancock_missionary_vaginal_fast
    

label event_hancock_missionary_vaginal_fast:
    window hide
    window auto
    show movie_hancock_missionary fast

    pause 1.0

    hancock "Yes—yes—YES!! Pound me!!"
    hancock "{size=40}Use your Empress like your personal slut!!{/size}"
    hancock "I'm nothing but yours right now—take everything!"
    hancock "My breasts are bouncing so shamefully... touch them—squeeze them!"
    hancock "I'm close again [player.n]... my whole body is on fire!"
    hancock "Don't stop—don't you dare stop until we both shatter!"
    player "[hancock.n]... I'm at my limit!"
    hancock "Then give it to me—flood me—paint my insides white!"
    hancock "{size=40}Cum with me, my beloved—let's fall together!!{/size}"

    $ _window_hide()
    pause 1.0

    menu:
        "Slower":
            jump event_hancock_missionary_vaginal_slow

        "Keep going":
            show movie_hancock_missionary fast
            pause
            jump event_hancock_missionary_vaginal_fast

        "Cum":
            jump event_hancock_missionary_vaginal_cum


label event_hancock_missionary_vaginal_cum:

    menu:
        "Cum inside":
            jump event_hancock_missionary_vaginal_cum_inside

        "Cum outside":
            jump event_hancock_missionary_vaginal_cum_outside


label event_hancock_missionary_vaginal_cum_inside:

    show movie_hancock_missionary cum
    pause 1.0

    play sound "cum_01"
    play gems "gem_01"
    player "Fuuuuck... Take it all!!!"
    $ _window_hide()

    show hancock_missionary_cum_in at vibration  with flash
    hide movie_hancock_missionary

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    #stop gems
    with flash
    pause 0.2
    with flash
    pause 2.0

    hancock "I feel it... so hot... pulsing deep inside...!"
    hancock "You're filling your Empress to the brim... ahhn... it's overflowing..."
    hancock "My womb is yours now [player.n].... completely claimed..."
    hancock "My legs won't close... I'm still trembling... still cumming..."
    hancock "So warm... I'll carry your seed proudly..."
    hancock "This is love... this overwhelming heat inside me... is love."

    window hide
    pause 0.5 
    window auto
    pause 1.0
    jump event_hancock_missionary_vaginal_end


label event_hancock_missionary_vaginal_cum_outside:

    show movie_hancock_missionary cum

    play sound "cum_01"
    play gems "gem_01"
    player "Fuuuuck... Take it all!!!"
    $ _window_hide()

    show hancock_missionary_cum_out at vibration  with flash
    hide movie_hancock_missionary

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    #stop gems
    with flash
    pause 0.2
    with flash
    pause 2.0

    hancock "Ahhh... it's raining on me... so thick... so much..."
    hancock "My breasts... my stomach... my face... you've marked every inch of your Empress..."
    hancock "Look how filthy I am... covered in the man I love... covered of you [player.n]..."
    hancock "I'll wear your cum like the finest jewelry..."
    hancock "The scent... I'll never wash it off..."
    
    window hide
    pause 0.5 
    window auto
    pause 1.0
    jump event_hancock_missionary_vaginal_end


label event_hancock_missionary_vaginal_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    stop gems
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_hancock_missionary
    hide hancock_missionary_cum_in
    hide hancock_missionary_cum_out
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show hancock happy with dissolve
    

    player "[hancock.n]... that was beyond anything I ever dreamed."
    hancock "Hmph... naturally. Only I could give you such perfection."
    hancock "...But you... you were magnificent, my love."
    hancock "I, [hancock.n], belong only to you... body and soul."
    hancock "Never forget that."
    player "How could I?"
    show hancock happy with dissolve
    hancock "Good. Now hold me... your Empress commands it."


    $ hancock_lust += 2
    $ hancock_love += 2
    narrador "[hancock.n] Lust +2 and Love +2" 

    window hide
    show hancock c1_underwear with dissolve
    pause 0.2
    show hancock c1 with dissolve

    window hide
    hide hancock with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location