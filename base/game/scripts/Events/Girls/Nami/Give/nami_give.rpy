# Version event: 1
# Version game: 0.14

label nami_give:
    menu:
        "Give her a Bracelet" if bracelet_nami > 0:
            $ bracelet_nami -= 1

            player "How are you, [nami.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            show nami happy with dissolve
            nami "How thoughtful, Captain! It's a bit unexpected but I like it, and the material it's made of is so fine! Thank you very much!"
            $ nami_love += 2
            $ nami_lust += 1
            narrador "[nami.n] Love +2 | [nami.n] Lust +1"

        "Give her a Tangerine" if tangerine_nami > 0:
            $ tangerine_nami -= 1
            
            player "How are you, [nami.n]? I have a gift for you, I hope you like it..."
            player "I think they'll bring back memories of your hometown!!"

            show nami happy with dissolve
            nami "How thoughtful, Captain! You have such a good memory, you know I love these. Thank you very much!..."
            $ nami_love += 4
            $ nami_lust += 2

            narrador "[nami.n] Love +4 | [nami.n] Lust +2"

        "Give her a totem" if totem_robin > 0:
            $ totem_robin -= 1
            
            player "How are you, [nami.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            #show nami with dissolve
            nami "Hmm, I suppose it's nice... It's a bit unexpected, but I could find a use for it. Thank you!"
            $ nami_love -= 2
            $ nami_lust -= 1

            narrador "[nami.n] Love -2 | [nami.n] Lust -1"

        "Back":
            return 
    
    jump nami_bye