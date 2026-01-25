# Version event: 3
# Version game: 0.36

default hancock_doggystyle = 0

image movie_hancock_doggystyle_ass = MovieFallback(play="movie/hancock/doggystyle/ass.webm", image="movie/hancock/doggystyle/ass.webp", character="hancock")

image movie_hancock_doggystyle slow = MovieFallback(play="movie/hancock/doggystyle/1.webm", image="movie/hancock/doggystyle/img.webp", character="hancock")
image movie_hancock_doggystyle fast = MovieFallback(play="movie/hancock/doggystyle/2.webm", image="movie/hancock/doggystyle/img.webp", character="hancock")
image movie_hancock_doggystyle cum  = MovieFallback(play="movie/hancock/doggystyle/3.webm", image="movie/hancock/doggystyle/img.webp", character="hancock")

image hancock_doggystyle_cum = "movie/hancock/doggystyle/cum.webp"

label event_hancock_doggystyle:
    if hancock_doggystyle == 0:

        player "[hancock.n], lately we're getting along better and better..."
        player "I feel like our relationship isn't the same as it was at the beginning. We've grown so much closer."
        show hancock c1 shame with dissolve
        hancock "Always saying such flattering things about me, [player.n]... You're making me blush."
        hancock "*giggles softly* You really know how to make a woman feel special."
        player "It's true. Every day you become even more attractive and sexy, [hancock.n]."
        player "You know, you shouldn't hide so much beauty from the world..."
        hancock "Oh?!? Perhaps I only want one special man to see it."
        player "You're truly the most beautiful woman in the world to me."
        show hancock c1 happy with dissolve
        hancock "He... Well, of course I am... "
        hancock "But hearing you say that makes me happier than you could imagine."
        hancock "Mm, [player.n]... what is it that you want to do now?"
        player "Why don't you take off your clothes and come to bed with me?"
        player "I want to feel your body close against mine..."
        show hancock c1 shame with dissolve        
        hancock "Y-you... You certainly don't waste time, do you?"
        hancock "Ordering the Pirate Empress to disrobe... You truly are fearless, [player.n]."
        hancock "If it were anyone else, I'd turn them to stone for such insolence."
        hancock "But for you..."

    else:
        player "Every day you're more attractive and sexy, [hancock.n]..."
        player "You know you shouldn't hide so much beauty from the world..."
        player "Why don't you take off your clothes and come with me to the bed again?..."
        player "I want to feel your body close against mine once more..."


    call hancock_check pass (check_love = 25, check_lust = 25) from _hancock_check_doggystyle

    $ hancock_doggystyle += 1

    hancock "...I'll gladly make an exception."
    hancock "I've been longing for this as well."
    hancock "So yes... I'll do as you ask."
    pause 0.5
    hancock "Now, shall we move to the bed?"
    player "I promise I'll make you feel as wonderful as you are."
    hancock "Come here, my love... I'm all yours tonight." 

    window hide
    show hancock c1_underwear with dissolve
    pause 0.4
    show hancock neutral c1_naked with dissolve


    player "Ufff... such exquisite views... Your body is a work of art."

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show movie_hancock_doggystyle_ass
    hide screen screen_black with Dissolve(0.8)

    pause 4.0

    player "(Wow... This is truly a royal pussy...)"
    pause 1.0   
    hancock "Do you see this? This perfect, yearning pussy?"
    hancock "It's aflame with desire... All because of you, my beloved!"
    hancock "It's yours alone, for I, [hancock.n], have chosen you."
    hancock "It craves your touch, your possession."
    hancock "Come, claim me now... I, the Pirate Empress, beg you not to delay!"
    player "I won't keep you waiting any longer..."
    hancock "Yes, show me your strength [player.n]... Prove you're worthy of my love."
    player "I'll give you everything you desire."

    show screen screen_black with Dissolve(0.8)
    play sound "footjob_1" loop
    hide movie_hancock_doggystyle_ass
    show movie_hancock_doggystyle slow

    hide screen screen_black with Dissolve(0.8)

    hancock "Ohh yess... Deeper, my love!"
    pause 1.0
    hancock "Ahh... Yes, just like that [player.n]... I feel you so deep."
    pause 0.5
    hancock "That's it... Feel how I tremble for you."
    hancock "Your power... It's intoxicating!"
    hancock "No one else could satisfy me like this."
    hancock "You're the only one who sees me this vulnerable."
    pause 1.0

    jump hancock_doggystyle_slow

#doggystyle
label hancock_doggystyle_slow:
    window hide
    window auto
    show movie_hancock_doggystyle slow

    pause 3.0

    hancock "Mnnmnm... I adore your cock!!"
    hancock "It's fit for an empress like me!!"
    player "Fuuuuck... You're so tight and wet, I can barely hold back!"
    hancock "Yes!!! Yes!!! Give me more!"
    pause 1.0
    hancock "Ohh yess... I need it buried deep inside!"
    hancock "Your cock! Your essence! All of you!"
    hancock "I want every part of you within me [player.n]!"
    hancock "Don't hold back... Ravish me as only you can!"
    player "You're driving me wild..."
    hancock "Good... Let my beauty overwhelm you."
    hancock "Thrust harder... Make me yours completely!"
    player "As you command, my Empress..."


    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            show movie_hancock_doggystyle slow
            pause
            jump hancock_doggystyle_slow

        "Faster":
            hancock "Go faster!!"
            jump hancock_doggystyle_fast
    

label hancock_doggystyle_fast:
    window hide
    window auto
    show movie_hancock_doggystyle fast

    pause 3.0
    
    hancock "Faster [player.n]... I'm so close, my love!"
    pause 1.0
    hancock "Ahh! Yes! Right there... Don't stop!"
    player "I can feel you tightening... You're going to make me explode!"
    hancock "Do it! Fill me... I want all of you inside!"
    hancock "I'm... I'm coming!!"
    hancock "My body... it's yours... take it all!!"
    player "Hnnngh... Here it comes!"
    hancock "Yes! Yes! Give it to me!!"

    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump hancock_doggystyle_slow

        "Keep going":
            show movie_hancock_doggystyle fast
            pause
            jump hancock_doggystyle_fast

        "Cum":
            jump hancock_doggystyle_cum


label hancock_doggystyle_cum:

    show movie_hancock_doggystyle cum

    hancock "I feel it... so hot... so much...!"
    window hide
    window auto

    pause 2.0

    play sound "cum_01"
    show hancock_doggystyle_cum at vibration  with flash
    hide movie_hancock_doggystyle

    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    hancock "Ooohh... Magnificent..."
    hancock "My legs... they won't stop shaking..."
    hancock "You've ruined me for anyone else..."
    player "And I'd do it again in a heartbeat."
    hancock "Hmph... Of course you would. Only you are allowed to see me like this."
    hancock "Well done, my love!... To think I, [hancock.n], would surrender so completely..."
    hancock "But for you... I'd do it a thousand times more."

    window hide
    window auto
    pause 1.0
    jump hancock_doggystyle_end


label hancock_doggystyle_end:
    show screen screen_black with Dissolve(0.6)
    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ ui_interface = True
    hide movie_hancock_doggystyle
    hide hancock_doggystyle_cum
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    show hancock happy with dissolve
    
    hancock "Haa... My heart still races for you alone."
    hancock "Remember this moment, my love... No one else will ever have me like this."
    player "How could I forget? You're etched into my soul."
    hancock "Good. Now hold me... Let the Empress rest in your arms."
    hancock "Until next time... don't make me wait too long."

    $ hancock_lust += 2
    $ hancock_love += 2
    narrador "[hancock.n] Lust +2 and Love +2" 

    window hide
    show hancock c1_underwear with dissolve
    pause 0.2
    show hancock c1 with dissolve

    #jump hancock_bye

    window hide
    hide hancock with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location