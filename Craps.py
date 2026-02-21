import random
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)

if dice_1 + dice_2 == 7 or dice_1 + dice_2 == 11:      # 7, 11
    print('You Won!')
elif dice_1 + dice_2 in [2, 3, 12]:                    # 2, 3, 12
    print('You Lose.')
else:                                                  # 4, 5, 6, 8, 9, 10
    while True:
        dice_3 = random.randint(1,6)
        dice_4 = random.randint(1,6)
        if dice_3 + dice_4 == 7:
            print('You Lose.')
            break
        elif dice_3 + dice_4 == dice_2 + dice_1:
            print('You Win!')
            break