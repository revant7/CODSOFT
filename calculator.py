

def Calc(a,b,operator):

    if operator == "+":
        return a + b

    elif operator == "*":
        return a*b

    elif operator == "-":
        return a - b

    elif operator == "/":
        return a/b

    elif operator == "**":
        return a**b

    elif operator == "0":
        print("Thank You!")
        return 1
        

    else:
        print("Invalid Input! Enter Correct Input!")
        return 0


        
print("""MENU
1. Enter The First Number.
2. Enter The Second Number.
3. Enter The Operator.
   Enter "+" For Addition
   Enter "-" For Subtraction
   Enter "*" For Multiplication
   Enter "/" For Division
   Enter "**" For Exponential

   Enter "0" To Exit.

   THANK YOU!    
""")


while True:
    try:
        a = int(input("Enter First Number:- "))
        b = int(input("Enter Second Number:- "))
        operator = input("Enter The Operator:- ")
    except Exception as e:
        print(e)
        continue


    output = Calc(a,b,operator)
    while output == 0:
        output = Calc(a,b,operator)
    if output == 1:
        break
    else:
        print(f"The Result is {output}")


    