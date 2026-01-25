# Version event: 4
# Version game: 0.29

default yuba_bar_nami = 0

label nami_dance_1:
    $ ui_interface = False
    show nami c2 at center with dissolve

    if yuba_bar == 1:
        player "So here we are, [nami.n], what do you think of this bar?"
        nami "So you finally got yourself a place to dance!!"
        nami "This is [toto.n]'s bar, right?... So this is what you two were plotting all along..."
        nami "That perverted old man... Now I see what he's up to with that stage and this bar..."
        nami "Poor [vivi.n]... She has no idea how perverted [toto.n] really is..."
        player "Hahaha that's right! We'll slowly make his dream come true..."
        player "(And I'll benefit from it!!)"
        player "You still haven't answered me... You didn't tell me what you think in the end!"
        nami "It's not bad actually... Quite a bit of activity for a newly opened place..."
        show nami c2 berries with Dissolve(0.2)
        nami "We could do great things here..."
        player "Yeah Yeah, that's the idea!"
        show nami c2 serious with Dissolve(0.2)
        nami "But we have to stay alert... A few of these guys don't look very trustworthy..."
        nami "And they're pretty drunk..."
        player "Hhaha they're desert bandits! What did you expect?!!"
        player "Don't worry, nothing will happen with me here..."
        show nami c2 neutral with Dissolve(0.2)
        nami "Fine, I guess I can count on you for that... I've seen you defeat way worse than this scum..."
        nami "You cover me and I'll squeeze every last [Berries.n] out of these guys"
        player "Hhaha that's the spirit, I'm counting on you!..."

        $ yuba_bar = 2

    else:
        nami "You want me to dance again, Captain?!?"
        nami "You cover me and I'll squeeze every last [Berries.n] out of these guys"
        nami "Let's get to work!"

    if yuba_bar_nami == 0:
        $ yuba_bar_nami = 1

    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "ar_y_dance"
    scene BG locations:
        blur 3
    
    show events nami dance nami_dance_1

    hide screen screen_black with Dissolve(0.3)
    window auto

    player "([nami.n] is so sexy... She's going to drive the crowd crazy, it's only a matter of time before she becomes famous!)"
    player "(This is a gold mine ready to be tapped!)"
    player "(And maybe I could even get some extra benefits!)"
    nami "How are you guys doing!!"
    nami "Hope you're enjoying the view!..."
    nami "And be generous with your tips... Whoever pays the most gets a special prize!"
    unknown "Holy Shit! Just look at those massive tits!"          
    unknown "Hey get to it shake your ass and those jugs too while you're at it!"  
    nami "Calm down you bastards, the show hasn't started yet!"
    unknown "Hahaha her attitude turns me on!"
    player "(Hahah [nami.n] still has things to learn, her temper could be a problem...)"
    player "(But she's way too sexy, there won't be any trouble!)"
    player "(Maybe I could convince her to do a slightly spicier dance...)" 

    $ berries += dance_berries
    narrador "+[dance_berries] Berries"

    $ ui_interface = True
    $ game.clock.next()
    jump ar_y_bar