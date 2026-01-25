# Version event: 3
# Version game: 0.23

label vivi_hangout_2:
    player "You seem to be in a great mood today, [vivi.n]!"
    vivi "Do you really think so? Are you implying that I usually am not?"
    player "No, no, I didn't mean that! Don't misunderstand me!"
    show vivi c1 happy with Dissolve(0.2)
    vivi "Hahaha! Just kidding, [player.n]!"
    vivi "I've always tried to keep a smile, even in difficult moments."
    vivi "That doesn't mean I'm feeling bad now... Quite the opposite, but it became a habit to be like this."
    show vivi c1 serious with Dissolve(0.2)
    vivi "When I infiltrated Baroque Works, I had to pretend to be someone I wasn't for years..."
    vivi "That taught me that sometimes you have to put on a facade to protect what truly matters."
    vivi "I hope to change that little by little... To express how I feel at all times, to never be forced to pretend again…"


    menu:
        "You are really good at acting, you could fool anyone":
            player "I must admit that your acting was impeccable."
            player "If I didn't know the truth, I would never have suspected."
            show vivi c1 neutral with Dissolve(0.2)
            vivi "Hahaha! I'll take it as a compliment, but it's not something I'm proud of."
            vivi "I prefer to be honest with the people who matter to me."
            player "Don't worry, little by little it will become easier for you!"

            $ vivi_love += 1
            narrador "[vivi.n] love +1"

        "You don't have to pretend with me":
            
            player "Here, you don't need to pretend, Vivi. You can be yourself."
            show vivi c1 neutral with Dissolve(0.2)
            vivi "That's... nice to hear. It makes me feel more comfortable with you."
            player "With me, you can be exactly who you are, you don't have to pretend anymore… I will do everything possible to make it easier for you!"
            vivi "Thank you, [player.n]. I already trust you enough, little by little you will get to know me for who I truly am!"

            $ vivi_love += 2
            narrador "[vivi.n] love +2"

   

    return