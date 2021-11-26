# This Project is Created and Uploaded by Sahil Rai.
# Created On August 18, 2020
# Uploaded On November 09, 2021


print("Welcome to the Python.hub Bank ATM\t")
restart = ("Y", "y", "yes", "Yes")
chances = 3
balance = 30000
balance2 = 2000
balance3 = 1467
balance4 = 3000
balance5 = 5670
while chances >= 0:
    pin = int(input("\tPlease Enter Your 4 Digit Pin:\n\t"))
    if pin == (1234):
        print("\tYou Entered Your Pin Correctly\n")
        print("\tPlease Press 1 For Your Account Balance\n")
        print("\tPlease Press 2 To Make Withdrawl\n")
        print("\tPlease Press 3 To Pay In\n")
        print("\tPlease Press 4 To Return Card\n")
        while restart not in ("n", 'no', 'NO', 'N'):
            option = int(input("What Would You Like To Choose?:\n"))
            if option == 1:
                print("\nYour Balance Is $", balance)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawl = float(
                    input("\nHow Much Would You Like To Withdraw?"))
                balance = balance - withdrawl
                print("\nYour Balance Is $", balance)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 3:
                Pay_in = float(input("How Much Would You Like To Pay?\n"))
                balance = balance + Pay_in
                print("\nYour Balance Is $", balance)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned...\n")
                print("Thank You For Your Service ")
                break
            else:
                print("Please Enter Correct Number. \n")
                restart = ("y")
    elif pin == (7890):
        print("\tYou Entered Your Pin Correctly\n")
        print("\tPlease Press 1 For Your Account Balance\n")
        print("\tPlease Press 2 To Make Withdrawl\n")
        print("\tPlease Press 3 To Pay In\n")
        print("\tPlease Press 4 To Return Card\n")
        while restart not in ("n", 'no', 'NO', 'N'):
            print("\tPlease Press 1 For Your Account Balance\n")
            print("\tPlease Press 2 To Make Withdrawl\n")
            print("\tPlease Press 3 To Pay In\n")
            print("\tPlease Press 4 To Return Card\n")
            option = int(input("What Would You Like To Choose?:\n"))
            if option == 1:
                print("\nYour Balance Is $", balance2)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawl = float(input(
                    "\nHow Much Would You Like To Withdraw?" "\n10,20,40,60,80,100 for other enter 1: "))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance2 = balance2 - withdrawl
                    print("\nYour Balance Is $", balance2)
                    restart = input("Would You Like To Go Back? \n")
                    if restart in ("n", 'no', 'NO', 'N'):
                        print("Thank You")
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print("Invalid Amount, Please Re-Try\n")
                    restart = ("y")
                elif withdrawl == 1:
                    withdrawl = float(input("Please Enter Desired Amount:\n"))
            elif option == 3:
                Pay_in = float(input("How Much Would You Like To Pay?\n"))
                balance2 = balance2 + Pay_in
                print("\nYour Balance Is $", balance2)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned...\n")
                print("Thank You For Your Service ")
                break
            else:
                print("Please Enter Correct Number. \n")
                restart = ("y")
    elif pin == (7009):
        print("\tYou Entered Your Pin Correctly\n")
        print("\tPlease Press 1 For Your Account Balance\n")
        print("\tPlease Press 2 To Make Withdrawl\n")
        print("\tPlease Press 3 To Pay In\n")
        print("\tPlease Press 4 To Return Card\n")
        while restart not in ("n", 'no', 'NO', 'N'):
            print("\tPlease Press 1 For Your Account Balance\n")
            print("\tPlease Press 2 To Make Withdrawl\n")
            print("\tPlease Press 3 To Pay In\n")
            print("\tPlease Press 4 To Return Card\n")
            option = int(input("What Would You Like To Choose?:\n"))
            if option == 1:
                print("\nYour Balance Is $", balance3)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawl = float(input(
                    "\nHow Much Would You Like To Withdraw?" "\n10,20,40,60,80,100 for other enter 1: "))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance3 = balance3 - withdrawl
                    print("\nYour Balance Is $", balance3)
                    restart = input("Would You Like To Go Back? \n")
                    if restart in ("n", 'no', 'NO', 'N'):
                        print("Thank You")
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print("Invalid Amount, Please Re-Try\n")
                    restart = ("y")
                elif withdrawl == 1:
                    withdrawl = float(input("Please Enter Desired Amount:\n"))
            elif option == 3:
                Pay_in = float(input("How Much Would You Like To Pay?\n"))
                balance3 = balance3 + Pay_in
                print("\nYour Balance Is $", balance3)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned...\n")
                print("Thank You For Your Service ")
                break
            else:
                print("Please Enter Correct Number. \n")
                restart = ("y")
    elif pin == (4567):
        print("\tYou Entered Your Pin Correctly\n")
        print("\tPlease Press 1 For Your Account Balance\n")
        print("\tPlease Press 2 To Make Withdrawl\n")
        print("\tPlease Press 3 To Pay In\n")
        print("\tPlease Press 4 To Return Card\n")
        while restart not in ("n", 'no', 'NO', 'N'):
            print("\tPlease Press 1 For Your Account Balance\n")
            print("\tPlease Press 2 To Make Withdrawl\n")
            print("\tPlease Press 3 To Pay In\n")
            print("\tPlease Press 4 To Return Card\n")
            option = int(input("What Would You Like To Choose?:\n"))
            if option == 1:
                print("\nYour Balance Is $", balance4)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawl = float(input(
                    "\nHow Much Would You Like To Withdraw?" "\n10,20,40,60,80,100 for other enter 1: "))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance4 = balance4 - withdrawl
                    print("\nYour Balance Is $", balance4)
                    restart = input("Would You Like To Go Back? \n")
                    if restart in ("n", 'no', 'NO', 'N'):
                        print("Thank You")
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print("Invalid Amount, Please Re-Try\n")
                    restart = ("y")
                elif withdrawl == 1:
                    withdrawl = float(input("Please Enter Desired Amount:\n"))
            elif option == 3:
                Pay_in = float(input("How Much Would You Like To Pay?\n"))
                balance4 = balance4 + Pay_in
                print("\nYour Balance Is $", balance4)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned...\n")
                print("Thank You For Your Service ")
                break
            else:
                print("Please Enter Correct Number. \n")
                restart = ("y")
    elif pin == (4321):
        print("\tYou Entered Your Pin Correctly\n")
        print("\tPlease Press 1 For Your Account Balance\n")
        print("\tPlease Press 2 To Make Withdrawl\n")
        print("\tPlease Press 3 To Pay In\n")
        print("\tPlease Press 4 To Return Card\n")
        while restart not in ("n", 'no', 'NO', 'N'):
            print("\tPlease Press 1 For Your Account Balance\n")
            print("\tPlease Press 2 To Make Withdrawl\n")
            print("\tPlease Press 3 To Pay In\n")
            print("\tPlease Press 4 To Return Card\n")
            option = int(input("What Would You Like To Choose?:\n"))
            if option == 1:
                print("\nYour Balance Is $", balance5)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawl = float(input(
                    "\nHow Much Would You Like To Withdraw?" "\n10,20,40,60,80,100 for other enter 1: "))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance5 = balance5 - withdrawl
                    print("\nYour Balance Is $", balance5)
                    restart = input("Would You Like To Go Back? \n")
                    if restart in ("n", 'no', 'NO', 'N'):
                        print("Thank You")
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print("Invalid Amount, Please Re-Try\n")
                    restart = ("y")
                elif withdrawl == 1:
                    withdrawl = float(input("Please Enter Desired Amount:\n"))
            elif option == 3:
                Pay_in = float(input("How Much Would You Like To Pay?\n"))
                balance5 = balance5 + Pay_in
                print("\nYour Balance Is $", balance5)
                restart = input("Would You Like To Go Back? \n")
                if restart in ("n", 'no', 'NO', 'N'):
                    print("Thank You")
                    break
            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned...\n")
                print("Thank You For Your Service ")
                break
            else:
                print("Please Enter Correct Number. \n")
                restart = ("y")
    else:
        print("Incorrect Password")
        chances = chances - 1
        if chances == 0:
            print("\nNo More Tries")
            break
