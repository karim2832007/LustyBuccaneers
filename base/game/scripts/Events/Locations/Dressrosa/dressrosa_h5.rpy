# Version event: 6
# Version game: 0.33

label dressrosa_h5():
    $ ui_interface = False

    player "Oooohhhh!!!"
    player "What a great atmosphere!! This is pretty lively..."
    player "This must be the fighters's preparation room, I guess this is where I'll have to wait for my turn to fight..."
    pause 0.4
    player "Heheh!... well, there sure are some really big guys here..."
    player "I feel a strong pressure in the air..."
    player "There must be some good fighters hidden around this area..."
    unknown "Hey, look at that kid... I think he got lost and ended up here."
    unknown "Hahaha this kid wants us to take him seriously..."
    player "I see, everyone's got weapons and battle gear... Looks like you can use any kind of weapon..."
    player "I guess I'll take a walk around here to kill some time."
    pause 0.4
    unknown "What's a weakling like this doing here in this tournament..."
    unknown "I think he was the last one to sign up..."
    player "!!!"
    player "Mnmnm... And that commotion... I think a fight just started..."

    show spartan c1:
        xalign 0.05
        yalign 1.0

    show rebecca c2:
        xalign 0.85
        yalign 1.0

    with Dissolve(0.5)

    spartan "This is not amusing at all... It's really insulting that someone from your family is here..."
    player "(It's the pink-haired warrior angel!!)"
    player "(Lucky me, finding her so fast!!)"
    pause 0.4    
    spartan "Taking part in this tournament..."
    spartan "I thought I'd made it clear what would happen if I saw you around here..."
    spartan "Looks like I'll get to enjoy myself and play with you sooner than expected..."
    show rebecca c2 annoyed with Dissolve(0.2)
    spartan "That tasty body of yours... Why don't you give up right now, and we have some fun for a while, beautiful..."
    rebecca "You're disgusting..."
    spartan "Hehe..."
    spartan "No one came to watch weaklings like you get crushed, girl... The crowd only gets excited when the strongest fight..."
    spartan "We didn't come here to play, get lost already!!"
    rebecca "What are you saying!! I have just as much right to participate here as you do..."
    spartan "Don't you get it?! I told you to leave..."
    spartan "Looks like I'll have to show you the way out by force..."
    rebecca "Wait! We can't fight here or we'll be expelled..."
    spartan "Too late, damn it, you'll pay for your family..."
    player "Wait, big guy!!"
    player "What do you think you're doing?"
    player "What the hell is wrong with you... Leave that girl alone!"

    $ _window_hide()

    hide rebecca with Dissolve(0.5)

    show spartan at x_move(x_start=0.05, x_end=0.5, dur=0.3)

    pause 0.3

    show spartan c1:
        xalign 0.5
        yalign 1.0

    spartan "You talking to me?!?"
    spartan "I guess I'll have to teach you a lesson first."

    call fight_start pass (enemy_pass = enemy_spartan, no_run = True, no_interface = True) from _fight_enemy_spartan

    spartan "B-but... y-you... How the hell are you so strong..."
    $ _window_hide()
    hide spartan with Dissolve(0.8)

    narrador "After spartan's fall, you feel many gazes from the darkness"
    $ _window_hide()

    show events dressrosa h5 silhouette_1 with Dissolve(0.8):
        xalign 0.5
        yalign 0.5
        yoffset 0
        zoom 1.0
        linear 3.0 zoom 1.2 yoffset 50

    pause 2.2

    show events dressrosa h5 silhouette_2:
        xalign 0.5
        yalign 0.5
        yoffset 0
        zoom 1.0
        linear 3.0 zoom 1.2 yoffset 80

    pause 3.0

    show events dressrosa h5 silhouette_3:
        xalign 0.5
        yalign 0.5
        yoffset 0
        zoom 1.0
        linear 3.0 zoom 1.2 yoffset 80

    pause 3.0

    show events dressrosa h5 silhouette_4:
        xalign 0.5
        yalign 0.5
        yoffset 0
        zoom 1.0
        linear 3.0 zoom 1.2 yoffset 50

    pause 3.0
    hide events dressrosa h5 silhouette_4 with Dissolve(0.8)

    player "(There are several strong guys watching me right now...)"
    player "(I think I should listen to the girls and keep a lower profile)"

    pause 0.3
    $ music_dressrosa()

    unknown "Did you see what he did?"
    unknown "That kid knocked out [spartan.n] very easily..."
    unknown "No way... He's one of the best gladiators in the coliseum!"
    guard "What's all this commotion!!"
    guard "Attention, clear the area quickly!!!"
    pause 0.5

    show events dressrosa h5 guard with Dissolve(0.5):
        xalign 0.5
        yalign 1.0

    guard "Hey you, kid! What do you think you're doing!"
    guard "Did you start the fight?!"
    player "Me?!?!"
    guard "You're going to have to leave immediately!"
    guard "You're out! We don't want instigators before the event starts!"
    player "What are you saying!!?! What do you mean I'm out!"

    show events dressrosa h5 guard at x_move(x_start=0.5, x_end=1.6, dur=0.3)

    pause 0.3

    show sai c1 with Dissolve(0.8):
        xalign -0.3
        yalign 1.0

    sai "Out?!? Don't tell me... Hold it right there, idiot!"

    sai "That big guy was the one who started it all, bothering the girl over there and then picking a fight with the young man"
    sai "If anyone has to leave, it should be him..."
    unknown "Wow, that must be one of the brothers from the Kano Country..."
    unknown "It's Sai of the Chinjao family!!! His grandfather is a true legend!"
    guard "You over there, do you confirm the same?!"
    unknown "Uh, yeah, seriously... [spartan.n] was the one who started it..."
    guard "Good... Then [spartan.n] is out..."

    hide events dressrosa h5 guard with Dissolve(0.8)

    pause 0.8

    show sai c1 at x_move(x_start=-0.3, x_end=0.5, dur=0.3)

    pause 0.3

    show sai c1:
        xalign 0.5
        yalign 1.0


    player "Haha, thanks for stepping in, you saved me with that guard over there!"
    sai "There's nothing to thank me for, haha!"
    sai "In fact, don't even mention it... It really bothers me when people thank me..."
    sai "It's really annoying when someone says thank you..."
    sai "I hate that damn word..."
    narrador "You notice how Sai starts getting angry and worked up in an instant..."
    sai "{size=40}Take it back, damn you!!!!{/size}"
    sai "{size=40}Withdraw your damn gratitude, idiot!{/size}"
    player "Aaaaaahhh... What's wrong with you, you're scary!"
    guard "Hey you, stop right there, grab him so he doesn't start a fight!!"
    sai "{size=40}Don't thank me, idiot!!!!{/size}"

    rebecca "Hey you, kid, come here quickly... Let's go!"
    rebecca "Quick, follow me!!"
    player "Alright, I'm coming, I'm coming!! I'm following you!"


    $ _window_hide()
    show screen screen_black with Dissolve(0.6)

    hide sai

    $ game.location = "dr_ac_co_statue"
    scene BG locations:
        blur 3
    
    show rebecca c2 at center

    hide screen screen_black with Dissolve(0.3)

    player "Wow, this place!!"
    player "This place is full of helmets and armor, and all kinds of weapons!!"
    player "Awesome!!! Can I really use whatever I want from here?!?"
    show rebecca c2 happy with Dissolve(0.2)
    rebecca "Hahaha, you're not only strong, you're also really fun!!"

    $ rebecca_love += 2
    narrador "[rebecca.n] love +2"

    player "Mnmnm!?!?"
    player "Wow, do you hear that!?!?"
    player "They're really pumped out there in the arena... you can hear the shouting even from here!"
    show rebecca c2 neutral with Dissolve(0.2)
    rebecca "Yeah, they must have started the primary qualifying matches outside."
    rebecca "A lot of people will be filtered out until only the best in the tournament remain..."
    player "I had no idea about that... I guess it makes sense, it must be pretty fun..."
    rebecca "You think so? Well, it's not really like that... Do you know why they're so cheerful out there?"
    player "No idea... you tell me... You seem to be from around here..."
    show rebecca c2 serious with Dissolve(0.2)
    rebecca "It's simple... They want to see blood..."
    rebecca "And gladiators like me give it to them gladly..."
    rebecca "As you can see, besides the foreign fighters who came especially today, the place is packed with gladiators..."
    rebecca "Guys like [spartan.n] or me often fight here..."
    rebecca "We're captive gladiators... forced to fight until one day we're killed in the arena."
    player "Well that really sounds bad... Who forces you?"
    rebecca "Most are here for angering the Donquixote family..."
    player "!!!"
    rebecca "But that's another story..."
    rebecca "The king promised us freedom if we achieve a thousand victories... But that's a death sentence... No one can get out of here alive!"
    rebecca "Over time, little by little I made a name for myself, keeping a great winning streak in the Coliseum..."
    rebecca "But today is different... Today very strong fighters came from all over the seas..."
    rebecca "We're all here competing for the grand prize.."
    rebecca "Like I told you, the crowd here usually only cares about seeing blood..."
    rebecca "But the blood they most want to see is the losers one..."
    rebecca "This coliseum exposes everyone's true nature"
    rebecca "It's nothing but a spectacle for them... just a release from their everyday problems and tensions"
    player "Well, that doesn't sound so fun anymore..."
    show rebecca c2 neutral with Dissolve(0.2)
    rebecca "Uh... Sorry for ruining the moment, let's change the subject..."
    pause 0.3

    menu:
        "It's really interesting":
            player "Haha, no problem, it's really interesting to know what goes on around here!" 
            $ rebecca_love += 1
            narrador "[rebecca.n] Love +1"

        "No problem!":
            player "Don't worry, it's okey..."

    player "We're comfortable with each other now, right?!"
    rebecca "Well, yeah... We're comfortable now... Few people tend to support me here..."
    rebecca "I'm very grateful for what you did a little while ago, when you came to help me"
    rebecca "I really can't stand the way [spartan.n] acts, I hate that guy..."
    rebecca "You took down that brute so easily... Who are you?"
    player "Hahaha, to be honest it wasn't much... That fool asked for it, you saw it, it wasn't really a problem..."
    player "I am [player.n]"

    if player_goal == "Pirate":
        player "And I will be the King of the Pirates!"
        rebecca "Hahaha, are you serious?! So you're a pirate... You don't seem like a bad guy, you're really strange... I like you!"
        $ rebecca_love += 2
        narrador "[rebecca.n] love +2"

    elif player_goal == "Swordsman":
        player "And I will be the greatest swordsman in the world."
        rebecca "Hahaha, how interesting... you don't look like a swordsman to me!"
        $ rebecca_love += 1
        narrador "[rebecca.n] love +1"

    elif player_goal == "Harem":
        player "And I will have the largest harem in the world."
        rebecca "Um... are you serious?! That's... kind of weird, but interesting, I guess haha!"
        $ rebecca_lust += 2
        narrador "[rebecca.n] lust +2"

    elif player_goal == "King":
        player "And I will be the King of the World."
        rebecca "Are you serious?! You're really strange... You've got huge ambition to say something like that!"
        $ rebecca_love += 2
        narrador "[rebecca.n] love +2"

    player "Well, you'd better believe it, because I'm going to pull it off, hehehe!!"
    pause 0.5
    player "Wowww!!"
    player "Look at that... what an incredible statue!!"
    $ _window_hide()

    pause 0.5
    $ black_to_img("events dressrosa h5 h5_1")
    pause 1.5

    player "King of Gladiators Pancratium"
    player "An old half-naked warrior... Woow, incredible!"
    rebecca "You're interested, aren't you?"
    rebecca "The statue in front of you is of a legendary gladiator"
    rebecca "The greatest gladiator in the history of the Corrida Coliseum"
    rebecca "He is Kyros..."
    rebecca "Out of 3,000 fights, he earned 3,000 victories... and received only a single wound among all those battles"
    player "Wow, was he really that strong?!?"
    rebecca "About 20 years ago he fought in the Coliseum... and yet he's a complete unknown to the country..."
    rebecca "No one remembers anything!"
    player "What are you saying?!?! That's really strange... Why did that happen, why does no one remember?"
    rebecca "None of the elders, or even the oldest gladiators... No one remembers having met him..."
    rebecca "It's the most enigmatic statue in [Dressrosa.n], for all we know he might not have existed"
    rebecca "Maybe it's made up, I don't know, no one even knows when this statue was built, all that's known is what this plaque says"
    rebecca "Anyway, no one wants to remove the statue..."

    menu:
        "It's quite a strange mystery":
            player "Mmnnm... Its quite a strange mystery..."  
            player "Maybe I should ask the girls when I get out of here." 


        "It looks incredible!":
            player "It's really weird, isn't it? But it's true it looks incredible!"
            player "He looks like a strong, very manly guy!"
            rebecca "Yeah... It's true... I like it too!"

            $ rebecca_love += 1
            narrador "[rebecca.n] love +1"

    pause 0.3
    $ black_to_img("BG locations", hide="events dressrosa h5")

    show rebecca c2 neutral with Dissolve(0.2)    
    unknown "Well, would you look at that!! It's [rebecca.n] the great warrior!"
    narrador "You hear murmurs as some gladiators point at [rebecca.n] and laugh at her!"
    show rebecca c2 anger with Dissolve(0.2)
    unknown "You gonna compete, doll?"
    unknown "You're too pretty to be here..."
    unknown "Do you really think you can keep your win record..."
    unknown "With luck you'll make it past the qualifiers... Hahaha!"
    unknown "You must be more than relieved, right?!..."
    unknown "Your rival [spartan.n] is out of the tournament... Before he could lay a hand on you and finish you off..."
    unknown "Maybe I could take his place... and have a little fun myself..."
    unknown "Hahaha, leave her alone, idiots, we'd better go before they call us!"
    unknown "See you later, [rebecca.n]... We're all waiting to see you hit the floor!"
    unknown "Hahahaha!!"
    pause 0.5
    player "What a bunch of weaklings... You shouldn't pay them any attention..."
    player "What do they have against you?"
    rebecca "Ignore them"

    #sad face with tears /// helmet // vignette

    narrador "You notice all the local gladiators laughing at [rebecca.n] or giving her dirty looks."
    rebecca "It all ends today... Today will be my last battle!"
    rebecca "I'll claim the Devil Fruit and put an end to this..."
    rebecca "{size=40}I'm going to kill [donflamingo.n]!!{/size}"
    player "W-What!?!?"
    rebecca "...."
    show rebecca c2 serious with Dissolve(0.2)
    rebecca "Don't let the sun in the sky fool you... There's a lot of darkness in this country..."
    pause 0.5
    rebecca "You'd better go, and don't be seen with me..."
    player "I don't care what the others think..."
    rebecca "Please listen to me, it's for your own good... We'll talk later"
    player "Uh.. Wait!"
    player "The toy soldier said I should look after you and deliver a message... You have to be careful, you have nothing to prove!"
    rebecca "The toy soldier!!!"
    show rebecca c2 neutral with Dissolve(0.2)
    rebecca "When will he understand that I'm already grown up? I've already turned 18, he should cut me some slack..."
    pause 0.5    
    rebecca "What did he tell you? What did he say to you?!?"
    player "Well, nothing... He just told me to keep an eye on you... What should he have told me!?"
    rebecca "Just that..."
    rebecca "Well then, it doesn't matter..."
    player "???"
    rebecca "This time I'll take the risk for him..."
    $ _window_hide()
    show rebecca c2 helmet with Dissolve(0.8)
    pause 0.5
    rebecca "I'll keep my fingers crossed for both of us..."
    rebecca "I hope to see you after the qualifiers..."
    rebecca "Goodbye [player.n]"

    hide rebecca
    with dissolve

    $ Dressrosa.h = 6
    $ _window_hide()
    $ ui_interface = True
    jump dr_ac_co_fighters_preparations
