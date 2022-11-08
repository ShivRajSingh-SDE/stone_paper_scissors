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
     9 (____)
---.__(___)
'''

#Write your code below this line 👇
game_sine= [rock, paper, scissors]

print("Hello guy's welcome to my game called rock paper sizer 🃏🃏 \n \n")


human_sin=input("what is your sine \n :- 0 for 'rock' 1 for 'paper' 2 for 'scissor' .\n ").lower()
print("Your sine")
human_sin= int(human_sin)#int
print(game_sine[human_sin])



computer_sine = random.randint(0,2)#int

print("computer sine")
print(game_sine[computer_sine])
if computer_sine == 0 and human_sin == 2:
  print("You Lose")
elif computer_sine== 2 and human_sin == 0 :
  print("You win")
  
elif computer_sine > human_sin:
  print("You Lose")
elif human_sin > computer_sine :
  print("You Win")
elif human_sin == computer_sine:
  print("game draw")


