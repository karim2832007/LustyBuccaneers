# Version event: 3
# Version game: 0.40

label haki_h6():
    
    if not haki_nami_panties or not haki_robin_panties or not haki_yamato_panties:
        player "(Before talking to [rayleigh.n], I need to get the underwear from [nami.n], [robin.n], and [yamato.n]...)"
        player "(I'd better search the whole ship carefully...)"
        
        if not haki_robin_panties:
            player "(I have to look in the girls' room... When there's no one inside.)"

        if not haki_nami_panties:
            player "(I have to look in the bathroom...)"

        if not haki_yamato_panties:
            player "(Or maybe in some room where they spend a lot of time training...)"

            
    else:
        show rayleigh at center with Dissolve(0.8)

        player "[rayleigh.n], master!! I'm back again."
        player "And I brought what you asked for! I completed your mission!"
        rayleigh "Mission? What mission are you talking about, kid!"
        player "The mission... you know... {size=25}the panties thing...{/size}"
        rayleigh "Seriously?! And you're still alive!?... You're incredible, kid!"
        pause 0.5
        rayleigh "Alright! Alright! Let's see... show me what you've got."
        narrador "Being very careful so no one else in the bar notices, you hand over the result of your mission..."

        $ haki_nami_panties = False
        $ haki_robin_panties = False
        $ haki_yamato_panties = False
        
        narrador "-1  [nami.n]'s panties | -1 [robin.n]'s panties | -1 [yamato.n]'s panties"

        rayleigh "Incredible!!!"
        rayleigh "(This one is even completely soaked with sweat!!)"
        rayleigh "I always trusted you... I knew you were special..."
        player "Hehe... I'm flattered, master..."
        rayleigh "Come on, come on... sit with me. We'll have the girls bring us something to drink."
        rayleigh "I'll teach you everything I know... You and I are going to do great things together!"
        narrador "And so... you manage to catch the attention of an old big shot... Who knows what fate has in store for you!"

        $ Haki.h = 6


    $ _window_hide()
    hide rayleigh with Dissolve(0.8)
    jump shells_town_bar