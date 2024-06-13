#stone = 0
#paper = 1
#scissor = 2

#Total 9 Cases:- 

#stone and paper - paper wins
#paper and stone - paper wins

#stone and scissor - stone wins
#scissor and stone - stone wins


#paper and scissor - scissor wins
#scissor and paper - Scissor wins

#paper and paper - ties
#scissor and scissor = ties
#stone and stone - ties



import random

computerScore = 0
userScore = 0
name = input("Enter Your Name:- ")
noOfRounds = int(input("Enter No. of Rounds You Want To Play:- "))
nor = noOfRounds
lt = []
while noOfRounds > 0:
    computerValue = random.randint(0,2)
    userInput = int(input("Enter Value:- "))

    if computerValue == userInput:
        lt.append(f"Round {noOfRounds} - TIES")

    elif computerValue == 0 and userInput == 1:
        lt.append(f"Round {noOfRounds} - USER WINS")
        userScore += 1

    elif computerValue == 1 and userInput == 0:
        lt.append(f"Round {noOfRounds} - COMPUTER WINS")
        computerScore += 1

    elif computerValue == 0 and userInput == 2:
        lt.append(f"Round {noOfRounds} - COMPUTER WINS")
        computerScore += 1

    elif computerValue == 2 and userInput == 0:
        lt.append(f"Round {noOfRounds} - USER WINS")
        userScore += 1

    elif computerValue == 1 and userInput == 2:
        lt.append(f"Round {noOfRounds} - USER WINS")
        userScore += 1

    elif computerValue == 2 and userInput == 1:
        lt.append(f"Round {noOfRounds} - COMPUTER WINS")
        computerScore += 1


    else:

        print("ERROR")

    noOfRounds -= 1

print("Computer Score:- ",computerScore)
print(f"{name}'s Score:- {userScore}")
print("Number of Rounds Played:- ",nor)
[print(i) for i in lt]

print(f"{name} WINS!!!") if userScore > computerScore else print("COMPUTER WINS!!! BETTER LUCK NEXT TIME.")


        


