# Version event: 3
# Version game: 0.23

label vivi_hangout_5:
    player "Vivi, do you have a hobby that no one knows about? Something you like to do that we don't know about..."
    vivi "Mmm... well, it's no secret, but I love taking care of animals."
    vivi "When I was a child, I spent hours in the royal garden taking care of the birds and camels."
    player "That sounds adorable. Do you still do it?"
    vivi "Whenever I can. Animals don't judge, they just accept you."
    player "I'll see what I can do so you can keep doing it with us..."
    show vivi c1 happy with Dissolve(0.2)
    vivi "That's so sweet to hear. It always makes me feel so comfortable with you."

    $ vivi_love += 2
    narrador "[vivi.n] love +2"

    return