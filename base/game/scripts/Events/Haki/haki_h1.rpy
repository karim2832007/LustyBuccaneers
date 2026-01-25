# Version event: 3
# Version game: 0.34

label haki_h1():
    narrador "As you walk into the bar, you see a few people having a drink or chatting among themselves."

    player "Well, well... the girls are out shopping in the city and left me all alone..."
    player "I guess I could make the most of my time and grab a drink here at this bar..."
    player "It's pretty out of the way, not many people around..."
    pause 1.0
    player "Let's see... Where could I sit?..."
    player "!!!"

    show rayleigh c1 

    player "(Who's this old man...)"
    pause 1.0
    player "(What a strange feeling... My instincts are completely on edge...)"
    player "(I have no idea who this guy is... But...)"
    player "(It's clear he's not some ordinary person...)"
    player "(There's this strange pressure around him... some kind of aura... I've never met anyone like this before...)"
    player "(But what really caught my attention...)"
    player "..."
    pause 2.0
    player "{size=40}(Is that he's surrounded by gorgeous women!!!!){/size}"

    show girl_1:
        xalign 0.05
        yalign 1.0

    show girl_2:
        xalign 0.95
        yalign 1.0

    with dissolve

    pause 1.0
    girl_1 "Ahh come on, sweetheart, just a little longer."
    girl_1 "Have another drink with us... We'll have a great time, I promise!"
    girl_2 "Yeah, one more round, handsome!"
    player "(Wtf, what the hell... they could easily be his daughters...)"
    rayleigh "Not now, girls, I've got things to do..."
    pause 0.5
    rayleigh "Argh... Out of booze again... Guess it's about time... What I've been waiting for has finally arrived..."
    rayleigh "I'll probably see you girls around later..."
    girl_1 "Ugh... Always the same excuse..."
    girl_2 "You're such a buzzkill..."
    rayleigh "Hahaha, who'd want to hang around with an old man like me anyway..."
    rayleigh "I'm sure you'll have plenty of fun here without me..."
    player "(What the hell, this old guy's hanging out with those two gorgeous women like it's nothing...)"
    player "(And not only that—he doesn't even seem to care!!!)"
    player "(He must have a secret... I've got to find out what it is...)"
    pause 0.5
    girl_1 "Alright then... Hope you don't lie to us next time..."
    girl_2 "You'll have to make it up to us!!!"
    player "(They're leaving... What a shame! This old man clearly doesn't know how to treat a woman!)"
    pause 0.5
    hide girl_1
    hide girl_2
    with dissolve

    narrador "After the girls leave, you see the old man walking straight toward you."
    pause 0.5
    rayleigh "Well, well..."
    rayleigh "Looks like I'll be postponing my trip to the gambling house..."
    rayleigh "Something told me I had to be here today... And it seems that something is you..."
    player "Eh?!... You talking to me, old man?"
    rayleigh "Hahaha, of course, young man... You seem like a fellow who wears his emotions on his sleeve..."
    player "You're a pretty strange guy..."
    rayleigh "Heh... Well, to the point..."
    rayleigh "..."
    rayleigh "What was the point again?!?"
    rayleigh "Hahahahaha!"
    player "Whatever you say, strange old man..."
    
    $ rayleigh_name = "Rayleigh"

    rayleigh "Hahah maybe I am... My name's [rayleigh.n]."
    rayleigh "As you can see, I'm just an old man..."
    rayleigh "I've retired already, just want a peaceful life..."
    rayleigh "And if I can spend it surrounded by women, booze, and a bit of gambling... even better!!"
    player "Hahah, now that's the life!!"
    player "I like the way you think!"
    rayleigh "It's a good life, isn't it?!"
    pause 0.5
    rayleigh "So then... tell me, you're a pirate, aren't you?"
    player "Huh?!? How did you know?"
    rayleigh "Hahaha, I could tell just by looking at you... Experience, my boy."
    player "(What a weird old man...)"
    player "You're not from the Navy, are you?!?"
    rayleigh "Hahaha, so direct... Of course not... I've been fighting them for years..."
    pause 0.5
    rayleigh "Tell me..."
    rayleigh "Who are you, young man? What's your name?"
    pause 0.5
    player "Well..."
    player "I'm [player.n], and..."


    if player_goal == "Pirate":
        player "And I will be the King of the Pirates!"
        pause 1.0
        rayleigh "Hahaha, are you serious?"
        player "Of course I'm serious!"
        player "The Pirate King is the freest person in the world!"
        rayleigh "Heh... I see."
        rayleigh "You remind me of someone..."


    elif player_goal == "Swordsman":
        player "And I will be the greatest swordsman in the world."
        pause 0.5
        rayleigh "Hahaha, how interesting... you don't look like a swordsman to me!"


    elif player_goal == "Harem":
        player "And I will have the largest harem in the world."
        pause 0.5
        rayleigh "Um... are you serious?! Interesting dream, kid..." 
        rayleigh "I won't deny that the thought crossed my mind back in my youth... Hahahaha!"


    elif player_goal == "King":
        player "And I will be the King of the World."
        pause 1.0
        rayleigh "He... You've got huge ambition to say something like that!"


    rayleigh "These seas are dangerous... Do you really think you can make it?"
    rayleigh "The New World is truly perilous, and even more so its enemies... There's nothing else like it..."
    rayleigh "Do you think you'll be able to conquer the entire ocean?"
    player "Haha, I have no doubt I will!"
    rayleigh "Heh... You sound very confident, young man... That's the spirit... I like that."
    rayleigh "But still... I'll be honest with you... In your current state, it'll be difficult..."
    rayleigh "You're not ready for your journey... yet."
    player "And why do you say that..."
    player "I guess I can trust your intuition..."
    rayleigh "You said you had a clear goal, didn't you..."
    pause 0.5
    player "Of course I do! It's what I promised myself!"
    pause 0.5
    rayleigh "I see..."
    rayleigh "But it's too soon..."
    rayleigh "Maybe you feel strong, like you can beat anyone..."
    rayleigh "But that's not the case... And I think you know it..."
    player "Hmm... Maybe..."
    rayleigh "You feel something strange, don't you? When you look at me... I've noticed..."
    rayleigh "What do you say now..."
    pause 1.0

    #sound of pressure or something like that
    # move the map
    #     linear 0.15 xoffset -12
    #     linear 0.15 xoffset 12
    #     linear 0.10 xoffset -6
    #     linear 0.10 xoffset 0
    #     linear 0.15 xoffset -12
    #     linear 0.15 xoffset 12
    #     linear 0.10 xoffset -6
    #     linear 0.10 xoffset 0
    
    player "That pressure again..."
    player "(This guy is really strong... I can feel it...)"
    rayleigh "Heh..."
    rayleigh "You've got good instincts... But you're still an unpolished gem..."
    pause 0.5
    rayleigh "Let me give you some advice... Take it or leave it..."
    player "Alright!"
    rayleigh "It's just a suggestion... But I think it's exactly what you and your crew need..."
    rayleigh "You have to get stronger—and you've just run into the right person."
    player "What do you mean?"
    rayleigh "I'll put you to the test..."
    rayleigh "And we'll see if you have what it takes..."
    rayleigh "{size=40}To become a true pirate!{/size}"
    player "You mean it!?!"
    rayleigh "Come find me here later... There are some things I forgot to take care of first..."
    rayleigh "I'll be waiting!"
    rayleigh "I know you'll come..."
    rayleigh "Hahaha! Goodbye!"

    $ _window_hide()
    hide rayleigh with dissolve    

    player "What a weird old man... But he's really strong... That's undeniable."
    player "[rayleigh.n]... Why does that name sound familiar..."
    pause 0.5
    player "What should I do!?!"
    pause 1.0


    $ Haki.h = 1
    jump shells_town_bar
