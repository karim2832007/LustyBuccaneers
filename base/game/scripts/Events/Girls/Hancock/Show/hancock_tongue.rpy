# Version event: 2
# Version game: 0.12

default hancock_tongue = 0

label event_hancock_tongue:
    if hancock_tongue == 0:
        player "How are you, [hancock.n]?? ... I imagine that when you were little with your sisters, you surely had happy moments teasing each other..." 
        show hancock c1 serious with dissolve
        hancock "Yes, aside from the sad times we lived through... we used to try to support each other to keep moving forward constantly..." 
        hancock "They were small good moments, oasis in a sea of tears... We used to play games to disconnect from the bad situation, braid each other's hair, play house, make funny faces..."
        player "Hahaha, funny faces? What was that like?..." 
        show hancock c1 neutral with dissolve
        hancock "Ehhh?!?... We were little girls, it would be pretty strange if I did it now..."
        $ hancock_tongue += 1
    else:
        player "How are you, [hancock.n]?? ... Maybe you could... Make a funny face for me once again, for old times' sake..."
        hancock "You always manage to convince me..." 
        player "You're really cute when you do it... What do you say?"

    menu:
        "It would be nice to remember and relax together":
            call hancock_check pass (check_love = 3, check_lust = 3) from _hancock_tongue_check
            player "It would be nice to remember and relax together, [hancock.n], hahahaa!" 
            player "You don't have to be embarrassed, you're a beautiful woman!"
            show hancock c1 shame with dissolve
            hancock "R-really, you think so, [player.n]??" 
            player "Absolutely!"
            show hancock c1 neutral with dissolve 
            hancock "You always manage to convince me... I'll only do it because of your kind words..." 
            hancock "Don't get used to it, [player.n]... I feel a bit childish doing this..."  
            player "Don't worry... it'll stay just between the two of us..."

        "It's an order, you should do it for your captain...":
            player "You should do it for me… I am your captain, it's an order!"
            show hancock c1 annoyed with dissolve
            hancock "No one gives me orders or tells me what to do!!! Do you understand, [player.n]?"
            hancock "You'll have to improve your manners if you want to get along with me..."
            jump hancock_refuse


    window hide
    show hancock c1 tongue with dissolve
    pause 2
    show hancock neutral with Dissolve(0.2)
    window auto
    
    $ hancock_lust += 1
    narrador "[hancock.n] lust +1"

    show hancock c1 with dissolve

    jump hancock_goodbye