import unittest
from scoringDemo import ScoreMachine

class TestAce(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_zero(self):
        self.assertEqual(self.machine.aces([6,2,3,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.aces([1,2,3,4,5]), 1, "Should be 1")
        self.assertEqual(self.machine.aces([2,3,4,5,1]), 1, "Should be 1")
        self.assertEqual(self.machine.aces([1,1,1,0,1]), 5, "Should be 1")
    
    def test_two(self):
        self.assertEqual(self.machine.aces([1,2,1,4,5]), 2, "Should be 2")


if __name__ == '__main__':
    unittest.main()