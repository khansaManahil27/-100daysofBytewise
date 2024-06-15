import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while guess != number_to_guess:
        # Prompt the user to enter a guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        # Provide feedback
        if guess < number_to_guess:
            print("Your guess is too low. Try again.")
        elif guess > number_to_guess:
            print("Your guess is too high. Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

# Run the Guess the Number game
guess_the_number()