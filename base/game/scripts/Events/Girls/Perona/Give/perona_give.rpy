# Version event: 2
# Version game: 0.27 

label perona_give:
    menu:
        "Give her a Chocolate" if chocolate > 0:
            $ chocolate -= 1

            player "How are you, [perona.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            show perona happy with dissolve
            perona "How thoughtful, [player.n]! It's a bit unexpected but I like it, Thank you very much!"

            $ perona_love += 2
            $ perona_lust += 1
            narrador "[perona.n] Love +2 | [perona.n] Lust +1"

        "Give her a Flowers" if flowers > 0:
            $ flowers -= 1
            
            player "How are you, [perona.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            show perona happy with dissolve
            perona "Thanks [player.n]! You have such a good memory, you know I love these. Thank you very much!..."

            $ perona_love += 3

            narrador "[perona.n] Love +3"

        "Give her a Perfume" if perfume > 0:
            $ perfume -= 1
            
            player "How are you, [perona.n]? I have a gift for you, I hope you like it..."
            player "I think they'll bring back memories of your hometown!!"

            show perona happy with dissolve
            perona "How thoughtful, [player.n]! I love it, Thank you very much!"

            $ perona_love += 3
            $ perona_lust += 2
            narrador "[perona.n] Love +3 | [perona.n] Lust +2"

        "Back":
            return 
    
    jump perona_bye