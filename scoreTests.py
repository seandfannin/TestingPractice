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

class TestTwos(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()
        
    def test_zero(self):
        self.assertEqual(self.machine.twos([6,1,3,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.twos([1,2,3,4,5]), 1, "Should be 1")
        self.assertEqual(self.machine.twos([2,3,4,5,1]), 1, "Should be 1")
        self.assertEqual(self.machine.twos([2,2,2,5,2]), 5, "Should be 1")
    
    def test_two(self):
        self.assertEqual(self.machine.twos([2,2,1,4,5]), 2, "Should be 2")


class TestThrees(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()
        
    def test_zero(self):
        self.assertEqual(self.machine.threes([6,1,3,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.threes([1,2,3,4,5]), 1, "Should be 1")
        self.assertEqual(self.machine.threes([2,3,4,5,1]), 1, "Should be 1")
        self.assertEqual(self.machine.threes([2,2,2,5,2]), 5, "Should be 1")
    
    def test_two(self):
        self.assertEqual(self.machine.threes([2,2,1,4,5]), 2, "Should be 2")


class TestFours(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()
        
    def test_zero(self):
        self.assertEqual(self.machine.fours([6,1,3,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.fours([1,2,3,4,5]), 1, "Should be 1")
        self.assertEqual(self.machine.fours([2,3,4,5,1]), 1, "Should be 1")
        self.assertEqual(self.machine.fours([2,2,2,5,2]), 5, "Should be 1")
    
    def test_two(self):
        self.assertEqual(self.machine.fours([2,2,1,4,5]), 2, "Should be 2")


class TestFives(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()
        
    def test_zero(self):
        self.assertEqual(self.machine.fives([6,1,3,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.fives([1,2,3,4,5]), 1, "Should be 1")
        self.assertEqual(self.machine.fives([2,3,4,5,1]), 1, "Should be 1")
        self.assertEqual(self.machine.fives([2,2,2,5,2]), 5, "Should be 1")
    
    def test_two(self):
        self.assertEqual(self.machine.fives([2,2,1,4,5]), 2, "Should be 2")


class TestSixes(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()
        
    def test_zero(self):
        self.assertEqual(self.machine.sixes([6,1,3,4,5]), 0, "Should be 0")
    
    def test_one(self):
        self.assertEqual(self.machine.sixes([1,2,3,4,5]), 1, "Should be 1")
        self.assertEqual(self.machine.sixes([2,3,4,5,1]), 1, "Should be 1")
        self.assertEqual(self.machine.sixes([2,2,2,5,2]), 5, "Should be 1")
    
    def test_two(self):
        self.assertEqual(self.machine.sixes([2,2,1,4,5]), 2, "Should be 2")


if __name__ == '__main__':
    unittest.main()
    
