from src.pips import Pips

class Yatzy:
    
    ZERO_POINTS = 0
    FIFTY_POINTS = 50
    NUMBER_OF_DICE = 5
    NUMBER_OF_FACES = 6

    @staticmethod
    def chance_score(*dice):
        return sum(dice)
    """
     Smell: Long Function
    Common Refactorings: Replace Temp with Query
    """

    @staticmethod
    def yatzy(dice):
        dice_value_frequencies = [0] * (len(dice) + 1) #Initialize frequency list
        for die in dice: #Count occurrences of each die value
            dice_value_frequencies[die - 1] += 1 #Increment count for this die value
        for frequency in range(len(dice_value_frequencies)): #Check for Yatzy condition
            if dice_value_frequencies[frequency] == 5: #If any die value appears 5 times
                return Yatzy.FIFTY_POINTS #Return Yatzy score
        return Yatzy.ZERO_POINTS
    """
    Smell: Primitive Obsession
    Common Refactorings: Replace Primitive with Object
    Smell: Rename Variable
    Common Refactorings: Mysterious Name
    """
  
    

    @staticmethod
    def ones(*dice): # Calculate score for ones
        ONE = Pips.ONE.value #Get the pip value for ones
        return dice.count(ONE) * ONE #Count and multiply by pip value
    """
    Smell: Loops
    Common Refactorings: Replace Loop with Pipeline
    Smell: Long Parameter List
    Common Refactorings: Introduce Parameter Object
    """
      

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO
    """
    Smell: Loops
    Common Refactorings: Replace Loop with Pipeline
    Smell: Long Parameter List
    Common Refactorings: Introduce Parameter Object
    """


    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE
    """
    Smell: Loops
    Common Refactorings: Replace Loop with Pipeline
    Smell: Long Parameter List
    Common Refactorings: Introduce Parameter Object
    """

    @staticmethod
    def fours(*dice):
        FOUR = Pips.FOUR.value
        return dice.count(FOUR) * FOUR
    """
    Smell: Loops
    Common Refactorings: Replace Loop with Pipeline
    Smell: Long Parameter List
    Common Refactorings: Introduce Parameter Object
    """
    

    @staticmethod
    def fives(*dice):
        FIVE = Pips.FIVE.value
        return dice.count(FIVE) * FIVE
    """
    Smell: Loops
    Common Refactorings: Replace Loop with Pipeline
    Smell: Long Parameter List
    Common Refactorings: Introduce Parameter Object
    """

    @staticmethod
    def sixes(*dice):
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX
    """
    Smell: Loops
    Common Refactorings: Replace Loop with Pipeline
    Smell: Long Parameter List
    Common Refactorings: Introduce Parameter Object
    """
    
    @staticmethod
    def score_pair(*dice):
       dice = sorted(dice, reverse=True) # Sort dice in descending order
       for value in Pips.reversedValues(): # Iterate from highest to lowest pip value
           if dice.count(value) >= Pips.TWO.value: # Check if there are at least two of this value
               return value * Pips.TWO.value # Return the score for the pair
       return Yatzy.ZERO_POINTS
   
    """
    Smell: Long Function
    Common Refactorings: Extract Function 
    """ 















    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0