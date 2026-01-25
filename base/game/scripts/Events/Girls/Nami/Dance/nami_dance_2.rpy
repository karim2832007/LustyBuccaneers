# Version event: 3
# Version game: 0.29

image movie_nami_dance_2a = MovieFallback(play="movie/nami/dance/2/a1.webm", image="movie/nami/dance/2/a1.webp", character="nami")
image movie_nami_dance_2b = MovieFallback(play="movie/nami/dance/2/b1.webm", image="movie/nami/dance/2/b1.webp", character="nami")


label nami_dance_2:
    $ ui_interface = False
    show nami c2 at center with dissolve

    if yuba_bar_nami == 1:
        player "Here we are again!... [toto.n] told me business is really booming when you're on stage, [nami.n]..."
        player "That old man is desperate for you to get back to dancing!"
        nami "Hahaha, I'm not surprised, Captain. The customers know what's good!"
        player "That's exactly what old [toto.n] says!"
        player "Speaking of which... I think there's still room for improvement..."
        nami "Room for improvement? What do you mean?"
        player "Hahaha... If business is already doing so well with your current dancing..."
        player "What if we add a little... spice?"

        show nami c2 berries with Dissolve(0.2)
        nami "!!!"
        nami "I like the way you think... These horny visitors will definitely tip better if I show a little more of what they want..."
        player "Yeah yeah, that's the idea!"
        show nami c2 neutral with Dissolve(0.2)
        nami "Interesting!"
        nami "I can do that... Leave it to me."
        player "Excellent, I'll be here making sure no one crosses the line."
        nami "Fine, I guess I can count on you for that... I've seen you defeat way worse than this scum..."
        nami "You cover me and I'll squeeze every last [Berries.n] out of these guys"

        $ yuba_bar_nami = 2

    else:
        nami "You want me to dance again, Captain?!?"
        nami "You cover me and I'll squeeze every last [Berries.n] out of these guys"
        nami "Let's get to work!"

    window hide
    show screen screen_black with Dissolve(0.6)
    show movie_nami_dance_2a#events nami dance nami_dance_2a
    hide screen screen_black with Dissolve(0.3)
    window auto

    pause 1.5

    player "([nami.n] is so sexy... She's going to drive the crowd crazy again. It's only a matter of time before she becomes famous!)"
    nami "How are you guys doing!!"
    nami "Hope you're enjoying the view!..."
    unknown "I love coming to see you!! I came today just to see those huge tits!!"
    unknown "We've all missed them around here!!!"
    nami "Calm down you bastards, the show hasn't started yet!"
    unknown "That's exactly what we came for too!!! Hope you're like that in private as well!"
    unknown "Hahaha, her attitude turns me on!"
    unknown "And look at that waist!!!"
    unknown "Why don't you come down here, redhead?! I'll give you everything you want!!!"

    window hide
    show screen screen_black with Dissolve(0.6)
    #show events nami dance nami_dance_2b
    show movie_nami_dance_2b
    hide screen screen_black with Dissolve(0.3)
    window auto

    pause 1.5

    nami "Oh yeah?!?"
    nami "I almost forgot the main course!!"
    player "(Holy shit!!!! All of that is in my crew... They're huge!!)"
    nami "Today I'm bringing you something new!!!"
    nami "Hope you like what you see!"
    player "(We love it, [nami.n], keep going!!!!)"
    nami "You better be generous with your tips if you want to see more of all this!"
    player "(Sometimes I forget how lucky I am to have her in the crew!)"
    unknown "Look at those udders!!!"
    unknown "They have to be mine!!"
    nami "You like it?!? Bunch of misfits!!!"


    $ berries += dance_berries
    narrador "+[dance_berries] Berries"

    $ ui_interface = True
    $ game.clock.next()
    jump ar_y_bar