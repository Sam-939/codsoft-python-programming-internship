import random
print("welcome to Rock Paper Scissor Game!")
while True:
    play_game = input("Do you want to play Rock, Paper, Scissor? (yes/no): ").lower()
    if play_game == "no":
        print("Thank you for playing!")
        break
    elif play_game != "yes":
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue
    your_choice = input("Choose rock or paper, or scissor: ").lower()
    while your_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice. Please choose rock or paper or scissor.")
        your_choice = input("Choose rock or paper or scissor: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissor"])
    if your_choice == computer_choice:
        output = "It's a tie!"
    elif (
        (your_choice == "rock" and computer_choice == "scissor")
        or (your_choice == "paper" and computer_choice == "rock")
        or (your_choice == "scissor" and computer_choice == "paper")):
        output = "You win!"
    else:
        output = "You lose!"
    print(f"You choice is {your_choice}, the computer choice is {computer_choice}.")
    print(output)
