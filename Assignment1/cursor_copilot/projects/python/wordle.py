import json
from datetime import datetime

def wordle_game():
    with open('words.json', 'r') as f:
        data = json.load(f)

    current_day = str(datetime.now().day)
    word_to_guess = data[current_day]
    attempts = 0

    while True:
        user_guess = input("Enter your guess: ")
        attempts += 1

        if len(user_guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        if user_guess == word_to_guess:
            print(f"Congratulations! You've guessed the word in {attempts} attempts.")
            break

        feedback = ''
        for guess_char, word_char in zip(user_guess, word_to_guess):
            if guess_char == word_char:
                feedback += guess_char.upper()
            elif guess_char in word_to_guess:
                feedback += guess_char
            else:
                feedback += '_'

        print(feedback)

if __name__ == "__main__":
    wordle_game()