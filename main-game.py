import random

# Level input function
def get_level_range():
    while True:
        level = input("Choose a level (Easy=1/Medium=2/Hard=3): ").strip().lower()
        if level in ['easy', '1']:
            return 1, 10
        elif level in ['medium', '2']:
            return 1, 50
        elif level in ['hard', '3']:
            return 1, 100
        else:
            print("Invalid level! Please choose Easy, Medium, or Hard or (1/2/3).")

def play_game():
    low, high = get_level_range()
    number = random.randint(low, high)

    print(f"\n >> I have selected a number between {low} and {high}. Try to guess it!")
    while True:
        try:
            user_input = int(input("Enter your guess: "))

            if user_input < low or user_input > high:
                print(f"Please enter a number between {low} and {high}.")
                continue

            if user_input == number:
                print("Congratulations! You guessed it right!")
                break
            elif user_input < number:
                print("Too low.. Try again!")
            else:
                print("Too high.. Try again!")

        except ValueError:
            print("Please enter a valid number!")

while True:
    play_game()

    while True:
        choice = input("Do you want to play again? (yes/y) or (no/n): ").strip().lower()
        if choice in ['yes', 'y']:
            break
        elif choice in ['no', 'n']:
            print("Thanks for playing! Goodbye!")
            exit()
        else:
            print("Invalid input! Please type (yes/y) or (no/n).")

