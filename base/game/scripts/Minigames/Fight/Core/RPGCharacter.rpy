# Version event: 1
# Version game: 0.23
init -1 python:
    import random
    
    class RPGCharacter:
        """Clase con métodos de cálculo para combate y defensa."""
        
        @staticmethod
        def take_damage(damage, damage_type, armor, magic_resist, defense, agility):            
            if damage_type == "physical":
                damage_taken = max(0, damage * (100 / (100 + armor)) * (100 / (100 + defense)))
            elif damage_type == "magic":
                damage_taken = max(0, damage * (100 / (100 + magic_resist)) * (100 / (100 + defense)))
            else:
                damage_taken = damage  

            return int(damage_taken)

        @staticmethod
        def attack(base_damage, strength=0, power=0, attack_type="physical", crit_chance=0, crit_damage=0, multiplier=1):
            """Calcula el daño de ataque basado en fuerza o poder."""
            if attack_type == "physical":
                damage = base_damage + strength * multiplier
            elif attack_type == "magic":
                damage = base_damage + power * multiplier
            else:
                damage = base_damage  # Si no se especifica, usa solo `base_damage`

            # Cálculo de crítico
            crit_attack = False
            if random.random() < (crit_chance / 100):
                damage = int(damage * (1 + crit_damage / 100))
                crit_attack = True

            return damage, crit_attack

        @staticmethod
        def heal(hp, max_hp, heal_amount=50, min_heal=0):
            """Cura una cantidad de HP, con opción de variabilidad."""
            if min_heal > 0:
                heal_amount = random.randint(min_heal, heal_amount)  # Cura aleatoria

            new_hp = min(max_hp, hp + heal_amount)
            return new_hp, heal_amount
            
        def reset(self):# Reinicia la salud, maná y estado del enemigo.
            self.hp = self.true_hp_max()
            self.mana = self.true_mana_max()
            self.is_alive = True

        def is_dead(self):# Devuelve True si el enemigo ha muerto.
            return self.hp <= 0
