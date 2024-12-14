import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie.."
    
    if (user_choice == 'rock' and computer_choice == 'scissor') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissor' and computer_choice == 'paper'):
        return "You win!"
    
    return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissor!")
    
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()
        if user_choice in ['rock', 'paper', 'scissor']:
            break
        else:
            print("Invalid choice. Please choose rock, paper, or scissor.")
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
if __name__ == "__main__":
    play_game()
