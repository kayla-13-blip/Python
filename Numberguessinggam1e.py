import random
def number_guessing_game():
    """
    A simple number guessing game that stores the users guesses in a list.
    """
    secret_number = random.randint(1, 100)
    guesses = []
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess it?")
    while True:
     try:
        current_guess = int(input("Enter your guess: "))
        guesses.append(current_guess)
        if current_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {len(guesses)} attempts.")
            print(f"Your guesses were: {guesses}")
            break
        elif current_guess < secret_number:
            print("Too low, try a higher number.")
        else:
            print("Too high, try a lower number.")
     except ValueError:
        print("Invalid input. Please enter a whole number.")
    if __name__ == "__main__":
     number_guessing_game()

