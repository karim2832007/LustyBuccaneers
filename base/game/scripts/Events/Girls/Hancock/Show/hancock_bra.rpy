# Version event: 2
# Version game: 0.12

default hancock_bra = 0

label event_hancock_bra:
    if hancock_bra == 0:
        player "[hancock.n], how's everything going?... You have quite an elegant style..."
        player "You dress very well, I like the elegance and presence you carry... It matches perfectly with your style..."
        show hancock c1 serious with dissolve
        hancock "You flatter me, [player.n]... Being the empress, I wanted to stand out from most of the girls at Amazon Lily, who have a more `wild´ way of dressing..."
        player "I'm a man of many pleasures, [hancock.n]..."
        player "What bra are you wearing... Does it match your empress attire?..." 
        show hancock c1 neutral with dissolve
        hancock "Eh?!?... What did you say... Did you just ask me about my bra?..."
        $ hancock_bra += 1
    else:
        player "[hancock.n], you know I really like your style..."
        player "Plus, I feel like we're becoming more comfortable with each other..."
        hancock "It's true, I do feel more and more at ease with you, [player.n]..."
        player "What bra are you wearing today?... Would you show me?"

    menu:
        "You know I have no other intentions":
            call hancock_check pass (check_love = 5, check_lust = 5) from _hancock_bra_check
            player "You know I have no other intentions..."
            player "I hope you don't mind... I really admire your fashion sense."
            player "Also I hope it doesn't make you feel embarrassed, it's simply to admire your beauty..."
            player "You don't have to be embarrassed, you're a beautiful woman!"
            show hancock c1 shame with dissolve
            hancock "R-really, you think so, [player.n]??" 
            player "Absolutely!"
            show hancock c1 neutral with dissolve 
            hancock "You always manage to convince me... I'll only do it because of your kind words..." 
            hancock "Don't get used to it, [player.n]... I feel a bit childish doing this..."  
            player "Don't worry... it'll stay just between the two of us..."

        "Show me what you're wearing...":
            player "It should look really sexy on you, show me what you've got on..."
            show hancock c1 annoyed with dissolve
            hancock "Are you giving me an order, [player.n]?"
            hancock "Of course, it looks sexy... But you'll never know!!"
            jump hancock_refuse

    window hide
    show hancock c1_bra with dissolve
    pause 1
    show hancock neutral with Dissolve(0.2)
    window auto

    $ hancock_lust += 1
    narrador "[hancock.n] lust +1"

    show hancock c1 with dissolve

    jump hancock_goodbye
