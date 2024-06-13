import random
userInput = int(input("Enter The Length of Password:- "))

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallAlpha = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
specialChars = "!@#$%^&*"

ratio1 = userInput//3
ratio2 = userInput%3

def passwordGenerator(userInput):
    __password = ""
    for i in range(ratio1):
        __password += alpha[random.randint(0,25)]
        __password += smallAlpha[random.randint(0,25)]
        __password += nums[random.randint(0,9)]

    for i in range(ratio2):
        __password += specialChars[random.randint(0,7)]

    return __password

print(passwordGenerator(userInput))



