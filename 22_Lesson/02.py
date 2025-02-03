import random
Choices = ["rock", "paper", "scissors"]
c = 0
p = 0

while True:
    computer = random.choice(Choices)
    player = input("rock, paper or scissors?")
    if player == "rock":
        if computer == "rock":
            print("Tie")
        elif computer == "paper":
            print("You lost:(paper covers rock")
            c += 1
        elif computer == "scissors":
            print("You won:) rock smashes scissors")
            p += 1
    elif player == "paper":
        if computer == "paper":
            print("Tie")
        elif computer == "scissors":
            print("You lost:(scissors cuts paper)")
            c += 1
        elif computer == "rock":
            print("You won:) paper covers rock")
            p += 1
    elif player == "scissors":
        if computer == "scissors":
            print("Tie")
        elif computer == "rock":
            print("You lost:(rock smashes scissors")
            c += 1
        elif computer == "paper":
            print("You won:)scissors cuts paper")
            p += 1
    elif player == 'end':
        print("*****FINAL SCORES*****")
        print("Computer:", c)
        print("Player:", p)
        if p > c:
            print("Congratulation! You Won!")
        elif p < c:
            print("Soryy! You Lost!")
        else:
            print("Ops...")
        break
    else:
        print("Wrong command...")