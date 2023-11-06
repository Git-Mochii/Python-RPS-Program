import random

# Define the available options for the game
options = ("rock", "paper", "scissors")

# Initialize the game loop flag
running = True

# Start the game loop
while running:
    # Get the player's name
    player_name = input("Enter your name: ")

    # Initialize the player's score
    player_score = 0

    # Initialize the computer's score
    computer_score = 0

    # Print a welcome message
    print(f"Welcome to the Rock, Paper, Scissors Game, {player_name}! You'll be playing against a CPU.")

    # Ask the player if they are ready to play
    choice = input("Are you ready to play? (y/n): ")

    # Check for valid choice for "Are you ready to play?"
    while choice not in ["y", "n"]:
        print("Invalid choice. Please enter 'y' for yes or 'n' for no.")
        choice = input("Are you ready to play? (y/n): ")

    if choice == "n":
        # If the player chooses not to play, print a goodbye message and exit the game loop
        print(f"Bye, {player_name}! Final Score: {player_name} - {player_score}, Computer - {computer_score}")
        running = False
    elif choice == "y":
        # If the player chooses to play, enter the game loop
        while True:
            # Initialize player's choice to None
            player = None

            # Randomly choose the computer's move
            computer = random.choice(options)

            # Keep prompting the player until they enter a valid choice
            while player not in options:
                player = input("Enter a choice (rock, paper, scissors): ")

            # Print the player's and computer's choices
            print(f"{player_name}: {player}")
            print(f"Computer: {computer}")

            # Determine the outcome of the game and update scores
            if player == computer:
                print(f"It's a tie, {player_name}!")
            elif player == "rock" and computer == "scissors":
                player_score += 1
                print(f"You win, {player_name}!")
            elif player == "paper" and computer == "rock":
                player_score += 1
                print(f"You win, {player_name}!")
            elif player == "scissors" and computer == "paper":
                player_score += 1
                print(f"You win, {player_name}!")
            else:
                computer_score += 1
                print(f"You lose, {player_name}!")

            # Display the current score
            print(f"Score: {player_name} - {player_score}, Computer - {computer_score}")

            # Ask the player if they want to play again
            play_again = input("Play again? (y/n): ").lower()

            # Check for valid choice for "Play again?"
            while play_again not in ["y", "n"]:
                print("Invalid choice. Please enter 'y' for yes or 'n' for no.")
                play_again = input("Play again? (y/n): ").lower()

            if play_again == "n":
                # If the player chooses not to play again, print a goodbye message and exit the game loop
                print(f"Thanks for playing, {player_name}! Final Score: {player_name} - {player_score}, Computer - {computer_score}")
                quit()

