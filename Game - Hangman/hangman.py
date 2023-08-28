import random
import json

print("Hello! Today, we will be playing the game \"Hangman\"!"
      "\nThe rules are simple:"
      "\n1. I will choose a secret word."
      "\n2. You will receive the first and the last letter of the word, along with their repetitions."
      "\n3. You have 10 attempts to guess each letter of the word."
      "\n4. If your guess is correct, you will discover the position of "
      "the letter in the word and, if the letter appears multiple times, "
      "its repetitions in the word."
      "\n5. If you think you know the whole word before using up all 10 guesses, "
      "you can always try to guess the word. If your guess is incorrect, "
      "it will be counted as a wrong guess. "
      "\n(Disclaimer - you cannot use words to try to find the letters of the secret word "
      "because the letters in that word won't be counted as separate letters.)"
      "\nGood luck!🍀")

with open("hangman_data.json", "r") as file:
    data = json.load(file)

guesses_list = []
wrong_guesses = 0
secret_word_found = False


def chosen_word():
    word = random.choice(data["secret words"])
    return word


def secret_word_starting_shown_letters():  # this function is needed because of Rule 2
    for s in range(1, len(secret_word)):
        if secret_word[0] == secret_word[s]:
            secret_word_indexes_list[s] = secret_word[0]
        if secret_word[-1] == secret_word[s]:
            secret_word_indexes_list[s] = secret_word[-1]
    return secret_word_indexes_list


secret_word = chosen_word()
guesses_list.append(secret_word[0])
guesses_list.append(secret_word[-1])

secret_word_indexes = secret_word[0] + (len(secret_word) - 2) * "_" + secret_word[-1]
secret_word_indexes_list = list(secret_word_indexes)
secret_word_starting_shown_letters()

print(f"The secret word is: {''.join(secret_word_indexes_list)}.")

while True:
       print()
    letter_found = False
    invalid_letter = False

    letter_guess = input("Give your guess: ").lower()
    for i in range(len(letter_guess)):
        if ord(letter_guess[i]) not in range(ord("a"), ord("z") + 1):
            invalid_letter = True
    if invalid_letter:
        print("Invalid letter found! Try again!")
        continue

    if letter_guess == secret_word:
        secret_word_found = True
        break

    if letter_guess in guesses_list:
        print("This letter has already been used! Try a different one!")
        continue
    guesses_list.append(letter_guess)

    for l in range(len(secret_word)):
        if secret_word[l] == letter_guess:
            letter_found = True
            secret_word_indexes_list[l] = letter_guess

    if "".join(secret_word_indexes_list) == secret_word:
        secret_word_found = True
        break

    if letter_found:
        print("You guessed a letter! Good job!")
        print(f"Guessed letters: {''.join(secret_word_indexes_list)}")
    else:
        wrong_guesses += 1
        if wrong_guesses == 10:
            print(f"You ran out of guesses! Play a new game!")
            print(f'The word was "{secret_word}"!')
            break
        print(f"Oops, wrong guess! Guesses left: {10 - wrong_guesses}. Try again!")

if secret_word_found:
    print(f'You guessed the word "{secret_word}"! Good job!')
