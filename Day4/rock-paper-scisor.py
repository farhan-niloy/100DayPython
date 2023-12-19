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

moves = [rock, paper, scissors]

usr = input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.")

int_usr = int(usr) - 1

choose = moves[int_usr]

computer = random.randint(0, 2)

computer_choose = moves[computer]

print(f"\n\nYou've chosen\n {choose}")
print(f"Computer choose\n {computer_choose}")


if int_usr == computer:
    print("it's a tie")
elif (int_usr + computer) == 1 and int_usr > computer:
    print("you win!")
elif (int_usr + computer) == 2 and int_usr > computer:
    print("you win")
elif (int_usr + computer) == 3 and int_usr > computer:
    print("you win")
else:
    print("you loose")







