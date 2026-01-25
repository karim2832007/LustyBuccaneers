# Version event: 4
# Version game: 0.36

label haki_h2():

    narrador "You come back to the bar, looking for [rayleigh.n]... But unfortunately you don't see him anywhere..."
    player "(Where could that old man be?... Don't tell me he won't be around today...)"
    player "(!!!)"
    player "(That's the blonde he was with last time... And who's the other guy?!)"
    
    show girl_1 with dissolve:
        xalign 0.5
        yalign 1.0

    #$ sarquiss_name = "Sarquiss"

    show sarquiss c1 with dissolve:
        xalign 0.1
        yalign 1.0

    show sarquiss c1:
        xalign 0.1
        yalign 1.0

        linear 0.4 xalign 0.4

    show girl_1:
        xalign 0.5
        yalign 1.0

        linear 0.4 xalign 0.9

    pause 0.4

    sarquiss "Hey, gorgeous... alone at this hour?"
    girl_1 "..."
    sarquiss "Don't tell me no one's with you, that would be a waste."
    girl_1 "I prefer to be alone, thanks."
    sarquiss "Oh come on, don't be like that. I can buy you a drink... or two."
    girl_1 "No, really. I'm fine like this."
    sarquiss "So proud, are you? Come on, I don't bite."
    girl_1 "I'm not interested, I don't like wasting time..."
    sarquiss "Hahaha, they all say that at first... Don't you know who I am?!?"
    girl_1 "..."
    sarquiss "Look at me, baby, it's in your best interest to have friends like me in this place."
    girl_1 "I'm not looking for friends; I have plenty around here..."
    sarquiss "Don't play hard to get. You're just waiting for someone better... but spoiler: he's not coming."
    girl_1 "I already told you no; it'd be better if you leave me alone, or you might end up lying on the floor..."
    sarquiss "Calm? Relax, I just want to chat... don't be so cold."
    girl_1 "..."
    pause 0.5
    sarquiss "What?!?"
    girl_1 "I've been clear—leave."
    sarquiss "Tsk, what a temper... You're not even nervous... I like that. Fiery girls always entertain me more."
    sarquiss "I suppose one has to use a little force in these situations... Show who's in charge here..."
    girl_1 "Uh... Wait... What are you planning... I already told you no..."
    player "Hey, hold it! She said no..."
    sarquiss "Huh?!? You talking to me..."
    sarquiss "What, are you her boyfriend or something?!... This girl is with me now—forget about her..."
    player "Looks like you don't understand words... Maybe I should teach you a lesson..."
    sarquiss "Hahaha, looks like you don't know who you're messing with, twig..."
    sarquiss "I think it's time to liven up this bar a bit..."
    girl_1 "Wait... Don't cause trouble here..."
    sarquiss "Don't worry, sweetheart... You stay to the side; I'll be back with you in a few minutes..."

    rayleigh "Hahaha, the young lady is right! Today is not a good day to cause trouble..."
    girl_1 "[rayleigh.n]!"

    hide girl_1 with Dissolve(0.2)    

    show sarquiss c1:
        xalign 0.4
        yalign 1.0
        linear 0.3 xalign 0.15

    show rayleigh c1 with Dissolve(0.2):
        xalign 0.9
        yalign 1.0

    pause 0.2

    sarquiss "Huh?!? And who are you, old man?!"
    player "Ah, you're the lucky old man from last time... I was looking for you..."
    sarquiss "You two know each other?... It's not that I enjoy hitting old men, but if I have no other choice..."
    rayleigh "Hahaha, you're a brash and inexperienced youngster, it seems... Unfortunately for you, I'm not in the mood to waste time today..."
    rayleigh "I lost a lot at cards, you know..."
    sarquiss "What the hell are you talking about, old man..."

    pause 0.5

    show BG locations at vibration:
        blur 8

    narrador "Once again, you feel that strange sensation, and an odd pressure strikes against the stranger."   
    
    sarquiss "Huh?!? W-w-what the... ughhhh..."    
    pause 0.5    
    hide sarquiss with dissolve

    show BG locations:
        blur 3
        zoom 1.0
        xalign 0.5
        yalign 0.5

    player "(That strange power again... He seems to have total control over whatever this ability does...)"

    show rayleigh c1:
        xalign 0.9
        yalign 1.0

    show girl_1 with dissolve:
        xalign 0.2
        yalign 1.0

    girl_1  "Pfft... He turned out to be a good-for-nothing..."
    girl_1  "Thanks again! You're always getting all the creeps off our backs!"
    girl_1  "Hey, you lot—weren't you going to help me?! You saw perfectly well what was happening!... Get him out of here!!"
    unknown "Yes! Yes! We're sorry, miss..."

    pause 0.5

    girl_1  "Tell me, [rayleigh.n]... Drinking anything today???"
    rayleigh "Not today, no! Thanks... I came to chat a bit with the young man here..."
    girl_1  "Alright... I'll leave you two alone then..."
    girl_1  "And you, boy... Thanks for trying to help me when no one else would!"
    girl_1  "If you come by often, come see me!"

    hide girl_1
    with dissolve
    pause 0.5

    show rayleigh c1:
        xalign 0.9
        yalign 1.0
        linear 0.4 xalign 0.5

    pause 0.4

    show rayleigh c1:
        xalign 0.5
        yalign 1.0

    rayleigh "Hahaha, you seem lucky with the young ladies!"
    player "Not as much as you, last time you were surrounded by girls..."
    rayleigh "Hahaha, I'm already retired, unfortunately... Time catches up to us all..."
    player "Well, I don't think time affects you much..."
    player "You walk around so carefree and calm... But I can see the reality..."
    pause 0.5    
    player "I feel you're truly powerful!"
    rayleigh "Heh..."
    player "I can't explain it... But I'm sure... you had something to do with that guy fainting out of nowhere..."
    player "I'm sure of it!"
    rayleigh "You're a good observer!"
    rayleigh "It's not something just anyone can sense..."
    pause 1.0
    rayleigh "{size=40}It's thanks to a power...{/size}"
    rayleigh "One you must learn to master too... If you want to reach the summit..."
    player "Ahh?!"
    rayleigh "It's known as {outlinecolor=#a85d74}{color=#ffffff}Haki{/color}{/outlinecolor}..."
    player "{outlinecolor=#a85d74}{color=#ffffff}Haki{/color}{/outlinecolor}?!"
    rayleigh "Pay attention, [player.n]..."
    rayleigh "Believe it or not, {outlinecolor=#a85d74}{color=#ffffff}Haki{/color}{/outlinecolor} is a power that resides in all the world's inhabitants..."
    rayleigh "Presence, will, intimidation..."
    rayleigh "Most people don't notice that power... And those who do don't always manage to exploit it to the fullest..."
    rayleigh "Abandon any doubt..."
    rayleigh "Only then will you be strong..."
    player "..."
    rayleigh "Well then, to sum it up..."
    rayleigh "{outlinecolor=#a85d74}{color=#ffffff}Haki{/color}{/outlinecolor} is divided into two very important types..."
    rayleigh "First is the power to sense the presence of others... It's called {outlinecolor=#00BFFF}{color=#ffffff}Observation Haki{/color}{/outlinecolor}..."
    rayleigh "If you master it, you'll be able to know the number of enemies around you, whether they're hiding, and if you focus, you can even know what the opponent will do before they do it..."
    rayleigh "Then, secondly, there's {outlinecolor=#B0B0B0}{color=#ffffff}Armament Haki{/color}{/outlinecolor}"
    rayleigh "This is as if you had an invisible armor..."
    rayleigh "Armor doesn't just protect... It also serves to attack..."
    rayleigh "You can even transfer it to weapons... among other uses it has..."
    rayleigh "Observation and Armament... Those are the two types of Haki..."
    rayleigh "However, there's also a small number of people who can use a third type of Haki..."
    rayleigh "Don't get distracted..."

    pause 0.5
    narrador "Once again, you feel that strange sensation in the air..."  

    rayleigh "You felt it, didn't you?"
    rayleigh "This is the power to intimidate others... {outlinecolor=#FFD700}{color=#B08D57}Conqueror's Haki{/color}{/outlinecolor}... The most powerful men across all the seas generally have this Haki at their full disposal..."
    rayleigh "Unlike the other two, this last one can't be improved through training..."
    rayleigh "That's because it's a representation of your spirit; it will only improve as you yourself improve..."
    player "Incredible... it's what you used earlier on that guy; I've already seen you use it..."
    rayleigh "That's right—good that you noticed..."
    rayleigh "I can sense that you can use them too..."
    player "Now that I think about it... I believe I've run into many people who, without me realizing it, were using it... It's amazing!"
    rayleigh "That's likely a good observation... It's very probable you've seen it several times..."
    rayleigh "Hahaha, have I earned your respect now?!"
    player "Of course, old man!!"
    rayleigh "But learning to use it isn't easy."
    rayleigh "Generally we'd have to start from zero... but you've already made some progress..."
    rayleigh "That's good... Now the goal is to master it..."
    player "So when do we start, old man! You have to teach me!"
    rayleigh "Haha... First of all, don't call me old man anymore... You can call me master or [rayleigh.n]..."
    player "Alright, [rayleigh.n]! Tell me what I have to do!"
    rayleigh "Haha, don't rush! All in good time!"
    rayleigh "Come see me next time... and we'll discuss it; it's gotten late today"
    player "Alright, [rayleigh.n]! I'll come back for you!"
    rayleigh "Perfect, come prepared! Until next time!"

    pause 0.4   

    $ _window_hide()
    hide rayleigh with Dissolve(0.8)    

    $ Haki.h = 2
    jump shells_town_bar