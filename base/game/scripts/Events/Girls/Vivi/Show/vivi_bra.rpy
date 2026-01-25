# Version event: 2
# Version game: 0.23

default vivi_bra = 0

label event_vivi_bra:
    if vivi_bra == 0:
        player "[vivi.n], how's everything going?"
        player "I usually see that you are always talking about fashion with the girls..."
        player "You have quite an elegant style..."
        player "You dress very well, I like the elegance and presence you carry... It matches perfectly with your style..."
        show vivi c1 neutral with dissolve
        vivi "You flatter me, [player.n]... Being a princess, I wanted to stand out from most of the girls at [Arabasta.n]..."
        player "You may not know it, but I am very interested in arts and fashion."
        vivi "It's quite strange for a pirate, I'm surprised [player.n]..."
        player "Yes it is..."        
        player "I'm a man of many pleasures, [vivi.n]..."
        player "What bra are you wearing... Does it match your princess attire?..." 
        show vivi c1 shame with dissolve
        vivi "Eh?!?... What did you say... Did you just ask me about my bra?..."
        $ vivi_bra += 1
    else:
        player "[vivi.n], you know I really like your style..."
        player "Plus, I feel like we're becoming more comfortable with each other..."
        vivi "It's true, I do feel more and more at ease with you, [player.n]..."
        player "What bra are you wearing today?... Would you show me?"

    menu:
        "You know I have no other intentions":
            call vivi_check pass (check_love = 5, check_lust = 5) from _vivi_bra_check
            player "You know I have no other intentions..."
            player "I hope you don't mind... I really admire your fashion sense."
            player "Also I hope it doesn't make you feel embarrassed, it's simply to admire your beauty..."
            player "You don't have to be embarrassed, you're a beautiful woman!"
            show vivi c1 shame with dissolve
            vivi "R-really, you think so, [player.n]??" 
            player "Absolutely!"
            vivi "You're always so good to me, you flatter me and take care of me so much..."  
            vivi "You always manage to convince me... I'll only do it because of your kind words..." 
            vivi "I feel so comfortable with you, so... so safe... But don't get used to it, [player.n]... "  
            player "Don't worry... it'll stay just between the two of us..."
            vivi "Well, it's not that weird... And I want you to know that I trust you!" 

        "Show me what you're wearing...":
            player "It should look really sexy on you, show me what you've got on..."
            show vivi c1 annoyed with dissolve
            vivi "I think there are better ways to ask for it..."
            vivi "There are times when it really makes me feel uncomfortable."
            vivi "Of course, it looks sexy... But you'll never know!!"
            jump vivi_refuse

    window hide
    show vivi c1_bra with dissolve
    pause 1
    show vivi neutral with Dissolve(0.2)
    window auto

    $ vivi_lust += 2
    narrador "[vivi.n] lust +2"

    show vivi c1 with dissolve

    jump vivi_goodbye
