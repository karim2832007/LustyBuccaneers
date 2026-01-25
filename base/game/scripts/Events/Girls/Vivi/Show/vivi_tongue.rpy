# Version event: 2
# Version game: 0.23

default vivi_tongue = 0

label event_vivi_tongue:
    if vivi_tongue == 0:
        player "How are you, [vivi.n]??... I remember you telling me that you were very good friends with [koza.n] during your childhood" 
        player "You surely had happy moments teasing each other..."         
        show vivi c1 happy with dissolve
        vivi "Yes, aside from the sad times we lived through... We used to try to support each other to keep moving forward constantly..." 
        vivi "We had a great time as young people, we even formed a group of boys with whom we had fun every day, the Suna Suna Clan"         
        player "Hahah, I imagine you must have had some great times, you must have been up to all kinds of mischief."
        vivi "Yes, it really was a good time..."          
        player "It may sound strange, but how about you make a funny face at me, so we can laugh together like back then?" 
        show vivi c1 neutral with dissolve
        vivi "Ehhh?!?... We were little kids, it would be pretty weird if I did it now..."
        $ vivi_tongue += 1
    else:
        player "How are you, [vivi.n]?? ... Maybe you could... Make a funny face for me once again, for old times' sake..."
        vivi "You always manage to convince me..." 
        player "You're really cute when you do it... What do you say?"

    menu:
        "It would be nice to remember and relax together":
            call vivi_check pass (check_love = 3, check_lust = 3) from _vivi_tongue_check
            player "It would be nice to remember and relax together, [vivi.n], hahahaa!" 
            player "You don't have to be embarrassed, you're a beautiful woman!"
            show vivi c1 shame with dissolve
            vivi "R-really, you think so, [player.n]??" 
            player "Absolutely!"
            show vivi c1 neutral with dissolve 
            vivi "You are the first person to treat me like this.... I'll only do it because of your kind words..." 
            vivi "Don't get used to it, [player.n]... I feel a bit childish doing this..."  
            player "Don't worry... it'll stay just between the two of us..."

        "It's an order, you should do it for your captain":
            player "You should do it for me... I am your captain, it's an order!"
            show vivi c1 annoyed with dissolve
            vivi "Well... That's a very bad way to ask me..."
            vivi "You'll have to improve your manners if you want to get along with me..."
            jump vivi_refuse


    window hide
    show vivi c1 tongue with dissolve
    pause 2
    show vivi neutral with Dissolve(0.2)
    window auto
    
    $ vivi_lust += 2
    narrador "[vivi.n] lust +2"

    show vivi c1 with dissolve

    jump vivi_goodbye