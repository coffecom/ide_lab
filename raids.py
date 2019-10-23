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
