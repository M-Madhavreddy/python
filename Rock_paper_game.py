import random

def user_input():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice, Please choose rock, paper, or scissors.")

def computer_input():
    choices = ["rock", "paper", "scissors"]
    random_index = random.randint(0,1000) % 2
    return choices[random_index]


def who_is_winner(user, computer):
    if user == computer :
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

user_score = 0
computer_score = 0

while True:
    user = user_input()
    computer = computer_input()

    print(f"Your choice: {user}")
    print(f"Computer's choice: {computer}")

    result = who_is_winner(user, computer)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

    Continue = input("Do you want to play again? (yes/no): ").lower()
    if Continue != "yes":
        break
