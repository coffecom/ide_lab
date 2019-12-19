import unittest
# import main/
import sys
from character import Character, Character_status, Hero, Hero_class, Race

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("John", 20)
    
    def test_take_damage_exception(self):
        with self.assertRaises(TypeError):
            self.character.take_damage("damage")

        

class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Anna", 20, Race.GREMLIN, Hero_class.PALADIN)
        self.enemy = Hero("Clay", 20, Race.HUMAN, Hero_class.MAGE)
    
    def test_use_normal_skill(self):
        self.hero.use_normal_skill(self.enemy)
        self.assertEqual(self.hero.mana, 5)
		

test1 = TestCharacter()
test1.setUp()
test1.test_take_damage_exception()

test2 = TestHero()
test2.setUp()
test2.test_use_normal_skill()
