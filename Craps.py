import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def play_game():
    dice_1, dice_2 = roll_dice()
    total = dice_1 + dice_2
    print(f"First roll: {dice_1} + {dice_2} = {total}")

    if total in [7, 11]:
        print("You Won!")
        return
    elif total in [2, 3, 12]:
        print("Craps! You Lose.")
        return

    goal = total
    print(f"Goal point is: {goal}")

    while True:
        d1, d2 = roll_dice()
        current = d1 + d2
        print(f"Roll: {d1} + {d2} = {current}")

        if current == 7:
            print("You Lose.")
            break
        elif current == goal:
            print("You Win!")
            break
play_game()