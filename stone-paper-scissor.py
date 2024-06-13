# stone paper scissor game

# stone = 0
# paper = 1
# scissor = 2

# Total 9 Cases:-

# stone and paper - paper wins
# paper and stone - paper wins

# stone and scissor - stone wins
# scissor and stone - stone wins


# paper and scissor - scissor wins
# scissor and paper - Scissor wins

# paper and paper - ties
# scissor and scissor = ties
# stone and stone - ties


import random

print("\n====Welcome To Stone The Paper Scissor Game!!!====\n")

computerScore = 0
userScore = 0
name = input("Enter Your Name:- ")
noOfRounds = int(input("\nEnter No. of Rounds You Want To Play:- "))
nor = 1

lt = []
print("\nEnter 0 For Stone\nEnter 1 For Paper\nEnter 2 For Scissor\n")
while nor <= noOfRounds:
    computerValue = random.randint(0, 2)
    userInput = int(input("Enter Your Choice:- "))

    if computerValue == userInput:
        lt.append(f"Round {nor} - TIES")
        print(
            f"\nYou Entered:- {userInput}\nComputer Played:- {computerValue}\nRound {nor} - TIES.\n"
        )

    elif computerValue == 0 and userInput == 1:
        lt.append(f"Round {nor} - {name} WINS")
        userScore += 1
        print(
            f"\nYou Entered:- {userInput}\nComputer Played:- {computerValue}\nRound {nor} - {name} WINS This Round.\n"
        )

    elif computerValue == 1 and userInput == 0:
        lt.append(f"Round {nor} - COMPUTER WINS")
        computerScore += 1
        print(
            f"\nYou Entered:- {userInput}\nComputer Played:- {computerValue}\nRound {nor} - COMPUTER WINS This Round.\n"
        )

    elif computerValue == 0 and userInput == 2:
        lt.append(f"Round {nor} - COMPUTER WINS")
        computerScore += 1
        print(
            f"\nYou Entered:- {userInput}\nComputer Played:- {computerValue}\nRound {nor} - COMPUTER WINS This Round.\n"
        )

    elif computerValue == 2 and userInput == 0:
        lt.append(f"Round {nor} - {name} WINS")
        userScore += 1
        print(
            f"\nYou Entered:- {userInput}\nComputer Played:- {computerValue}\nRound {nor} - {name} WINS This Round.\n"
        )

    elif computerValue == 1 and userInput == 2:
        lt.append(f"Round {nor} - {name} WINS")
        userScore += 1
        print(
            f"\nYou Entered:- {userInput}\nComputer Played:- {computerValue}\nRound {nor} - {name} WINS This Round.\n"
        )

    elif computerValue == 2 and userInput == 1:
        lt.append(f"Round {nor} - COMPUTER WINS")
        computerScore += 1
        print(
            f"\nYou Entered:- {userInput}\nComputer Played:- {computerValue}\nRound {nor} - COMPUTER WINS This Round.\n"
        )

    else:

        print("ERROR")

    nor += 1

print("\nComputer Score:- ", computerScore)
print(f"\n{name}'s Score:- {userScore}")
print("\nNumber of Rounds Played:- ", noOfRounds)
[print(i) for i in lt]


if userScore > computerScore:
    print(f"\n{name} WINS The Game!!!")

elif userScore == computerScore:
    print("\nOops! This Game TIES. Try Again.")

else:
    print("\nCOMPUTER WINS The Game!!! BETTER LUCK NEXT TIME.")
