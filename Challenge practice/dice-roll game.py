import random
def roll():
        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)
        return first_dice,second_dice # python iterprets the result as tuple
    

print(f'Outcome of dice roll is {roll()}')