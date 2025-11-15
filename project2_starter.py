"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Che Mullins]
Date: [Date]

AI Usage: [Assisted with self and super assignments within the code, also with inheritance structure and method overriding when it came to displaying stats]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
   
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        # TODO: Set the character's name, health, strength, and magic
        # These should be stored as instance variables
        self.name = name
        self.strength = strength
        self.health = health
        self.magic = magic
        
    def attack(self, target):
        damage = self.strength
        target.take_damage(damage)
        print(f"{self.name} attacks {self.name} for {damage} damage.")
       
        
    def take_damage(self, damage):
            self.health -= damage
            if self.health < 0:
                self.health = 0

                print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
      
       
        
    def display_stats(self):
       
    
        print(f"---{self.name}'s Stats ---")
        print(f"Strength: {self.strength}")
        print(f"Health: {self.health}")
        print(f"Magic: {self.magic}")

class Player(Character):
    
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.xp = 0
    


    def get_xp(self, amount):
        self.xp += amount
        if self.xp >= 100:
            self.level += 1
            self.xp -= 100
            self.health += 10
            self.strength += 2
            self.magic += 2
            print(f"{self.name} leveled up to level {self.level}!")

    def get_level(self):
        print(f"self.name} is at level {self.level}")
        
    def display_stats(self):
        super().display_stats()
        print(f"Level: {self.level}")
        print(f"Class: {self.character_class}")
        print(f"XP: {self.xp}")


class Warrior(Player):
  
    
    def __init__(self, name):

        super().__init__(name, "Warrior", 120, 15, 5)
        
    def attack(self, target):
        damage = self.strength + 5
        target.take_damage(damage)

        print(f"{self.name} performs a attack on {target.name} for {damage} damage.")
        
       
        
    def power_strike(self, target):
        damage = self.strength * 2
        target.take_damage(damage)
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage.")
        
        

class Mage(Player):
    
    def __init__(self, name):
        super().__init__(name, "Mage" 80, 8, 20)

    def attack(self, target):
        damage = self.magic
        target.take_damage(damage)
        print(f"{self.name} casts a spell on {target.name} for {damage} damage.")

    def fireball(self, target):
        damage = self.magic + 10
        target.take_damage(damage)
        print(f"{self.name} casts Fireball on {target.name} for {damage} damage.")


class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)
        
    def attack(self, target):
        import random
        if random.randint(1, 10) <= 3:
            damage = self.strength * 2
            target.take_damage(damage)
            print(f"{self.name} lands a CRITICAL HIT on {target.name} for {damage} damage!")
        else:
            damage = self.strength
            target.take_damage(damage)
            print(f"{self.name} lands a normal hit on {target.name} for {damage} damage.")
    
    def sneak_attack(self, target):
        damage = self.strength * 2
        target.take_damage(damage)
        print(f"{self.name} uses Sneak Attack on {target.name} for {damage} damage.")
        # Special rogue ability - guaranteed critical hit.


class Weapon:
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus
        # Create a weapon with a name and damage bonus.
        
    def display_info(self):
        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}")


# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    warrior.get_xp(120)
    warrior.get_level()
    warrior.display_stats()
    mage.get_xp(200)
    mage.get_level()
    mage.display_stats()
    rogue.get_xp(150)
    rogue.get_level()
    rogue.display_stats()
    
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)

    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
