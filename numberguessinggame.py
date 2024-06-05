import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    if lower_bound >= upper_bound:
        print("Invalid range! The upper bound must be greater than the lower bound.")
        return
    
    secret_number = random.randint(lower_bound, upper_bound)
    max_attempts = int(input("Enter the maximum number of attempts: "))
    
    print(f"\nI'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: Make a guess: "))
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")
    
    print("Game over. Thank you for playing!")

if __name__ == "__main__":
    number_guessing_game()
