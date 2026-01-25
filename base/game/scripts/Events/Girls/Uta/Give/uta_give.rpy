# Version event: 1
# Version game: 0.28

label uta_give:
    menu:
        "Give her a Chocolate" if chocolate > 0:
            $ chocolate -= 1

            player "How are you, [uta.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            show uta happy with dissolve
            uta "How thoughtful, [player.n]! It's a bit unexpected but I like it, Thank you very much!"

            $ uta_love += 2
            $ uta_lust += 1
            narrador "[uta.n] Love +2 | [uta.n] Lust +1"

        "Give her a Flowers" if flowers > 0:
            $ flowers -= 1
            
            player "How are you, [uta.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            show uta happy with dissolve
            uta "Thanks [player.n]! You have such a good memory, you know I love these. Thank you very much!..."

            $ uta_love += 3

            narrador "[uta.n] Love +3"

        "Give her a Perfume" if perfume > 0:
            $ perfume -= 1
            
            player "How are you, [uta.n]? I have a gift for you, I hope you like it..."
            player "I think they'll bring back memories of your hometown!!"

            show uta happy with dissolve
            uta "How thoughtful, [player.n]! I love it, Thank you very much!"

            $ uta_love += 3
            $ uta_lust += 2
            narrador "[uta.n] Love +3 | [uta.n] Lust +2"

        "Back":
            return 
    
    jump uta_bye