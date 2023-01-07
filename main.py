import random

def main():
  # List of play options
  plays = ["rock", "paper", "scissors"]

  # Welcome message
  print("Welcome to Rock-Paper-Scissors!\n")

  while True:
    # Get player's play
    player = input("Enter your play (rock, paper, scissors): ").lower()

    # Check if player wants to quit
    if player == "quit" or player == "q":
      print("Thanks for playing!\n")
      break

    # Make sure player entered a valid play
    if player not in plays:
      print("Invalid play. Please try again.\n")
      continue

    # Get computer's play
    computer = random.choice(plays)

    # Display plays
    print(f"You played {player}. Computer played {computer}.\n")

    # Determine the winner
    if player == computer:
      print("It's a tie!\n")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
      print("You win!\n")
    else:
      print("Computer wins!\n")

# Run the game
main()


