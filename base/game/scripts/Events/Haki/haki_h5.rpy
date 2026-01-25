# Version event: 2
# Version game: 0.38

label haki_h5():

    narrador "I push open the door to the old bar. The place smells of cheap rum, fried food, and sea salt, as usual."
    narrador "As always too... [rayleigh.n] is surrounded by gorgeous women"

    show rayleigh at center with Dissolve(0.8)

    show girl_1:
        xalign 0.05
        yalign 1.0

    show girl_2:
        xalign 0.95
        yalign 1.0


    girl_1 "[rayleigh.n]-san, you're terrible! Telling stories like that with that deep voice of yours..."
    girl_2 "Seriously, no man in this town even comes close. You're like a legend come to life."

    rayleigh "Ha ha, easy there, ladies. I'm just an old retired pirate enjoying the company."

    narrador "I walk up to the table. Both girls turn their heads at the same time and give me a slow once-over."

    girl_1 "Well, hello there... Again this handsome young thing?"
    girl_2 "Mmm, look at those eyes. You training with this old-man too, cutie?"
    girl_1 "We could make room for one more if you want to join us..."

    player "He-he... Thanks, but I'm just here to talk to [rayleigh.n]."

    girl_2 "Aw, too bad. We'll be right over at the bar if you change your mind."
    girl_1 "Don't keep this handsome waiting to long, [rayleigh.n]-san"

    pause 0.5
    hide girl_1
    hide girl_2
    with dissolve

    narrador "They stand up, blow me a kiss, and sway their hips as they head toward the bar."
    player "(I can't believe I did that... I must be sick or something...)"
    rayleigh "Heh, lively girls."

    player "You never change, old man. Always surrounded by beauties."

    rayleigh "And you can talk? I've seen you around the islands, kid."
    rayleigh "Always got that redhead navigator barking orders, the dark-haired archaeologist smiling mysteriously, and that tall horned girl trailing behind like she's ready to fight the world for you."
    rayleigh "You've got your own little fan club following you everywhere."

    player "H-hey! It's not like that! They're just... crewmates. Close... crewmates."

    rayleigh "Ha ha ha! Look at you turning red. Relax, I'm only teasing."

    player "A-anyway... changing the subject. Can we keep training {outlinecolor=#a85d74}{color=#ffffff}Haki{/color}{/outlinecolor} today?"

    rayleigh "{outlinecolor=#a85d74}{color=#ffffff}Haki{/color}{/outlinecolor}, huh? Alright, sit down."
    rayleigh "I can feel that You've got the basics of Observation down—feeling intent, dodging a little better in fights."
    rayleigh "Next step is strengthening it: sensing presence from farther away, reading emotions a bit, maybe even getting a glimpse of the future if you're talented."
    rayleigh "Armament is simpler but tougher to master—coating yourself, hitting Logia users, emitting it..."
    rayleigh "And Conqueror's... well, you either have it or you don't."

    narrador "He pauses, takes a long swig of rum, and sighs."

    rayleigh "But honestly... explaining it like this is boring as hell."
    rayleigh "Theory's useless without real pressure. You need something that forces you to use your {outlinecolor=#a85d74}{color=#ffffff}Haki{/color}{/outlinecolor} instinctively."

    rayleigh "So... I came up with a little test. Something fun that'll really put you on edge."
    player "That's it! That's exactly what I want!!"
    rayleigh "Something only a true disciple could obtain for me..."
    player "Keep going, keep going!"
    rayleigh "A test!"
    player "A test? I'm listening."
    rayleigh "Simple. Bring me three very specific items."
    rayleigh "And we can take the final step!"
    player "Great!! It must be difficult to achieve, but that doesn't matter, I'll go to whatever lengths I have to go to!"
    rayleigh "That's the spirit... well, what you have to bring me is..."
    rayleigh "Three pairs of panties."
    rayleigh "One from each of those three main girls in your crew."

    player "W-wait, what?! Panties?!"

    rayleigh "Exactly."
    rayleigh "First: from the fiery redhead navigator who's always worried about money and drawing maps."
    rayleigh "Second: from the calm, dark-haired, sexy archaeologist who always investigating something new."
    rayleigh "Third: from the tall one with the horns, the one who shouts a lot and wants to fight with half the island."

    player "You've got to be kidding me! How am I supposed to get those without getting murdered?!"

    rayleigh "That's the whole point, kid."
    rayleigh "You'll need to use {outlinecolor=#00BFFF}{color=#ffffff}Observation Haki{/color}{/outlinecolor} to predict their movements, sense when they're distracted, avoid their killing intent when you get too close."
    rayleigh "Perfect real-world training. High stakes, high focus."
    rayleigh "Get caught, and you're on your own—getting struck by lightning, turned to stone, or smashed by an oni club."

    player "This is insane..."

    rayleigh "If you pull it off and bring me all three, I'll teach you an advanced Armament technique."
    rayleigh "The kind that can cut through anything. Very useful for what's coming your way soon."

    player "..."

    player "You're enjoying this way too much."

    rayleigh "Immensely."
    rayleigh "Clock's ticking, kid. Better start planning."

    player "Fine... challenge accepted."

    rayleigh "That's the spirit! Now get out of here before I raise the stakes."

    $ _window_hide()
    hide rayleigh with Dissolve(0.8)    

    
    $ haki_nami_panties = False
    $ haki_robin_panties = False
    $ haki_yamato_panties = False
    $ Haki.h = 5
    jump shells_town_bar


label haki_h5_nami():

    player "(I'd love to go in and enjoy the view... But I need to stay focused...)"
    player "{size=40}I have a mission!{/size}"
    player "(This is the perfect moment... I might not get another chance like this...)"
    player "(While she's showering, I'll grab her panties...)"
    player "(They should be around here...)"

    narrador "Carefully, I reach out and grab them, feeling the soft fabric between my fingers."
    narrador "I quickly stuff them into my pocket..."
    #image
    $ haki_nami_panties = True
    narrador "+1 [nami.n]'s panties acquired."

    player "(They're still warm from her body... I can't help myself... I need to resist!)"

    narrador "Just at that moment, the water shuts off..."

    nami "Huh?! Who's out there?!"
    player "(Shit... time to get the hell out of here.)"
    pause 0.5

    $ _window_hide()
    jump ship_mid

label haki_h5_robin():
    
    player "The girls' room is completely empty. The silence is almost suspicious, but there's no time to waste."
    player "(They should be around here...)"
    narrador "I quickly search through [robin.n]'s drawers until I find the one with her underwear. There they are: a pair of black panties with subtle lace, folded with her usual neatness."
    narrador "I pick them up carefully, feeling the soft fabric between my fingers. My heart is racing like crazy. This is weird... but a mission is a mission."
    narrador "I slip them into the inner pocket of my jacket and close the drawer without making a sound."
    #image
    $ haki_robin_panties = True
    narrador "+1 [robin.n]'s panties acquired."

    player "Mission accomplished. Time to leave the nest... Before things get complicated!"


    $ _window_hide()
    $ game.clock.next()
    jump ship_mid

label haki_h5_yamato():


    player "The gym is completely empty after today's intense training."
    player "[rayleigh.n] and his stupid missions... but here I am, doing them like an idiot."
    narrador "I spot [yamato.n]'s locker slightly open. Inside, on top of her folded clothes, are her panties."
    #image
    $ haki_yamato_panties = True
    narrador "+1 [yamato.n]'s panties acquired."

    player "(God, they're completely soaked with sweat. Does she seriously leave them like this?)"
    player "(The smell is strong, intense... it's really sexy!!)"
    player "Focus!!! I can't keep wasting time!"
    player "I'd better get out of here before [yamato.n] comes back and kills me."


    $ _window_hide()
    $ game.clock.next()
    jump ship_mid