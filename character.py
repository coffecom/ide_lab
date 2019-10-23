from enum import Enum
import random

class Race(Enum):
    HUMAN = 'Human'
    ELF = 'Elf'
    GNOME = 'Gnome'
    ORC = 'Orc'
    GREMLIN = 'Gremlin'

class Hero_class(Enum):
    MAGE = 'Mage'
    WARRIOR = 'Warrior'
    PRIEST = 'Priest'
    PALADIN = 'Paladin'
    FIGHTER = 'Fighter'

class Weapon(Enum):
    SWORD = 2
    NOTHING = 0
    BOW = 1
    DAGGER = 3
    STAFF = 2
    AXE = 2.5

class Character_status(Enum):
    ALIVE = 1
    DEAD = 0

class Character(object):
    def __init__(self, name, hp, race = Race.HUMAN):
        self.name = name
        self.hp = hp
        self.race = race

        self.level = 1
        self.status = Character_status.ALIVE
        self.attack = 10
        self.xp = 0
    
    def __str__(self):
        return self.status.name +' ' + self.race.value + ' ' + self.name + ' ' + str(self.hp) +' hp'

    def check_status(self):
        if self.hp <= 0:
            self.hp = 0
            self.status = Character_status.DEAD

    def take_damage(self, damage):
        """Decreases hp
        
        Arguments:
            damage {int} -- value of damage to character
        """
        self.hp-=damage
        self.check_status
    
    def restore_hp(self, value):
        self.hp+=value

    def suicude(self):
        self.hp = 0
        if self.hp <= 0:
            self.hp = 0
            self.status = Character_status.DEAD  

    def get_characteristics(self):
         return "LEVEL: " + str(self.level) + "\nHP: " + str(self.hp) 

    def level_up(self):
        if self.status == Character_status.DEAD or self.xp < 10:
            return
        self.xp -= 10
        self.level += 1
        self.attack += 2
        self.level_up()   
    
    def go_hunt(self):
        random.seed()
        luck = random.random()
        print('Somedays you hunt, somedays you are hunt. Luck: ' + str(round(luck,3)))
        self.hp -= round(self.hp * luck)
        self.check_status
        if self.status == Character_status.ALIVE:
            self.xp += int(luck*10)



class Hero(Character):
    def __init__(self, name, hp, race = Race.HUMAN, hero_class = Hero_class.FIGHTER):
        super().__init__(name, hp, race)
        self.hero_class = hero_class

        self.weapon = Weapon.NOTHING
        self.mana = 10

    def __str__(self):
        return self.status.name + ' ' + self.race.value + ' ' + self.hero_class.value + ' with '+ self.weapon.name + ', '+ str(self.level) +' level, name ' + self.name + ' ' + str(round(self.hp,3)) +' hp'
        
    def attack_enemy(self, enemy, damage):
        print(self.name+' attacks '+enemy.name+'!')
        enemy.take_damage(self.attack + self.weapon.value)
    
    def take_weapon(self, weapon):
        self.weapon = weapon
    
    def use_easy_skill(self, character):
        if self.mana >= 1:
            self.mana -= 1
            character.hp -= 2
        else:
            print('No mana') 

    def use_normal_skill(self, character):
        if self.mana >= 5:
            self.mana -= 5
            character.hp -= 8
        else:
            print('No mana')

class Team(object):
    def __init__(self, name):
        self.name = name 
        self.members = []

    def add_member(self, character):
        self.members.append(character)
    
    def heal_member(self, member, value):
        self.members[self.members.index(member)].hp += value

    def damage_member(self, member, value):
        self.members[self.members.index(member)].hp -= value
        self.members[self.members.index(member)].check_status

    def level_up_everyone(self):
        for member in self.members:
            member.level_up()

    def __str__(self):
        string = 'TEAM: \n'
        for member in self.members:
            string += member.__str__+"\n"
        return string

    def get_detailed_inf(self):
        string = 'TEAM: \n'
        for member in self.members:
            string += member.__str__+" attack: "+member.attack+" xp: "+member.xp+"\n"
        return string
        
    def get_short_inf(self):
        string = 'TEAM: \n'
        for member in self.members:
            string += member.name+" attack: "+ member.attack + " hp: " + member.hp  + "\n"
        return string
    
    def remove_all_dead_members(self):
        for member in self.members:
            if member.status.value == 0:
                self.members.remove(member)
                
    def damage_everyone(self, value):
        for member in self.members:
            member.hp -= value
            member.check_status
            
    def heal_member(self, member, value):
        self.members[self.members.index(member)].hp += value



# maya = Hero("Maya", 20, Race.ELF, Hero_class.MAGE)
# stieve = Hero("Stieve", 30, Race.GNOME, Hero_class.PALADIN)
# maya.level_up()
# # maya.take_damage("hello")
# maya.take_weapon(Weapon.STAFF)
# team = Team("Rocket")
# team.add_member(maya)
# team.add_member(stieve)
# team.damage_member(maya, 10)
# maya.attack(stieve,20)
# maya.suicude()
# print(maya)
# print(stieve)