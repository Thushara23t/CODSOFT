import random

# Function to display the main menu and get user input
def get_user_choice():
    print("Choose Rock, Paper, or Scissors (or type 'quit' to exit):")
    return input("Your choice: ").strip().lower()

# Function to get the computer's random choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        
        # Check if the user wants to quit the game
        if user_choice == 'quit':
            print("Thank you for playing!")
            break
        
        # Validate user input
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        # Get the computer's choice and determine the result
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice.capitalize()}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores based on the result
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        # Display the current scores
        print(f"Scores -> You: {user_score}, Computer: {computer_score}\n")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
play_game()
