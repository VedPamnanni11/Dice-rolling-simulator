import random

nums_in_dice = [1, 2, 3, 4, 5, 6]

nums_of_dice = input("How many dices do you want to roll 1 or 2 : ")
while True:
    if nums_of_dice == "2":
        chosen_num1 = random.choice(nums_in_dice)
        chosen_num2 = random.choice(nums_in_dice)
        print(chosen_num1, "and", chosen_num2)
        nums_of_dice = input("How many dices do you want to roll again? 1 or 2 : ")
        
    elif nums_of_dice == "1":
        chosen_num = random.choice(nums_in_dice)
        print(chosen_num)
        nums_of_dice = input("How many dices do you want to roll again? 1 or 2 : ")

    elif nums_of_dice == "2":
        chosen_num1 = random.choice(nums_in_dice)
        chosen_num2 = random.choice(nums_in_dice)
        print(chosen_num1, "and", chosen_num2)
        nums_of_dice = input("How many dices do you want to roll again? 1 or 2 : ")
    else:
        print("Please enter a valid number between 1 and 2!")
        break
    