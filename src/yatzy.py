from src.pips import Pips

class Yatzy:
    
    ZERO_POINTS = 0
    FIFTY_POINTS = 50
    NUMBER_OF_DICE = 5
    NUMBER_OF_FACES = 6
    SMALL_STRAIGHT_SCORE = 15
    LARGE_STRAIGHT_SCORE = 20 


    @staticmethod
    def chance_score(*dice): 
        return sum(dice)
    """
     Smell: Long Function
    Common Refactorings: Replace Temp with Query
    """

    @staticmethod
    def yatzy(dice):
        dice_value_frequencies = [Yatzy.ZERO_POINTS] * (len(dice) + Pips.ONE.value)
        for die in dice:
            dice_value_frequencies[die - Pips.ONE.value] += Pips.ONE.value
        for frequency in range(len(dice_value_frequencies)):
            if dice_value_frequencies[frequency] == Yatzy.NUMBER_OF_DICE:
                return Yatzy.FIFTY_POINTS
        return Yatzy.ZERO_POINTS
    """
    Smell: Primitive Obsession
    Common Refactorings: Replace Primitive with Object
    """

    @staticmethod
    def ones(*dice):
        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE
    """
    Smell: Loops
    Common Refactorings: Replace Loop with Pipeline
    """

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    @staticmethod
    def fours(*dice):
        FOUR = Pips.FOUR.value
        return dice.count(FOUR) * FOUR

    @staticmethod
    def fives(*dice):
        FIVE = Pips.FIVE.value
        return dice.count(FIVE) * FIVE

    @staticmethod
    def sixes(*dice):
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX

    @staticmethod
    def score_pair(*dice):
        dice = sorted(dice, reverse=True)
        for value in Pips.reversedValues():
            if dice.count(value) >= Pips.TWO.value:
                return value * Pips.TWO.value
        return Yatzy.ZERO_POINTS
    """
    Smell: Long Function
    Common Refactorings: Extract Function 
    """

    @staticmethod
    def two_pair(*dice):
        dice = sorted(dice, reverse=True)
        pair_count = Yatzy.ZERO_POINTS
        score = Yatzy.ZERO_POINTS
        for value in Pips.reversedValues():
            if dice.count(value) >= Pips.TWO.value:
                pair_count += Pips.ONE.value
                score += value * Pips.TWO.value
        return score if pair_count >= Pips.TWO.value else Yatzy.ZERO_POINTS
    """
    Smell: Long Function
    Common Refactorings: Extract Function        
    """
    @staticmethod
    def three_of_a_kind(*dice):
        THREE = Pips.THREE.value
        for pip in Pips.reversedValues():
            if dice.count(pip) >= THREE:
                return pip * THREE
        return Yatzy.ZERO_POINTS
    """
    Smell: Long Function
    Common Refactorings: Extract Function
    """


    @staticmethod
    def four_of_a_kind(*dice):
        tallies = Yatzy._count_dice(dice)
        for pip_value in range(len(tallies)):
            if tallies[pip_value] >= Pips.FOUR.value:
                return (pip_value + Pips.ONE.value) * Pips.FOUR.value
        return Yatzy.ZERO_POINTS
    """
    Smell: Duplicated Code
    Common Refactorings: Extract Function
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
    """

    @staticmethod
    def smallStraight(*dice):
        required = {Pips.ONE.value, Pips.TWO.value, Pips.THREE.value, Pips.FOUR.value, Pips.FIVE.value}
        return Yatzy.SMALL_STRAIGHT_SCORE if set(dice) == required else Yatzy.ZERO_POINTS
    """
    Smell: Magic Numbers
    Common Refactorings: Replace Magic Number with Symbolic Constant
    """

    @staticmethod
    def largeStraight(*dice):
        required = {Pips.TWO.value, Pips.THREE.value, Pips.FOUR.value, Pips.FIVE.value, Pips.SIX.value}
        return Yatzy.LARGE_STRAIGHT_SCORE if set(dice) == required else Yatzy.ZERO_POINTS
    """
    Refactoring: Replacing manual counting with set operations
    """

    @staticmethod
    def fullHouse(*dice):
        pairs = [v for v in Pips.values() if dice.count(v) == Pips.TWO.value]
        threes = [v for v in Pips.values() if dice.count(v) == Pips.THREE.value]
        if pairs and threes:
            return pairs[0]*Pips.TWO.value + threes[0]*Pips.THREE.value
        return Yatzy.ZERO_POINTS
    """
    Smell: Long Function
    Common Refactorings: Extract Function
    """



