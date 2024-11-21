class Character:
     
    #Get Init for Character
    def __init__(self, name, type, clan, cooldown = 10, level = 1, health = 100):
         self.name = name
         self.type = type
         self.clan = clan
         self.cooldown = cooldown
         self.level = level
         self.health = health
         self.current_xp = 0
         self.xp_to_next_level = 10
     
    # Display Information
    def character_information(self):
        print(f"Name: {self.name}, Type: {self.type}, Clan: {self.clan}, Level: {self.level}, HP: {self.health}")
        
    # Level Up   
    def gain_xp(self, xp):
        self.current_xp += xp
        self.check_level_up()
    
    def check_level_up(self):
        while self.current_xp >= self.xp_to_next_level:
            self.current_xp -= self.xp_to_next_level
            self.level += 1
            self.xp_to_next_level += 5
            print(f"{self.name} has leveled up! Current Level: {self.level}")
            self.level_up_stats()

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Reamining health is: {self.health}")
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")
    
    # Cooldown
    def update_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1
            
    # Level Up
    def level_up_stats(self):
        pass # Use later
            
# Class for Assasin
class Zed(Character):
    
    # Get Init for Zed
    def __init__(self, name, clan = "Shadow", level = 1):
        self.name = name
        self.type = "Assasin"
        self.cooldown = 10
        self.clan = clan
        self.level = level
        self.current_xp = 0
        self.xp_to_next_level = 10
        self.health = 100
        self.attack_damage = 15
    
    # Zed Attack Damage
    def attack(self, target):
        damage = self.attack_damage
        target.take_damage(self.attack_damage)
        print(f"{self.name} attacked {target.name} and dealt {damage} damage!")
        
    def use_ability(self, target):
        ability_damage = 30
        print(f"{self.name} uses a dart that deals on {target.name}!")
        target.take_damage(ability_damage)
    
    # Level Up
    def level_up_stats(self):
        print(f"{self.name} has increased health and damage!")
        self.health += 20
        self.attack_damage += 5
        
# Class for Leblanc
class Leblanc(Character):
    
    # Get Init for Leblance
    def __init__(self, name, clan = "Black Rose", level = 1):
        self.name = name
        self.type = "Mage"
        self.cooldown = 10
        self.clan = clan
        self.level = level
        self.current_xp = 0
        self.xp_to_next_level = 10
        self.health = 100
        self.spell_power = 20
        
    # Attack
    def attack(self, target):
        damage = self.spell_power
        target.take_damage(self.spell_power)
        print(f"{self.name} attacked {target.name} and dealt {damage} damage!")
    
    # Use Ability
    def use_ability(self, target):
        ability_damage = 10 + self.spell_power
        target.take_damage(ability_damage)
        print(f"{self.name} uses tranformation to damage {target.name}!")
        
    def level_up_stats(self):
        self.health += 10
        self.spell_power += 15
        print(f"{self.name} has increased health and magic power!")
    

# Output
zed = Zed(name = "Zed")
leblance = Leblanc(name = "Leblance")

zed.character_information()
leblance.character_information()

zed.attack(leblance)
leblance.attack(zed) 

zed.gain_xp(12)
leblance.gain_xp(20)

zed.character_information()
leblance.character_information()




