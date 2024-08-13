import random

rock = (''' 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
''')

paper =('''
         ,..........   ..........,
     ,..,'          '.'          ',..,
    ,' ,'            :            ', ',
   ,' ,'             :             ', ',
  ,' ,'              :              ', ',       
 ,' ,'............., : ,.............', ',
,'  '............   '.'   ............'  ',
'''''''''''''''''''''''''''''''''''''''''''
''')

scissors = (''' 
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
''')

rock_paper_scissors = ["Rock", "Paper", "Scissors"]
random_int = random.randint(0,2)
random_choice = rock_paper_scissors[random_int]

users_choice = input("Please type one of the following: ROCK, PAPER, SCISSORS\nYou choose: ").lower()

if users_choice == "rock":
    print(rock)
elif users_choice == "paper":
    print(paper)
else:
    print(scissors)

print(" ")
print(f"Computer chooses: {random_choice}")
print(" ")

if random_choice == "Rock":
    print(rock)
elif random_choice == "Paper":
    print(paper)
else:
    print(scissors)

if users_choice == "rock" and random_choice == "Scissors":
    print("You Win!!")
elif users_choice == "rock" and random_choice == "Paper":
    print("You Lose!!")

elif users_choice == "paper" and random_choice == "Rock":
    print("You Win!!")
elif users_choice == "paper" and random_choice == "Scissors":
    print("You Lose!!")

elif users_choice == "scissors" and random_choice == "Paper":
    print("You Win!!")
elif users_choice == "scissors" and random_choice == "Rock":
    print("You Lose!!")

else:
    print("Draw!!")
    
print(" ")