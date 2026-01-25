# Version event: 1
# Version game: 0.1

# Haki
define enemy_sarquiss = RPGEnemy(   name= 'Sarquiss', hp=200, mana=0, armor=2, magic_resist=2, 
                                    agility=1, defense=5, strength=4, power=0,
                                    base_damage=30, crit_chance=10, crit_damage=20,
                                    heals=0,
                                    abilities=[],
                                    image="enemy_sarquiss", exp = 40)

# Bounty Board
define enemy_alvida = RPGEnemy(   name= '[alvida_name]', hp=200, agility=1, defense=2, strength=1, base_damage=20, image="enemy_alvida", exp = 15)

define enemy_zala = RPGEnemy(   name= '[zala_name]', hp=240, agility=1, defense=2, strength=1, base_damage=25, image="enemy_zala", exp = 20)


# Thriller Bark
define enemy_cerberus = RPGEnemy(   name= 'Cerberus', hp=140, agility=3, defense=1, strength=1, base_damage=15, image="cerberus")

define enemy_ryuma = RPGEnemy(      name= 'Ryuma', hp=160, agility=3, defense=0, strength=1, base_damage=30, image="ryuma", exp = 30)

define enemy_zombie = RPGEnemy(     name= 'Zombie', hp=100, agility=0, defense=0, strength=1, base_damage=15, image="zombie")


# Black Drum
define enemy_lapahn = RPGEnemy(     name= 'Lapahn', hp=300, agility=0, defense=1, strength=1, base_damage=20, image="lapahn")


# Amazon Lily
define enemy_bacura = RPGEnemy(name='Bacura', hp=100, agility=1, defense=1, strength=1, base_damage=15, image="bacura", exp = 0)

define enemy_marguerite = RPGEnemy(name='[marguerite_name]', hp=200, agility=2, defense=2, strength=1, base_damage=15, image="enemy_marguerite", exp = 0)

define enemy_marigold = RPGEnemy(name='[marigold_name]', hp=200, agility=1, defense=3, strength=1, base_damage=15, image="enemy_marigold", exp = 0)

define enemy_marigold_v2 = RPGEnemy(name='[marigold_name]', hp=200, agility=1, defense=3, strength=2, base_damage=20, image="enemy_marigold_v2", exp = 40)

# Arabasta
define enemy_mr5 = RPGEnemy(name='Mr. 5', hp=260, agility=1, defense=2, strength=2, base_damage=35, image="enemy_mr5")

define enemy_dugong = RPGEnemy(name='Dugong', hp=200, agility=2, defense=2, strength=1, base_damage=15, image="dugong")

define enemy_sandoradragon = RPGEnemy(name='Sandora Dragon', hp=300, agility=2, defense=3, strength=2, base_damage=30, image="sandoradragon", exp = 20)

define enemy_bananawani = RPGEnemy(name='Bananawani', hp=400, agility=1, defense=4, strength=2, base_damage=40, image="bananawani", exp = 20)


define enemy_mr2 = RPGEnemy(   name= 'Mr. 2', hp=200, mana=0, armor=0, magic_resist=0, 
                                    agility=8, defense=2, strength=1, power=2,
                                    base_damage=30, crit_chance=5, crit_damage=10, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_mr2", exp = 25)


define enemy_mr1 = RPGEnemy(   name= 'Mr. 1', hp=250, mana=0, armor=10, magic_resist=2, 
                                    agility=2, defense=8, strength=3, power=1,
                                    base_damage=35, crit_chance=5, crit_damage=10, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_mr1", exp = 30)

define enemy_mr0 = RPGEnemy(   name= 'Crocodile', hp=300, mana=120, armor=8, magic_resist=8, 
                                    agility=5, defense=2, strength=4, power=8,
                                    base_damage=40, crit_chance=15, crit_damage=20, 
                                    heals=2, 
                                    abilities=["Desert spada", "Sables"],
                                    image="boss_crocodile", exp = 100)

image boss_crocodile = ConditionSwitch(
                                    "enemy_figth.hp <= enemy_figth.max_health*0.25", "enemy_crocodile_w2",
                                    "enemy_figth.hp <= enemy_figth.max_health*0.5", "enemy_crocodile_w1",
                                    True,"enemy_crocodile",)

# Elegia
define enemy_kaginote = RPGEnemy(   name= 'Kaginote', hp=250, mana=0, armor=0, magic_resist=0, 
                                    agility=8, defense=2, strength=3, power=0,
                                    base_damage=30, crit_chance=15, crit_damage=10, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_kaginote", exp = 35)


define enemy_hanagasa = RPGEnemy(   name= 'Hanagasa', hp=400, mana=0, armor=0, magic_resist=0, 
                                    agility=0, defense=2, strength=3, power=0,
                                    base_damage=35, crit_chance=5, crit_damage=10, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_hanagasa", exp = 45)

define enemy_eboshi = RPGEnemy(   name= 'Eboshi', hp=300, mana=0, armor=0, magic_resist=0, 
                                    agility=2, defense=2, strength=5, power=0,
                                    base_damage=40, crit_chance=15, crit_damage=20, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_eboshi", exp = 60)
                                    
# Dressrosa

define enemy_sai = RPGEnemy(   name= 'Sai', hp=300, mana=0, armor=0, magic_resist=0, 
                                    agility=4, defense=2, strength=8, power=0,
                                    base_damage=40, crit_chance=20, crit_damage=10, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_sai", exp = 60) 



define enemy_spartan = RPGEnemy(   name= 'Spartan', hp=200, mana=0, armor=0, magic_resist=0, 
                                    agility=2, defense=3, strength=5, power=0,
                                    base_damage=40, crit_chance=20, crit_damage=10, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_spartan", exp = 60)

define enemy_lepanto = RPGEnemy(   name= 'Lepanto', hp=350, mana=0, armor=0, magic_resist=0,
                                    agility=2, defense=2, strength=9, power=0,
                                    base_damage=40, crit_chance=30, crit_damage=30, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_lepanto", exp = 75) 

define enemy_gilly = RPGEnemy(   name= 'Gilly', hp=300, mana=0, armor=5, magic_resist=0,
                                    agility=5, defense=5, strength=12, power=0,
                                    base_damage=40, crit_chance=30, crit_damage=30, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_gilly", exp = 75)

define enemy_ideo = RPGEnemy(   name= 'Ideo', hp=350, mana=0, armor=4, magic_resist=4,
                                    agility=5, defense=4, strength=15, power=0,
                                    base_damage=55, crit_chance=30, crit_damage=45, 
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_ideo", exp = 90) 

#enemy_logan
define enemy_logan = RPGEnemy(   name= 'Logan', hp=450, mana=0, armor=5, magic_resist=5,
                                    agility=3, defense=5, strength=17, power=0,
                                    base_damage=60, crit_chance=25, crit_damage=55, 
                                    heals=0, 
                                    abilities=[],
                                    image="boss_logan", exp = 100) # LVL 3 - strength 25 (despues de derrotarlo subis a nivel 3 - 430xp)

image boss_logan = ConditionSwitch( "enemy_figth.hp <= enemy_figth.max_health*0.25", "enemy_logan_w2",
                                    "enemy_figth.hp <= enemy_figth.max_health*0.5", "enemy_logan_w1",
                                    True,"enemy_logan",)


define enemy_chinjao = RPGEnemy(   name= 'Chinjao', hp=500, mana=0, armor=4, magic_resist=4,
                                    agility=3, defense=3, strength=17, power=0,
                                    base_damage=60, crit_chance=25, crit_damage=55,
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_chinjao", exp = 100) # LVL 3 - strength 30 justo (despues de derrotarlo subis a nivel 4 - 550xp)


define enemy_dellinger = RPGEnemy(   name= 'Dellinger', hp=250, mana=0, armor=3, magic_resist=3,
                                    agility=6, defense=4, strength=25, power=0,
                                    base_damage=65, crit_chance=30, crit_damage=60,
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_dellinger", exp = 80) # LVL 3 - strength 30 


define enemy_machvise = RPGEnemy(   name= 'Machvise', hp=450, mana=0, armor=3, magic_resist=3,
                                    agility=4, defense=3, strength=15, power=20,
                                    base_damage=20, crit_chance=20, crit_damage=50,
                                    heals=0, 
                                    abilities=[],
                                    image="enemy_machvise", exp = 80) 

define enemy_diamante = RPGEnemy(   name= 'Diamante', hp=550, mana=120, armor=3, magic_resist=3,
                                    agility=2, defense=3, strength=20, power=20,
                                    base_damage=70, crit_chance=20, crit_damage=60,
                                    heals=0, 
                                    abilities=["Death Swarm", "Half Moon Glaive"],
                                    image="boss_diamante", exp = 200)

image boss_diamante = ConditionSwitch( "enemy_figth.hp <= enemy_figth.max_health*0.25", "enemy_diamante_w2",
                                    "enemy_figth.hp <= enemy_figth.max_health*0.5", "enemy_diamante_w1",
                                    True,"enemy_diamante",)

#image boss_diamante = ConditionSwitch(
#                                    "enemy_figth.hp <= enemy_figth.max_health*0.25", "enemy_diamante_w2",
#                                    "enemy_figth.hp <= enemy_figth.max_health*0.5", "enemy_diamante_w1",
#                                    True,"enemy_diamante",)

# player_level
# Strength
# player_exp
# EXP [0, 60, 150, 300, 600, 1200]

# Dessrosa - Fight Coliseum
# spartan (lvl 1 - strength 1) 0+60=60-60= 0 exp - Subio lvl 2
# lepanto (lvl 2 - strength 8) - 0+75= 75 exp - (entreno +7) (muy justo - 1 error)
# gilly (lvl 2 - strength 8) - 75+75=150-150= 0 exp - subio lvl 3 -(muy justo - 1 error)
# ideo (lvl 3 - strength 12) - 0+90 = 90 exp - lvl 3 - (entreno +4) (muy justo - 3 error)
# logan (lvl 3 - strength 20) - 90+100 = 190 exp - lvl 3 - (entreno +8) (muy justo - 1 error)
# chinjao (lvl 3 - strength 24) - 190+100 = 290 exp - lvl 3 - (entreno +4) (muy justo - 1 error)
# dellinger (lvl 3 - strength 24) - 290+80=370-300 = 70 exp - subio lvl 5
# machvise (lvl 4 - strength 24) - 70+80 = 150 exp
# diamante (lvl 4 - strength 24) 