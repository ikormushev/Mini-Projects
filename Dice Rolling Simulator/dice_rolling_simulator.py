import random

print("This is a dice rolling simulator!")
print("If you want to roll the dice, type roll."
      "\nIf you want to stop, type stop.")

commands_list = ["roll", "stop"]
dice_numbers = [1, 2, 3, 4, 5, 6]


def dice_choice():
    choice = random.choice(dice_numbers)
    return choice


def dice_drawing():
    if dice_side == 1:
        print("-------")
        print("|     |")
        print("|  ●  |")
        print("|     |")
        print("-------")
    elif dice_side == 2:
        print("-------")
        print("|    ●|")
        print("|     |")
        print("|●    |")
        print("-------")
    elif dice_side == 3:
        print("-------")
        print("|    ●|")
        print("|  ●  |")
        print("|●    |")
        print("-------")
    elif dice_side == 4:
        print("-------")
        print("|●   ●|")
        print("|     |")
        print("|●   ●|")
        print("-------")
    elif dice_side == 5:
        print("-------")
        print("|●   ●|")
        print("|  ●  |")
        print("|●   ●|")
        print("-------")
    elif dice_side == 6:
        print("-------")
        print("|●   ●|")
        print("|●   ●|")
        print("|●   ●|")
        print("-------")


while True:
    print()
    command = input("Roll: ").lower()
    if command == "stop":
        break
    elif command not in commands_list:
        print("Please type a valid command!")
        continue

    dice_side = dice_choice()
    dice_drawing()
    print(f"You rolled a {dice_side}!")

print()
print("Thanks for playing!")
