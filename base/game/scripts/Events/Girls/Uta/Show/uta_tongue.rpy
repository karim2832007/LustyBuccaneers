# Version event: 2 
# Version game: 0.28

default uta_tongue = 0

label event_uta_tongue:
    if uta_tongue == 0:
        player "How are you, [uta.n]??... I remember you told me you spent your whole childhood in Elegia..."

        uta "Yes, not only was I cared for by the king of the island... There were also all the boys and girls who came to the island to learn music."

        uta "It was a good time... Even though I would have preferred to have my father close, I can't complain... I had very happy moments in Elegia."

        uta "They were small good moments... We used to play games to disconnect from the bad situation, braid each other's hair, play house, we sang and practiced music together, made funny faces..."

        player "Hahaha, funny faces? What was that like?..."

        uta "Ehhh?!?... We were little girls, it would be pretty strange if I did it now..."
        $ uta_tongue += 1

    else:
        player "How are you, [uta.n]?? ... Maybe you could... Make a funny face for me once again, for old times' sake..."
        uta "Again with this strange request, [player.n]..."
        player "You're really cute when you do it... What do you say?"

    menu:
        "It would be nice to remember and relax together":
            call uta_check pass (check_love = 3, check_lust = 3) from _uta_tongue_check
            player "It would be nice to remember and relax together, [uta.n], hahahaa!" 
            player "You don't have to be embarrassed, you're a beautiful woman!"
            show uta c1 shame with dissolve
            uta "R-really, you think so, [player.n]??" 
            player "Absolutely!"
            show uta c1 neutral with dissolve 
            uta "You are the first person to treat me like this.... I'll only do it because of your kind words..." 
            uta "Don't get used to it, [player.n]... I feel a bit childish doing this..."  
            player "Don't worry... it'll stay just between the two of us..."

        "It's an order, you should do it for your captain":
            player "You should do it for me... I am your captain, it's an order!"
            show uta c1 annoyed with dissolve            
            uta "That's not a good way to ask!"
            uta "You'll have to improve your manners if you want to get along with me..."
            uta "I better go before I actually get mad..."
            jump uta_refuse


    window hide
    show uta c1 tongue with dissolve
    pause 2
    show uta neutral with Dissolve(0.2)
    window auto
    
    $ uta_lust += 2
    narrador "[uta.n] lust +2"

    show uta c1 with dissolve

    jump uta_goodbye