# Version event: 2
# Version game: 0.24

label nami_c2_outfit:

    show nami c1 with dissolve

    player "While we were walking around the city with the girls, I saw a very interesting shop..."
    nami "Oh really? What kind of shop, Captain?"
    player "Well, something I'm sure you're going to love... Look, I got something for you, here you go, [nami.n]"
    show nami c1 happy with Dissolve(0.2)
    nami "Mmh? A gift for me? How generous, captain!!! You've never done something like this for me before!"
    nami "A bag!?!... What could it be... Clothes maybe?!?... Mnmnm how strange... Before I open it I was thinking..."
    show nami c1 serious with Dissolve(0.2)
    nami "This is the first gift of this kind you've given me... You don't want something in return, do you!!!"
    player "Who, me? of course not!... No hidden intentions"
    player "You know me [nami.n]!"
    show nami c1 happy with Dissolve(0.2)
    nami "Hhahaha that's exactly why I'm asking, Captain!!!"
    nami "You're always thinking about one thing!!"
    player "Hhaahah you know me well! and maybe you're not wrong!"
    player "I just thought this dress would highlight your talents... especially if you decide to use it to entertain the crowd!"
    show nami c1 neutral with Dissolve(0.2)
    nami "Je... Sounds like you're offering me a business deal."
    player "Why don't you try it on and we'll see if it's worth the investment?"

    window hide
    hide nami with moveoutright
    pause 1.0
    window auto

    show nami c2:
        xalign 1.5
        yalign 1.0
        linear 0.4 xalign 0.5

    pause 1.4

    nami "Tadaaaa!"
    nami "So, Captain? What do you think?"
    nami "Do you like what you see?"
    player "Wow... I didn't expect it to look this sexy. That dress was made for you!"
    show nami c2 happy with Dissolve(0.2)
    nami "hahaha I knew you'd say something like that Captain!"
    show nami c2 neutral with Dissolve(0.2)
    nami "I really like it too... Maybe you should buy me clothes more often... We'd both benefit!"

    $ nami_love += 2
    narrador "[nami.n] Love +2"

    player "Of course I will!"
    player "(The rest of the girls would look amazing in similar outfits... I'll see what I can do with the others!)"
    nami "So... Did you just give it to me to score points or did you actually have a business idea in mind?"
    player "Hahah I like the way you think [nami.n], that's why you're in my crew!"
    player "With that hip movement you could raise more funds than an entire treasure!"
    nami "Are you suggesting I dance in this outfit to attract customers?"
    player "I'm just saying... you could turn every night into gold, if you know what I mean."
    show nami c2 berries with Dissolve(0.2)
    nami "Hehehe... I like the way you think. Easy money, and with my personal bodyguard by my side..."
    player "Exactly. I'll make sure to keep the drunks away... you just make sure they throw their [Berries.n]."
    nami "Then we have a deal, captain. But fair warning: I'm keeping the biggest share of the loot."
    player "As always... but at least I'll have front row seats."
    show nami c2 neutral with Dissolve(0.2)
    nami "Hmph~ Only if you behave yourself..."
    nami "Now all that's left is to find somewhere I can dance!"
    player "I already have something in mind... Just leave it to me, we'll see what fate has in store..."
    player "Yuba might be a good option!"

    window hide
    window auto
    hide nami with moveoutright
    pause 0.5
    return