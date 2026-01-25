# Version event: 5
# Version game: 0.36

default hancock_titjob = 0


image movie_hancock_titjob slow = MovieFallback(play="movie/hancock/titjob/1.webm", image="movie/hancock/titjob/img.webp", character="hancock")
image movie_hancock_titjob fast = MovieFallback(play="movie/hancock/titjob/2.webm", image="movie/hancock/titjob/img.webp", character="hancock")
image movie_hancock_titjob cum  = MovieFallback(play="movie/hancock/titjob/3.webm", image="movie/hancock/titjob/img.webp", character="hancock")

image hancock_titjob_cum = "movie/hancock/titjob/cum.webp"

label event_hancock_titjob:

    if hancock_titjob == 0:

        player "[hancock.n], things between us have really changed, haven't they?"
        player "We're closer now... there's a different kind of trust between us."
        player "I think it's time we explore that... try something new, just the two of us."
        show hancock c1 shame with dissolve
        hancock "*smirks with a teasing sparkle in her eyes* You're always so bold, [player.n]."
        hancock "Tell me... what exactly do you want to try this time?"
        player "Why don't you take off your clothes and come with me? I'd rather show you than explain."
        hancock "You dare to command an Empress so casually..."
        pause 1.0
        hancock "But... if it's you... I suppose I'll allow it."
        hancock "You always make me feel things I can't explain... it's unfair how easily you disarm me."
        player "That's because every moment with you makes my heart race... and I want to share that with you."
        hancock "Then guide me [player.n]. Tonight... I'm yours to command."


    else:
        player "You somehow grow more beautiful every day, [hancock.n]..."
        player "You really shouldn't hide that kind of beauty from the world..."
        player "Why don't you undress and join me again... like last time?"
        show hancock c1 smile with dissolve
        hancock "That hungry look again... you're insatiable, [player.n]."
        hancock "I'd be a fool to deny myself the chance to feel that again."
        hancock "I loved the way you made me feel."
        player "Then there's no reason to hold back, is there?"
        hancock "None at all... but this time, don't expect me to let you lead everything."


    call hancock_check pass (check_love = 35, check_lust = 35) from _hancock_check_titjob
    show hancock neutral with dissolve
           
    $ hancock_titjob += 1

    pause 1.0
    window hide
    show hancock neutral c1_naked with dissolve

    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    play sound "titjob_1" loop
    show movie_hancock_titjob slow

    hide screen screen_black with Dissolve(0.8)

    hancock "A titjob... from the Pirate Empress herself?"
    hancock "You've been devouring my cleavage with your eyes since the day we met, haven't you, [player.n]?"
    hancock "These breasts have toppled kings and crushed fleets... and now they'll worship your cock."
    player "[hancock.n]... your arrogance makes this even hotter."
    hancock "Hmph. Only for you do I allow such vulgarity."
    hancock "Look—your thick shaft is already pulsing between them..."
    hancock "So hot... so heavy... it's staining my perfect skin with your scent."
    hancock "I'll stroke you slowly at first... savor every throb."
    player "Fuck... your tits are softer than silk and warmer than the sun."
    hancock "Of course they are. Nothing less for the man I've chosen."
    hancock "Feel how they mold around you? Like they were sculpted for this alone."
    hancock "Your precum is dripping down my chest... marking me as yours."
    player "Keep talking like that and I won't last."

    jump event_hancock_titjob_slow

#titjob
label event_hancock_titjob_slow:
    window hide
    window auto
    show movie_hancock_titjob slow

    pause 3.0

    hancock "Do you want to spill your seed all over the Empress's sacred breasts?"
    hancock "Relax... let me milk you with these 'national treasures' you adore so much."
    hancock "Or... shall I quicken my pace, my love?"
    hancock "Tell me how you want your [hancock.n] to serve you."

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_hancock_titjob slow
            pause
            jump event_hancock_titjob_slow

        "Faster":
            hancock "Mmm... I can feel every vein dragging against my skin..."
            hancock "Your cockhead keeps kissing my chin... so greedy."
            jump event_hancock_titjob_fast
    

label event_hancock_titjob_fast:
    window hide
    window auto
    show movie_hancock_titjob fast

    pause 3.0
    
    hancock "Yes—like that! Fuck my tits harder!"
    hancock "They're bouncing so lewdly... all for you!"
    hancock "Your balls are slapping my chest—such a filthy sound!"
    player "[hancock.n]... I'm losing control!"
    hancock "Good. Lose yourself in me."
    hancock "I want to feel your cum painting my neck, my face, my crown..."
    
    pause 2.0

    menu:
        "Slower":
            jump event_hancock_titjob_slow

        "Keep going":
            show movie_hancock_titjob fast
            pause
            jump event_hancock_titjob_fast

        "Cum":
            jump event_hancock_titjob_cum


label event_hancock_titjob_cum:
    show movie_hancock_titjob cum


    hancock "Ah! Your shaft is swelling... you're close, aren't you?"
    hancock "Don't you dare hold back—drown your Empress!"

    player "(Fuuck... I'm reaching my limit...She do it so well!)"
    
    window hide
    window auto

    pause 1.0

    play sound "cum_01"
    show hancock_titjob_cum at vibration with flash
    
    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0


    hancock "Yes! Give it all to me!"
    pause 0.5
    hancock "Good boy, good boy!"
    hancock "So thick... so hot... it's pooling between my breasts!"
    hancock "Look at the mess you've made of the Pirate Empress..."
    hancock "Ropes of cum dripping from my chin... marking me like your personal whore."
    hancock "The scent is intoxicating... I could wear this all day."
    player "[hancock.n]... you're unreal."
    hancock "Hmph. Clean-up is beneath me... but for you, I'll lick every drop."
    pause 0.5
    hancock "Mmm... salty, thick, and all mine."
    hancock "Next time, I'll make you beg before I let you defile me again."

    window hide
    window auto
    pause 1.0
    jump event_hancock_titjob_end


label event_hancock_titjob_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_hancock_titjob
    hide hancock_titjob_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show hancock happy with dissolve
    
    hancock "You know where to find me if you want to repeat!!"
    hancock "It was very very good and funny!!"

    $ hancock_lust += 2
    $ hancock_love += 2
    narrador "[hancock.n] Lust +2 and Love +2" 

    window hide
    show hancock c1_underwear with dissolve
    pause 0.2
    show hancock c1 with dissolve

    jump hancock_bye