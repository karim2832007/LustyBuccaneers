# Version event: 2
# Version game: 0.28

default uta_bra = 0

label event_uta_bra:
    if uta_bra == 0:
        player "[uta.n], how's everything going? You have quite an elegant style..."
        player "You dress very well, I like the elegance and presence you carry... It matches perfectly with your style..."
        player "I suppose that since you dedicate yourself to music, you have a certain image to maintain..."

        show uta c1 neutral with dissolve
        uta "You flatter me, [player.n]... It's as you say, I always tried to dress according to my mood and the style of music I like..."
        uta "I'd love for my style and music to reach every corner of the seas someday... Be recognized, create a trend..."      
        player "What a great idea, [uta.n]... I'll help you achieve it..."   
        player "Going back to the topic of fashion... It's something I'm really interested in, you know?... Tell me..."
        player "What bra are you wearing... Does it match your idol attire?..."
        show uta c1 shame with dissolve
        uta "Eh?!?... What did you say... Did you just ask me about my bra?..."
        $ uta_bra += 1
    else:
        player "[uta.n], you know I really like your style..."
        player "Plus, I feel like we're becoming more comfortable with each other..."
        uta "It's true, I do feel more and more at ease with you, [player.n]..."
        player "What bra are you wearing today?... Would you show me?"

    menu:
        "You know I have no other intentions":
            call uta_check pass (check_love = 5, check_lust = 5) from _uta_bra_check
            player "You know I have no other intentions, I just admire your beauty..."
            player "I hope you don't mind... I really admire your fashion sense."
            player "Also I hope it doesn't make you feel embarrassed, it's simply to admire your beauty..."
            player "You don't have to be embarrassed, you're a beautiful woman!"
            show uta c1 shame with dissolve
            uta "R-really, you think so, [player.n]??" 
            player "Absolutely!"
            uta "I trust you... But to be honest, it does make me a little shy..."
            player "Nothing to be shy about... You're incredibly attractive, and with such great style, it should feel natural for you..."
            uta "Maybe you're right, [player.n]..."
            uta "So, what do you think?! How does it look on me?"

        "Show me what you're wearing...":
            player "It should look really sexy on you, show me what you've got on..."
            show uta c1 annoyed with dissolve
            uta "I think there are better ways to ask for it..."
            uta "There are times when it really makes me feel uncomfortable."
            uta "Of course, it looks sexy... But you'll never know!!"
            jump uta_refuse

    window hide
    show uta c1_bra with dissolve
    pause 1
    show uta neutral with Dissolve(0.2)
    window auto

    $ uta_lust += 2
    narrador "[uta.n] lust +2"

    show uta c1 with dissolve

    jump uta_goodbye
