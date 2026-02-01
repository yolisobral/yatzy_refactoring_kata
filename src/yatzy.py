from src.pips import Pips

class Yatzy:
    
    ZERO_POINTS = 0
    FIFTY_POINTS = 50
    NUMBER_OF_DICE = 5
    NUMBER_OF_FACES = 6
    SMALL_STRAIGHT_SCORE = 15


    @staticmethod
    def chance_score(*dice): 
        return sum(dice)
    """
     Smell: Long Function
    Common Refactorings: Replace Temp with Query
    """

    @staticmethod
    def yatzy(dice):
        dice_value_frequencies = [Yatzy.ZERO_POINTS] * (len(dice) + Pips.ONE.value) #Initialize frequency list
        for die in dice: #Count occurrences of each die value
            dice_value_frequencies[die - Pips.ONE.value] += Pips.ONE.value #Increment count for this die value
        for frequency in range(len(dice_value_frequencies)): #Check for Yatzy condition
            if dice_value_frequencies[frequency] == Yatzy.NUMBER_OF_DICE: #If any die value appears 5 times
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
    def two_pair(*dice):
        dice = sorted(dice, reverse=True)
        for value in Pips.reversedValues():
          if dice.count(value) >= Pips.TWO.value:
               pair_count += Pips.ONE.value
        score += value * Pips.TWO.value
        if pair_count == Pips.TWO.value: # Check if two pairs were found
                    return score
        return Yatzy.ZERO_POINTS
    """
    Smell: Long Function
    Common Refactorings: Extract Function        
    """
    










    @staticmethod
    def four_of_a_kind(*dice):
       tallies = Yatzy._count_dice(dice) 
       for pip_value in range(len(tallies)):
         if tallies[pip_value] >= Pips.FOUR.value: return (pip_value + 1) * Pips.FOUR.value 
         return Yatzy.ZERO_POINTS
       """ 
       Smell: Long Parameter List Common Refactorings: Introduce Parameter Object 
       Smell: Duplicated Code Common Refactorings: Extract Function
       Smell: Primitive Obsession Common Refactorings: Replace Primitive with Object
       """

    @staticmethod
    def _count_dice(dice):
        tallies = [Yatzy.ZERO_POINTS] * Yatzy.NUMBER_OF_FACES
        for die in dice:
            tallies[die - Pips.ONE.value] += Pips.ONE.value
        return tallies
        """
        Smell: Temporary Variables
        Common Refactorings: Replace Temp with Query

        Smell: Duplicated Code
        Common Refactorings: Extract Function
        """

   

    @staticmethod
    def smallStraight(*dice):
        tallies = Yatzy._count_dice(dice)
        required = [1, 1, 1, 1, 1, 0] # 1–5 straight 
        if all(tallies[i] == required[i] for i in range(len(required))): 
            return Yatzy.SMALL_STRAIGHT_SCORE       
        return Yatzy.ZERO_POINTS    
    """ 
    Smell: Duplicated Code Common Refactorings: Extract Function 
    Smell: Magic Numbers Common Refactorings: Replace Magic Number with Symbolic Constant 
    """
 
    


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