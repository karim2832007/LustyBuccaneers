# Version event: 3
# Version game: 0.32

default obj_newcoo_1 = False

label newcoo_1:
    
    narrador "You unfold the newspaper and begin to read aloud."

    player "Elegia, the island of music, will open its doors to tourists from all over the world in the coming days."
    player "Known for its music academies, cutting-edge technology, and top-level professionals, many young people travel there to study singing, instruments, and composition."
    player "This year, several world-class musical prodigies are expected to debut on the various stages of this great city..."
    player "(Musicians!!... any respectable crew needs to have one...)"
    player "(Hmm... with some luck, maybe there'll be a sexy singer I can charm into joining my crew...)"

    show robin neutral:
        xalign 0.85
        yalign 1.0

    robin "Elegia... i've read about it. the musical culture of that island is quite advanced, they even have orchestras using unique instruments from the new world."
    robin "It's a culturally significant island for the world government... If i'm not mistaken, it's either a summer or spring island."

    show nami with dissolve:
        xalign 0.15
        yalign 1.0

    nami "It's an island that's a bit far from here... But i saw some eternal poses for sale in this city, it might be interesting to head there..."
    nami "But... Why the sudden interest, captain? Don't tell me that..."

    player "(Damn it, she figured it out so fast!)"
    player "F-for the culture! yes! culture and... tourism. It'd be good for the crew to relax a bit after these days of hard work."
    show nami happy with Dissolve(0.2)
    show robin happy with Dissolve(0.2)    
    nami "Haha... sure. whatever you say"

    nami "If we're really going to visit Elegia, we'll need to buy the eternal pose i mentioned... That should be the first step, then i'll handle the rest"

    robin "It could be an interesting stop. Besides, it's not every day an island like that opens to the general public."

    player "(Yes! having a sexy singer on board would be amazing!)"
    player "Alright! let's go buy the eternal pose and set sail!"

    hide nami with dissolve
    hide robin with dissolve
    $ obj_newcoo_1 = True
    jump m_shells_town