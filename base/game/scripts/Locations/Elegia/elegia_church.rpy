# Version event: 2
# Version game: 0.27

label elegia_church():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "elegia_church"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_elegia_church

label m_elegia_church():
    if Elegia.h == 10:
        player "First try!"
        player "Well done girls... We've left the forest behind!"
        nami "Look over there Captain, I can see some kind of building!"
        robin "It looks like some kind of old church..."
        yamato "If I were those Jellyfish pirates, I'd hide in a place like that..."
        yamato "It could easily be the enemy's base..."
        yamato "Mnmnmn... !!!"
        yamato "Careful, we have company!"

        window hide
        show kalifa with dissolve
        pause 1
        window auto

        unknown "You finally arrived... I couldn't believe how much time you wasted circling around in that forest..."
        unknown "You really kept me waiting..."
        player "(Wow who is this sexy woman?!?!)"
        player "(Look at the size of those melons!! She's not even trying to hide them with that outfit!)"

        yamato "And who are you?"

        call set_name_kalifa from _call_set_name_kalifa

        kalifa "My name is [kalifa.n]."
        kalifa "Don't expect a smile, or a welcome. I'm not here because I want to be, to be honest."
        player "(Who the hell is this now?... I'd remember a beauty like her if I knew her...)"

        kalifa "I've been ordered to watch you. A direct request from Captain [koby.n]!"
        kalifa "Really annoying... But I had no choice..."

        player "([koby.n]... So he was already spying on me even before I entered the forest...)"
        player "(I guess he realized I was up to something... Clever guy!)"
        player "(This sexy vixen is under his command... That little [koby.n] really has changed over time)"
        player "(Maybe I should teach this subordinate of his a thing or two hehe... Show her who's the best here!)"

        #mad kalifa

        kalifa "What are you thinking about, pervert... With that face staring into space..."
        kalifa "Don't get excited just because I'm here... I'm not here to keep you company..."
        kalifa "Nor to clean up your blood or whatever mess you make if you decide to play hero with those lowly pirates you're after"

        kalifa "Look, I'll be clear. This place bores me, it stinks, and you're not exactly thrilling company."
        kalifa "Now that you're here I suppose you'll go into that church no matter what I say..."
        kalifa "I'm not wasting my time either way..."
        kalifa "If you want to play the brave guy, do it yourself."
        kalifa "I don't have time to follow you around like some babysitter."
        player "(Hahaha I like her attitude... I think she likes me...)"

        if player_hp < RPGPlayer.true_hp_max() * 0.75 or player_mana < RPGPlayer.true_mana_max() * 0.75:

            kalifa "Although... Look at the state you're in... You look beat up, totally worn out."
            kalifa "I can't let you die just yet. Not because I care, don't get confused..."
            kalifa "But I don't want to have to explain anything to [koby.n] if something happens to you in there"
            kalifa "Take this. It'll help keep you on your feet a bit longer."

            window hide
            $ RPGPlayer.heal(heal_amount = 1000, mana_amount = 1000)
            window auto
            narrador "Now you are fully heal"
            player "Wow thanks, I feel much better now!"
            player "I knew you cared about me!"
            kalifa "Ha! Not even in your dreams... You're shameless..."

        kalifa "You're such a pain..."
        kalifa "If the Captain didn't care about you, I would've taken care of you right here and now!"
        kalifa "Anyway, I doubt I'll have to lift a finger myself..."
        kalifa "There are quite a few pirates inside the church..."
        kalifa "They're nobodies... But I'm sure they'll give you a hard time..."
        kalifa "Oh right... [koby.n] asked me to give you these potions"
        $ minorpotion += 2
        narrador "+2 Minor Potions"

        kalifa "I'm out of here. I've wasted enough time with you."
        kalifa "I hope I never see you again..."

        hide kalifa with moveoutright

        player "(What an insufferable woman...)"
        player "(But there's something about that shitty attitude that makes me want to... {size=40}Tame her!{/size})"
        player "([kalifa.n], huh? We'll see how long your arrogance lasts once you're the one at my feet.)"
        player "(We'll meet again!)"
        yamato "What an arrogant woman! She's really underestimating us..."
        player "Yeah Yeah, that's right but now it doesn't matter... Let her go, we have something else to worry about"
        player "Let's go to the church, we have someone to rescue!"
        yamato "Yes! On our way Captain!"


        $ Elegia.h = 11

    menu:
        "Enter the church":
            jump elegia_church_inside

        "Back":
            jump elegia_forest
