from character import Team, Weapon, Character_status, Hero, Hero_class, Race
class Easy_raid(object):
    def __init__(self, team, k = 1):
        self.team = team
        self.creeps_amount = 50  * k
        self.creeps_damage = 2 * k
        self.creeps_hp = 5 * k
        self.creeps_xp = 1 * k
        self.boss_hp = 100 * (2 * k)
        self.boss_damage = 7 * (2 * k)
        self.boss_xp = 10 * (2 * k)

    def enter_the_dungeon(self):
        creeps_hp = self.creeps_amount * self.creeps_hp
        creeps_alive = True
        while (creeps_alive):
            for member in self.team.members:
                if member.status == Character_status.ALIVE:
                    creeps_hp -= (member.atack + member.weapon.value)
                    member.take_damage(self.creeps_damage)
            if self.team.is_anyone_alive == False: return False
            if creeps_hp <= 0:
                creeps_alive = False
        boss_alive = True
        while(boss_alive):
            for member in self.team.members:
                if member.status == Character_status.ALIVE:
                    self.boss_hp -= (member.atack + member.weapon.value)
                    member.take_damage(self.boss_damage)
                if self.team.is_anyone_alive == False: return False
                if self.boss_hp <= 0:
                    boss_alive = False
        for member in self.team.members:
            member.xp+= self.creeps_amount*self.creeps_xp + self.boss_xp
        return True

class Three_bosses_raid(object):
    def __init__(self, team, k = 1):
        self.team = team
        self.boss1_hp = 100 * (2 * k)
        self.boss1_damage = 7 * (2 * k)
        self.boss1_xp = 8 * (2 * k)
        self.boss2_hp = 150 * (2 * k)
        self.boss2_damage = 9 * (2 * k)
        self.boss2_xp = 12 * (2 * k)    
        self.boss3_hp = 200 * (2 * k)
        self.boss3_damage = 4 * (2 * k)
        self.boss3_xp = 12 * (2 * k)
    
    
    def enter_the_dungeon(self):
        """Enters dungeon and add xp if win
        
        Returns:
            boolean -- pass or not
        """
        boss_alive = True
        while(boss_alive):
            for member in self.team.members:
                if member.status == Character_status.ALIVE:
                    self.boss1_hp -= (member.atack + member.weapon.value)
                    member.take_damage(self.boss1_damage)
                    self.boss2_hp -= (member.atack + member.weapon.value)
                    member.take_damage(self.boss2_damage)
                    self.boss3_hp -= (member.atack + member.weapon.value)
                    member.take_damage(self.boss3_damage)
                if self.team.is_anyone_alive == False: return False
                if self.boss1_hp+self.boss2_hp+self.boss3_hp <= 0:
                    boss_alive = False
        for member in self.team.members:
            member.xp+= self.boss1_xp*self.boss2_xp + self.boss3_xp
        return True

class Dice():
    def __init__(self, n_sides):
        self.n_sides = n_sides

    def roll_dice(self):
        from random import randrange
        return randrange(self.n_sides)