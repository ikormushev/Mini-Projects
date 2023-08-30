import random

print("Hello! Today we will be playing the game rock-paper-scissors."
      "\nPossible guesses are only rock, paper or scissors."
      "\nWhen you give a guess, I will respond."
      "\nThe rules are:"
      "\n1. Rock beats scissors."
      "\n2. Scissors beat paper."
      "\n3. Paper beats rock."
      "\n4. If the guesses match, the game continues."
      "\n5. It's a best of 3, so try your best!")

guesses_list = ["rock", "paper", "scissors"]

guesses_emojis = {
    "rock": "🗿",
    "paper": "📄",
    "scissors": "✂️"
}

ally_wins = 0
enemy_wins = 0


def random_choice():
    choice = random.choice(guesses_list)
    return choice


def ally_winner():
    ally_win = False
    if ally_guess == "rock" and enemy_guess == "scissors":
        ally_win = True
    elif ally_guess == "paper" and enemy_guess == "rock":
        ally_win = True
    elif ally_guess == "scissors" and enemy_guess == "paper":
        ally_win = True
    return ally_win


def enemy_winner():
    enemy_win = False
    if ally_guess == "rock" and enemy_guess == "paper":
        enemy_win = True
    elif ally_guess == "paper" and enemy_guess == "scissors":
        enemy_win = True
    elif ally_guess == "scissors" and enemy_guess == "rock":
        enemy_win = True
    return enemy_win


while True:
    print()
    ally_guess = input("Give your try: ").lower()
    if ally_guess not in guesses_list:
        print(f"Give a valid guess - rock, paper or scissors!")
        continue
    else:
        enemy_guess = random_choice()
        print(f"My guess was {enemy_guess} {guesses_emojis[enemy_guess]}.")
        if ally_guess == enemy_guess:
            print("Oops, we matched. The game continues!")
            continue
        elif ally_winner():
            ally_wins += 1
            if ally_wins == 3:
                print("YOU WON! You are so good at this game!🏆")
                break
            print(f"You won this round! Great job! Wins left for you: {3 - ally_wins}.")
        elif enemy_winner():
            enemy_wins += 1
            if enemy_wins == 3:
                print("I WON! You can always try again!")
                break
            print(f"I won this round! Wins left for me: {3 - enemy_wins}.")
