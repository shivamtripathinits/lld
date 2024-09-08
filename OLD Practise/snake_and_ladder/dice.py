import random


class Dice:
    def __init__(self, dice_count, min_val=1, max_val=6):
        self.dice_count = dice_count
        self.min = min_val
        self.max = max_val

    def roll_dice(self):
        final_roll_value = 0
        for i in range(0, self.dice_count):
            final_roll_value += random.randint(self.min, self.max)
        return final_roll_value



