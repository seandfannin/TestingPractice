class ScoreMachine:
    def __init__(self):
        pass
    
    def aces(self,rolls):
        total = 0
        for item in rolls:
            if item == 1:
                total += item
        return total
    
def testAces():
    x = ScoreMachine()
    assert 5 == x.aces([1,1,1,1,1])
    assert 4 == x.aces([1,1,1,1])
    
    print("Aces tests passed!")
    