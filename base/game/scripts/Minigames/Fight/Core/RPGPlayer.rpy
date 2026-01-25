# Version event: 2
# Version game: 0.39

# Base Player
define player_armor = 3
define player_magic_resist = 3
define player_crit_chance = 0
define player_crit_damage = 50

define player_abilities = [
    ("Strong attack", "True"), 
    ("Armament Punch", "armament_punch")
]

define player_exp_lvl = [0, 60, 150, 300, 600, 1200, 1500]

define player_hp_max_lvl  = [300, 420, 540, 660, 880, 1000, 1120] # +120
define player_mana_max_lvl  = [100, 125, 150, 175, 200, 225, 250] # +25

define player_health_max = 300 #obsolet
define player_mana_max = 100 #obsolet

# Create Player
define RPGPlayer = RPGPlayer()

# Level
default player_level = 1
default player_exp = 0

# Stats Base
default player_hp = player_hp_max_lvl[0]
default player_mana = player_mana_max_lvl[0]

# Stats Basic
default Strength      = 0
default Defense       = 0
default Agility       = 0
default Intelligence  = 0

# Stats Special 
default Charisma  = 0
default Cooking   = 0
default Aim       = 0

# Stats Rare
default Luck = 0

# OBJECTIVE = Pirate, Swordsman, Harem, King
default player_goal = "none" 

# haki
default player_haki = 0

init -1 python:
    class RPGPlayer(RPGCharacter):
        """Clase del jugador que usa solo variables globales."""

        def attack(self, attack_type="physical", ability_damage=0, multiplier=1):
            """Realiza un ataque y devuelve el daño causado."""
            damage, criti_attack = super().attack(
                base_damage = 20,  # Daño base del jugador
                strength    = Strength,
                power       = Intelligence,  # Inteligencia usada para magia
                attack_type = attack_type,
                crit_chance = player_crit_chance,  # Probabilidad de crítico
                crit_damage = player_crit_damage,
                multiplier  = multiplier
            )
            
            damage += ability_damage  # Agregar daño de habilidades si es necesario

            return damage, criti_attack

        def take_damage(self, damage, damage_type="physical"):
            """Recibe daño y actualiza player_hp."""
            global player_hp, player_guard  # Modificamos directamente la variable global

            damage_taken = super().take_damage(
                damage=damage,
                damage_type=damage_type,
                armor= self.true_armor(),  
                magic_resist=self.true_magic_resist(),  
                defense=Defense,
                agility=Agility,
            )

            if player_guard:
                damage_taken = int(damage_taken * 0.5)
                player_guard = False

            animate_bar("player_hp", 0, self.true_hp_max(), -damage_taken)

            #player_hp = max(0, player_hp - damage_taken)  # Reducir vida del jugador
            return f"You take {damage_taken} points of damage {damage_type}."

        def dodge(self, attacker_agility):
            global Agility

            """Determina si el ataque impacta considerando la diferencia de agilidad."""
            agility_difference = max(1, Agility - attacker_agility)

            # 📌 Nueva fórmula que crece rápido hasta 50% y luego se suaviza
            evasion_chance = 80 * (agility_difference / (25 + abs(agility_difference)))
            evasion_chance = max(0, min(100, evasion_chance))  # Limita entre 0% y 100%
            print(f"Player evasion_chance: {evasion_chance}")

            return random.uniform(0, 100) < evasion_chance  # true - el ataque es esquivado


        def heal(self, heal_amount=50, min_heal=0, mana_amount=0):
            """Se cura y actualiza player_hp."""
            global player_hp  # Modificamos directamente la variable global

            # Curar al jugador y obtener la cantidad curada
            _, heal_amount = super().heal(player_hp, self.true_hp_max(), heal_amount, min_heal)

            animate_bar("player_hp", 0, self.true_hp_max(), heal_amount)

            if (mana_amount > 0):
                animate_bar("player_mana", 0, self.true_mana_max(), mana_amount)

            return f"You healed {heal_amount} health points."
    
        def full_heal(self):
            #global player_hp, player_mana  # Modificamos directamente las variables globales

            animate_bar_background("player_hp", 0, self.true_hp_max(), self.true_hp_max())
            animate_bar_background("player_mana", 0, self.true_mana_max(), self.true_mana_max())

            return "You have been fully healed!"

        def run(self):
            if renpy.random.choice([True, True, True, False]):
                return True
            else:
                return False

        def use_ability(self, ability_key):
            global player_mana

            ability = ABILITIES[ability_key]

            animate_bar("player_mana", 0, self.true_mana_max(), -ability.mana_cost)

            return ability.damage, ability #.name, ability.attack_type  # Retorna daño, nombre y tipo

        def hp(self):
            """Devuelve la vida actual del jugador."""
            return player_hp

        def mana(self):
            """Devuelve la mana actual del jugador."""
            return player_mana
    
        def true_hp_max(self):
            """Devuelve la armadura del jugador."""
            global player_hp_max_lvl, player_level
            return player_hp_max_lvl[player_level-1]
        
        def true_mana_max(self):
            """Devuelve la mana actual del jugador."""
            global player_mana_max_lvl, player_level
            return player_mana_max_lvl[player_level-1]

        def true_armor(self):
            """Devuelve la armadura del jugador."""
            global player_armor, player_level
            return player_armor+(player_level*2)

        def true_magic_resist(self):
            """Devuelve la armadura del jugador."""
            global player_magic_resist, player_level
            return player_magic_resist+(player_level*2)

        def sleep(self):
            """Mana del jugador al dormir."""
            global player_mana  # Modificamos directamente las variables globales
            player_mana = self.true_mana_max()
            #animate_bar("player_mana", 0, self.true_mana_max(), self.true_mana_max())

        def reset(self):
            """Reinicia la salud y estado del jugador."""
            global player_hp, player_mana  # Modificamos directamente las variables globales

            player_hp = self.true_hp_max()
            player_mana = self.true_mana_max()

        def is_dead(self):
            """Devuelve True si el jugador ha muerto."""
            return player_hp <= 0


        def add_stat(self, stat, amount):
            """Añade puntos a una estadística del jugador."""
            global Strength, Defense, Agility, Intelligence, Charisma, Cooking, Aim, Luck

            if stat == "Strength":
                Strength += amount
            elif stat == "Defense":
                Defense += amount
            elif stat == "Agility":
                Agility += amount
            elif stat == "Intelligence":
                Intelligence += amount
            elif stat == "Charisma":
                Charisma += amount
            elif stat == "Cooking":
                Cooking += amount
            elif stat == "Aim":
                Aim += amount
            elif stat == "Luck":
                Luck += amount

            return f"¡Has aumentado tu {stat} en {amount} puntos!"

        def get_stat(self, stat):
            """Devuelve el valor de una estadística del jugador."""
            if stat == "Strength":
                return Strength
            elif stat == "Defense":
                return Defense
            elif stat == "Agility":
                return Agility
            elif stat == "Intelligence":
                return Intelligence
            elif stat == "Charisma":
                return Charisma
            elif stat == "Cooking":
                return Cooking
            elif stat == "Aim":
                return Aim
            elif stat == "Luck":
                return Luck

        def set_goal(self, goal):
            """Establece el objetivo del jugador."""
            global player_goal

            player_goal = goal
            return f"¡Tu nuevo objetivo es ser un {goal}!"

        def get_goal(self):
            """Devuelve el objetivo actual del jugador."""
            return player_goal

        def cover(self):
            """Cubre al jugador y reduce el daño recibido."""
            global player_guard 

            player_guard = True
            return "¡Te has cubierto!"

        # Level
        def add_exp(self, amount):
            global player_exp, player_level

            max_level = len(player_exp_lvl)
            start_level = player_level
            player_exp += amount

            # Subir niveles mientras tenga experiencia suficiente
            while player_level < max_level and player_exp >= player_exp_lvl[player_level]:
                self.level_up()

            # Si no subió ningún nivel
            if player_level == start_level:
                if player_level < max_level:
                    exp_needed = player_exp_lvl[player_level] - player_exp
                    return f"Next Level in: {exp_needed} EXP"
                else:
                    return f"Max Level Reached!"

            # Si subió de nivel
            else:
                self.reset()

                if player_level == max_level:
                    return f"Level Up! Level {start_level} >> {player_level}\nMax Level Reached!"
                else:
                    exp_needed = player_exp_lvl[player_level] - player_exp
                    return f"Level Up! Level {start_level} >> {player_level}\nNext Level in {exp_needed} EXP"

        def level_up(self):
            global player_exp, player_level

            max_level = len(player_exp_lvl)
            if player_level < max_level:
                player_exp -= player_exp_lvl[player_level]
                player_level += 1
                
