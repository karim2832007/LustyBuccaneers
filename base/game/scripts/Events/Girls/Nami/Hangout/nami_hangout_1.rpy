# Version event: 1
# Version game: 0.14

label nami_hangout_1:
    nami "How are you, Captain?... Since we live together on this ship,"
    nami "I imagine you've already learned a thing or two about me and my tastes..."
    player "Of course, I'm always very attentive to you and the rest of the girls."
    player "I always see you sunbathing, or looking for ways to make money... among many other things..."
    nami "Soo... you surely know what kind of islands I'd like to visit to relax, right?"

    menu:
        "A winter island":
            player "Umm... I suppose a winter island, right? To see its beautiful landscapes!"
            show nami c1 anger with dissolve
            nami "I hate the cold, Captain... Two minutes ago, you said you always see me sunbathing..."
            nami "Now I see how much attention you pay to us girls and me..."
            nami "Not everything is adventures, Captain! Resting from time to time, enjoying and celebrating with friends, and recovering for the next adventures are very important..."
            nami "I didn't realize you were so narrow-minded and carefree... I'll get back to my work..."

            $ nami_love -= 1
            narrador "[nami.n] Love -1"

        "A summer island":
            player "I'm sure you would love a summer island!... to enjoy its beaches and relax peacefully!"
            nami "Captain!! Of course, I love warm places with beautiful beaches and stunning sunsets to see!"
            nami "Any tropical island where I can relax, sunbathe, and enjoy something refreshing would be ideal!"
            player "Perfect, I'll keep that in mind. I'm sure we'll visit many on our journey!"
            show nami c1 happy with dissolve    
            nami "Thank you, Captain! I didn't realize you saw me that way... I'll get back to my duties now. See you later."
            player "Keep it up!"

            $ nami_lust += 1
            narrador "[nami.n] lust +1"

    return