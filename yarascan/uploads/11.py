import random
import tkinter as tk
from tkinter import simpledialog

def get_cows_and_bulls(secret_number, guess):
    cows = 0
    bulls = 0
    secret_number = str(secret_number)
    guess = str(guess)

    secret_digits_count = {}
    guess_digits_count = {}

    # Count occurrences of each digit in secret_number and guess
    for digit in secret_number:
        if digit in secret_digits_count:
            secret_digits_count[digit] += 1
        else:
            secret_digits_count[digit] = 1

    for digit in guess:
        if digit in guess_digits_count:
            guess_digits_count[digit] += 1
        else:
            guess_digits_count[digit] = 1

    # Calculate bulls and adjust cows
    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            bulls += 1

    # Calculate cows
    for digit in guess_digits_count:
        if digit in secret_digits_count:
            cows += min(secret_digits_count[digit], guess_digits_count[digit])

    cows -= bulls  # Adjust cows to exclude digits counted as bulls

    return cows, bulls

def get_secret_number(player):
    root = tk.Tk()
    root.withdraw()
    while True:
        number = simpledialog.askstring(player, f"{player}, enter your 3-digit secret number:", show='*')
        if number and number.isdigit() and len(number) == 3:
            root.destroy()
            return number
        else:
            tk.messagebox.showerror("Invalid input", "Please enter a 3-digit number.")

def generate_ai_secret_number():
    return random.randint(100, 999)

def play_game():
    print("Welcome to the Cows and Bulls Game!")

    # Player A chooses a number
    player_a_number = get_secret_number("Player A")
    
    # AI_Bot generates a number
    ai_bot_number = generate_ai_secret_number()
    
    possible_numbers_a = [str(i).zfill(3) for i in range(1000)]
    
    current_player = 'A'
    print(f"\nPlayer A will start guessing first.\n")
    
    while True:
        if current_player == 'A':
            guess = input("Player A, enter your guess: ")
            if guess.isdigit() and len(guess) == 3:
                cows, bulls = get_cows_and_bulls(ai_bot_number, guess)
                print(f"Cows: {cows}, Bulls: {bulls}")
                if bulls == 3:
                    print("Player A has guessed the number correctly!")
                    break
                current_player = 'AI_Bot'
            else:
                print("Invalid guess. Please enter a 3-digit number.")
        elif current_player == 'AI_Bot':
            guess = random.choice(possible_numbers_a)
            print(f"AI_Bot guesses: {guess}")
            cows, bulls = get_cows_and_bulls(player_a_number, guess)
            print(f"Cows: {cows}, Bulls: {bulls}")
            if bulls == 3:
                print("AI_Bot has guessed the number correctly!")
                break
            possible_numbers_a = [num for num in possible_numbers_a if get_cows_and_bulls(num, guess) == (cows, bulls)]
            current_player = 'A'

if __name__ == "__main__":
    play_game()
