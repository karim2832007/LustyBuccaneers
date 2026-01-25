# Version event: 2
# Version game: 0.25

label elegia_h6():

    pause 1.0

    narrador "As you enter the auditorium, a girl catches your attention among the crowd..."
    narrador "On the main stage, a sexy young woman with reddish and white hair was warming up her voice before what you assume would be a performance"

    show uta at center with dissolve    

    player "(Wow!!! That girl... She's an angel, her voice is so angelic... And she's so sexy!!!)"
    player "(That heart-shaped cleavage! Looks like her chest is about to burst out and fly away at any moment...)"
    player "(I can't stop looking at her...)"
    player "(Her sexy figure... And that voice... Could she be a siren instead of an angel?)"

    window hide
    window auto
    pause 1.0

    call set_name_uta from _call_set_name_uta

    nami "I guess you're seeing the same thing I am, captain..."
    nami "Who is she...? I've never heard a voice like that... Close your mouth or you'll start drooling!"
    robin "She must be one of the castle's main singers..."
    robin "She's very young and talented, surely one of the most outstanding!"
    player "(A voice like that... And a body like that... That should be illegal!)"

    narrador "Suddenly, a male voice interrupts the moment."
    unknown "That voice is worth a fortune, and it's really precious! Come with me, young lady... You'll make me rich!"

    show uta:
        xalign 0.5
        yalign 1.0
        linear 1.0 xalign 0.2

    pause 0.9

    show eboshi with dissolve:
        xalign 0.9
        yalign 1.0

    uta "Who are you? I don't know you..."
    uta "I'm not going anywhere with you... This is the main castle of Elegia, don't you know where you are?!?"

    unknown "With a gem like you, the nobles will pay anything for a private concert... Or maybe some other... services..."

    player "(Bastard!!! What is he implying...)"
    player "(I saw her first!!!)"
    player "(I found this angel first... And now this idiot wants to take her away!)"

    uta "What are you implying!?!... Get out of here or I'll call the king immediately!"
    unknown "Too late, sweetheart..."    
    player "Bastard leave her alone!"

    narrador "As you try to approach, the man pulls something out of his pocket"

    unknown "See you, losers!"

    show layer_smoke zorder 5 with Dissolve(0.6)
    narrador "BOOM!"

    hide uta
    hide eboshi

    narrador "You try to run toward the stage, but the smoke is too thick. Coughing, you can barely see a few meters ahead until the smoke clears..."

    window hide
    hide layer_smoke with Dissolve(1.4)
    window auto

    pause 0.5

    show nami serious at center with dissolve

    nami "Where's the girl?!"

    show nami:
        xalign 0.5
        yalign 1.0
        linear 1.0 xalign 0.15

    show yamato with dissolve:
        xalign 0.85
        yalign 1.0

    yamato "She's gone... just like that guy."
    yamato "That bastard escaped, just when things were about to get good..."
    player "Damn it, we have to find her!"
    yamato "There's no trace of her around here... So we'll have to get information elsewhere..."

    show nami:
        xalign 0.15
        yalign 1.0
        linear 1.0 xalign 0.15

    show yamato:
        xalign 0.85
        yalign 1.0
        linear 1.0 xalign 0.85

    show robin at center with Dissolve(0.5)

    robin "With such an exceptional voice... She must be known around here..."

    robin "An artist of that level... Someone must have authorized her presence on the stage"

    player "What do you mean?"

    robin "Elegia isn't just any city. Here, the king regulates everything related to music."

    robin "If that girl truly belongs to the castle... The king himself must know who she is."

    player "Alright, since we're in the castle, all that's left is to find this so-called king"


    
    pause 1.0


    $ Elegia.h = 7
    jump el_castle_auditorium
