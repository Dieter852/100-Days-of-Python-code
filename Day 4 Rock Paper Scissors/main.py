import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]
computers_choice = random.randint(0, 2)


print("Welcome to Rock, Paper, Scissors")
players_choice = int(input("Select a number to play\n0 - Rock\n1 - Paper\n2 - Scissors\n"))

if players_choice in range(0, 3):
    print(f"You chose:\n{game_list[int(players_choice)]}")
    print(f"Computer chose:\n{game_list[computers_choice]}")

    if players_choice == 0 and computers_choice == 2:
        print("YOU WIN.")
    elif players_choice == 1 and computers_choice == 0:
        print("YOU WIN.")
    elif players_choice == 2 and computers_choice == 1:
        print("YOU WIN.")
    elif players_choice == computers_choice:
        print("DRAW")
    else:
        print("COMPUTER WINS.")
else:
    print("That was a incorrect number! GAME OVER!")