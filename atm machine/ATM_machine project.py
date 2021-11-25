import time

print("please insert your CARD")

time.sleep(5)

password = 1234

pin = int(input("enter your atm pin: "))

if pin == password:
    while True:
        print("""
        1 == balance
        2 == withdraw
        3 == deposit balance
        4 == exit
        """)
        try:
            option = int(input("please enter your name: "))
        except:
            print("please enter valid option")

        if option == 1:
            print(f"your current balance is {balance}")
            print("==============================================================================")

        if option == 2:
            withdraw_amount = int(input("please withdraw_amount "))
            balance = balance = withdraw_amount
            print(f"{withdraw_amount} is debited from your account ")
            print(f"your current balance is {balance}")
            print("==============================================================================")
        if option == 3:
            deposit_amount = int(input("please enter deposit_amount"))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {balance}")
            print("==============================================================================")

        if option == 4:
            break
else:
    print("wrong pin please try again....")
