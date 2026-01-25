# Version event: 5
# Version game: 0.5

label event_perona_hangout:

    show perona c1 with dissolve

    perona "Hello, [player.n]. Do you need anything from me?"
    
    jump event_perona_hangout_menu


label event_perona_hangout_menu:
    menu:
        "Hangout":
            call perona_hangout from _call_perona_hangout

        "Give":
            call perona_give from _call_perona_give_chat
            jump event_perona_hangout_menu

        "Dismiss Her":
            player "That's all, [perona.n]. You can go back to your tasks."

            if perona_love < 10: 
                show perona anger with Dissolve(0.2)
                perona "Nobody gives me orders [player.n]! And especially doesn't waste my time... If you don't have something important to say, don't call me..."

            elif perona_love < 20:
                show perona with dissolve
                perona "If you need me for something else, call me. I'm quite bored!"

            elif perona_love >= 20:
                show perona with dissolve
                perona "What a shame, Captain! I'd like to spend more time with you next time... I hope you call me soon!"

                if perona_lust >= 20:
                    perona "If you need anything else, call me! We could even meet tonight, I've been feeling quite lonely lately..."
                else:
                    perona "If you need anything else, call me!"

    hide perona with moveoutright
    pause 0.5
    return

label perona_hangout:
    $ perona_random_talk = renpy.random.choice(["perona_hangout_1","perona_hangout_2","perona_hangout_3","perona_hangout_4"])

    #$ perona_random_talk = "perona_hangout_4"

    call expression perona_random_talk from _call_perona_random_talk_hangout
    return

label perona_hangout_1:
    
    show perona c1 anger with dissolve     
    perona "I just ran into [nami.n] and she kept giving me orders!"
    perona "No one gives me orders or tells me what to do!!! Is that clear, [player.n]?"
    perona "You have to do something about it!"


    menu:
        "It will be better to try to get out of this mess...":

            player "(It will be better to try to get out of this mess...)"
            player "Stay calm, [perona.n], I'll talk to [nami.n] about it..."
            player "We're all equals here, it must have been a misunderstanding!"

            show perona c1 happy with dissolve

            perona "I hope so, [player.n]... I trust it won't happen again, I believe in your word!"
            player "Don't worry... I'll take care of it!"



            $ perona_love += 1
            narrador "[perona.n] Love +1"

        "I have to put order":

            player "(If I don't establish order, these girls will do whatever they want... And I'm the one in charge here...)"
            player "[perona.n]... [nami.n] has a lot of experience in navigation, she was surely giving you necessary orders for our journey..."
            player "In matters of navigation, she is your superior and can give you orders if needed..."
            perona "No one gives me orders!! It seems it's not clear to you, [player.n]!!"
            perona "This better change! Or I'll make sure it does..."
            player "We'll see about that!... On this ship, you'll do as I say, [perona.n]..."
            perona "We'll see!!"

            $ perona_love -= 1
            narrador "[perona.n] Love -1"

    return

label perona_hangout_2:
    player "[perona.n] how are you?? I saw you several times walking around the ship with a teddy bear. Is it important to you?"
    perona "[player.n], what an observant person you are... His name is Kumashi, my teddy bear..."
    perona "Kumashi used to be the captain of the wild zombies before... Now I just have this bear to keep me company..."
    perona "Before, I always wanted Kumashi to be quiet... He wasn't allowed to speak, or else he wouldn't be cute anymore... And I can't tolerate that..."
    perona "That bear you saw serves this purpose quite well, as long as it remains cute, it will stay with me..."
    player "That's... alright..."
    perona "And what do you think, do you think it's cute too?"


    menu:
        "It's a cute little bear":

            player "Well... It's quite... Cute, I suppose..."
            player "One could say it's nice..."

            show perona c1 happy with dissolve

            perona "Of course it's cute!"
            perona "And unlike Kumashi, this one keeps its mouth shut..."
            perona "I'll get back to my business, see you next time!"


            $ perona_love += 1
            narrador "[perona.n] Love +1"


        "It's a little childish...":

            player "Well... I find it a bit childish, I'm not sure 'cute' would be the right word..."
            show perona c1 anger with dissolve
            perona "You say it's not cute?!?..."
            perona "Seems like you don't have much taste... It's not childish at all..."
            perona "I'll get back to my business, see you next time!"


            $ perona_love -= 1
            narrador "[perona.n] Love -1"

    return

label perona_hangout_3:
    player "[perona.n] I really like your style!"
    player "Always in black, pink, and white, with a distinct personality and elegance, but with playful touches that blend perfectly..."
    player "Plus, you're very attractive and sexy! I bet every pirate who sees you is madly in love with you..."
    show perona c1 shame with dissolve

    perona "You're such a flatterer [player.n]... I didn't think you were this good with words!"
    perona "I really appreciate you saying that!"
    show perona c1 happy with dissolve
    
    perona "I've always been around places like Thriller Bark..."
    perona "I'm really into all the gothic and dark styles!"
    player "It's a style that suits you really well! Maybe you could teach me a thing or two about fashion..."
    perona "Anytime [player.n]... Now, if you'll excuse me, I'll get back to my tasks!"

    $ perona_love += 1
    $ perona_lust += 1
    narrador "[perona.n] Love +1 and lust +1"

    return
    

label perona_hangout_4:
    
    player "[perona.n] How are you?? How about we chat a bit to get to know each other better... why don't you tell me something about yourself..."
    perona "Mnmnm there's not much to say..."
    perona "I spent my time going from here to there, bored, until I arrived at Thriller Bark as a child..."
    perona "And now I'm here, with its crew... I hope to have a lot of fun on this ship..."
    player "You will [perona.n], I assure you!... Tell me more about yourself and I won't bother you anymore..."
    perona "How about we make it more interesting and fun..."
    perona "How tall do you think I am?"

    menu:
        "170 cm":
            player "Mnmnm... You seem quite tall and slender... I'd say 170 cm..."
            show perona c1 happy with dissolve 
            perona "Seriously, you think I'm that tall? That's great! I like you already!"           

            $ perona_love += 2
            narrador "[perona.n] Love +2"

        "160 cm":
            player "Mnmnm... I think I know exactly how tall you are... 160 cm!!"
            perona "You've got a good eye! That's exactly my height!"

            $ perona_love += 1
            narrador "[perona.n] Love +1"

        "140 cm":
            player "Mnmnm... I'd say about 140 cm, heheh!"
            #aca una cara tipica de nenita haciendo puchero a futuro
            show perona c1 anger with dissolve  
            perona "I'm not that short!!!"
            perona "You're just teasing me!"

            $ perona_love -= 1
            narrador "[perona.n] Love -1"

    return