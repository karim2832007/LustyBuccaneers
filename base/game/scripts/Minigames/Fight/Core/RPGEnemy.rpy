# Version event: 1
# Version game: 0.23

default enemy_figth = RPGEnemy()

init -1 python:
    import random

    class RPGEnemy(RPGCharacter):
        """Clase de Enemigo que maneja sus propias estadísticas, heredando de RPGCharacter."""

        def __init__(self, image="none", name="", hp=100, mana=0, armor=0, magic_resist=0, 
                        agility=3, defense=3, strength=4, power=4, base_damage=15,
                        crit_chance=5, crit_damage=10, heals=0, exp=10, abilities=None, buffs=None):

            # 📌 Asignar estadísticas propias del enemigo
            self.name = name  
            self.image = image  
            self.hp = self.max_health = hp  
            self.mana = self.max_mana = mana  
            self.armor = armor  
            self.magic_resist = magic_resist  
            self.agility = agility
            self.defense = defense  
            self.base_damage = base_damage
            self.strength = strength  
            self.power = power  
            self.crit_chance = crit_chance  
            self.crit_damage = crit_damage  
            self.heals = self.max_heals = heals  
            self.exp = exp

            self.abilities = [ABILITIES[ability] for ability in (abilities or []) if ability in ABILITIES] 
            self.buffs = buffs or []
            self.action = "none"

            # 📌 Llamamos al constructor de RPGCharacter para inicializar métodos
            #super().__init__()

        @property
        def n(self):#"#2b221b"
            return renpy.substitute(str(self.name))

        def attack(self, attack_type="physical", ability_damage=0, multiplier=1):
            """El enemigo realiza un ataque (físico o mágico)."""
            damage, criti_attack = super().attack(
                base_damage=self.base_damage,
                strength=self.strength,
                power=self.power,
                attack_type=attack_type,
                crit_chance=self.crit_chance,
                crit_damage=self.crit_damage,
                multiplier=multiplier
            )
            
            damage += ability_damage  # Agregar daño de habilidades si es necesario

            return damage, criti_attack

        def take_damage(self, damage, damage_type="physical", ):
            if self.dodge():
                return f"{self.n} dodged the attack."

            """El enemigo recibe daño y actualiza su HP."""
            damage_taken = super().take_damage(
                damage=damage,
                damage_type=damage_type,
                armor=self.armor,
                magic_resist=self.magic_resist,
                defense=self.defense,
                agility=self.agility
            )

            #for i in range(damage_taken):
            #    if self.hp <= 0:
            #        break
            #    self.hp -= 1
            #    renpy.pause(max(0.00005, 0.01 * (0 - (i / damage_taken)))) 

            animate_bar("hp", 0, self.max_health, -damage_taken, obj_ref=self)


            #self.hp = max(0, self.hp - damage_taken)  # Reducir vida
            return f"{self.n} takes {damage_taken} points of damage {damage_type}." 

        def dodge(self):
            global Agility

            """Determina si el ataque impacta considerando la diferencia de agilidad."""
            agility_difference = max(1, self.agility - Agility)

            # 📌 Nueva fórmula que crece rápido hasta 50% y luego se suaviza
            evasion_chance = 80 * (agility_difference / (30 + abs(agility_difference)))
            evasion_chance = max(0, min(100, evasion_chance))  # Limita entre 0% y 100%

            return random.uniform(0, 100) < evasion_chance  # true - el ataque es esquivado

        def use_ability(self):
            """Elige y usa una habilidad si tiene maná suficiente."""
            available_abilities = [ability for ability in self.abilities if self.mana >= ability.mana_cost]

            if available_abilities:
                ability = random.choice(available_abilities)

                animate_bar("mana", 0, self.max_mana, -ability.mana_cost, obj_ref=self)
                #self.mana -= ability.mana_cost

                return ability #.name, ability.attack_type  # Retorna daño, nombre y tipo

            return None

        def heal(self):
            self.hp, heal_amount = super().heal(self.hp, self.max_health)
            self.heals -= 1
            return heal_amount

        def decide_action(self):
            """El enemigo decide su acción en combate."""
            action_type = None
            details = {}  # 📌 Diccionario para almacenar datos de la acción

            if self.should_heal():
                self.action = "heal"
                heal_amount = self.heal()
                action_type = "heal"
                details = {"heal_amount": heal_amount}
                talk = f"{self.n} healed {heal_amount} points of damage."

            #elif self.should_use_buff():
            #    self.action = "buff"
            #    buff = self.use_buff()
            #    action_type = "buff"
            #    details = {"buff": buff}
            #    talk = f"{self.n} usa {buff} para fortalecerse."
            #
            #elif self.should_defend():
            #    self.action = "defend"
            #    self.defend()
            #    action_type = "defend"
            #    talk = f"{self.n} adopta una postura defensiva."

            elif self.should_use_ability():
                self.action = "attack"
                #damage, ability_name, attack_type = self.use_ability()
                ability = self.use_ability()
                
                damage, crit_attack = self.attack(attack_type=ability.attack_type, ability_damage=ability.damage, multiplier=ability.multiplier)
                action_type = "attack"
                details = {
                    "damage": damage,
                    "damage_type": ability.attack_type,
                    "crit_attack": crit_attack,
                    "ability_name": ability.name,
                    "image": ability.image
                }
                talk = f"{self.n} uses {ability.name}."

            else:
                damage, crit_attack = self.attack()
                self.action = "attack"
                action_type = "attack"
                details = {
                    "damage": damage,
                    "damage_type": "physical",
                    "crit_attack": crit_attack,
                }
                talk = f"{self.n} attacks you physically"

            return talk, action_type, details

    
        def should_heal(self):
            """Decide si el enemigo debe curarse basado en su vida."""
            if self.hp < self.max_health * 0.3 and self.heals > 0:
                return random.random() < (0.5 if self.heals < 5 else 0.75)
            return False

        def should_use_ability(self):
            """Elige y usa una habilidad si tiene maná suficiente."""
            usable_abilities = [ability for ability in self.abilities if self.mana >= ability.mana_cost]

            """Decide si el enemigo usa una habilidad en lugar de un ataque físico."""
            return  bool(usable_abilities) and random.random() < 0.7 # bool(self.abilities) and

        def reset(self, hp_porcent = 1):
            """Reinicia las estadísticas del enemigo a sus valores iniciales."""
            self.hp = int(self.max_health * hp_porcent)
            self.mana = self.max_mana
            self.heals = self.max_heals 
            self.buffs = []

        def is_dead(self):
            """Determina si el enemigo está muerto basado en su vida."""
            return self.hp <= 0
