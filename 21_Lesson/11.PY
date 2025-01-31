import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        roll = input("Do you roll a dice? (yes/No): ").lower()
        if roll == "yes":
            computer_roll = roll_dice()
            player_roll = roll_dice()
            print(f"Computer:{computer_roll}")
            print(f"Player: {player_roll}")
            computer_score += computer_roll
            player_score += player_roll
        elif roll == "no":
            break
        else:
            print("Invalit input. plase type 'yes' or 'no'.")

    print("\n****FINAL SCORE*****")
    print(f"computer: {computer_score}")
    print(f"Player: {player_score}")

    if player_score > computer_score:
        print("conguter Won1 Better luck Next time.")
    elif player_score < computer_score:
        print("computer won1 Better luck Next Time")
    else:
        print("it's a tie1")

play_game()