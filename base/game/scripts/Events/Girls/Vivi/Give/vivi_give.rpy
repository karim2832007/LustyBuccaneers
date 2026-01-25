# Version event: 2
# Version game: 0.27

label vivi_give:
    menu:
        "Give her a Chocolate" if chocolate > 0:
            $ chocolate -= 1

            player "How are you, [vivi.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            show vivi happy with dissolve
            vivi "How thoughtful, [player.n]! It's a bit unexpected but I like it, Thank you very much!"

            $ vivi_love += 2
            $ vivi_lust += 1
            narrador "[vivi.n] Love +2 | [vivi.n] Lust +1"

        "Give her a Flowers" if flowers > 0:
            $ flowers -= 1
            
            player "How are you, [vivi.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            show vivi happy with dissolve
            vivi "Thanks [player.n]! You have such a good memory, you know I love these. Thank you very much!..."

            $ vivi_love += 3

            narrador "[vivi.n] Love +3"

        "Give her a Perfume" if perfume > 0:
            $ perfume -= 1
            
            player "How are you, [vivi.n]? I have a gift for you, I hope you like it..."
            player "I think they'll bring back memories of your hometown!!"

            show vivi happy with dissolve
            vivi "How thoughtful, [player.n]! I love it, Thank you very much!"

            $ vivi_love += 3
            $ vivi_lust += 2
            narrador "[vivi.n] Love +3 | [vivi.n] Lust +2"

        "Back":
            return 
    
    jump vivi_bye