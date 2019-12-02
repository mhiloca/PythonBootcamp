import unittest
from robot import Robot


class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("mega man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            'BEEP BOOP BEEP BOOP. My name is MEGA MAN'
        )
        self.assertEqual(self.mega_man.battery, 49)




if __name__ == '__main__':
    unittest.main()