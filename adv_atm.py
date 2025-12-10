# globally declared variables
bal = 50000
my_pin = "7129"

# To check the current balance
def balance():
    print(f"Your current balance is Rs. {bal}\n")

# To withdraw cash
def withdraw():
    pin = input("Enter your PIN: ")
    if my_pin == pin:
        cash= int(input("How much cash you want to withdraw?"))
        cu_balance = bal - cash
        print(f"Your amount is successfully withdraw and your current balance is Rs. {cu_balance}\n")
    else:
        print("Invalid pin")

# To deposit cash
def deposit():
    pin = input("Enter your PIN: ") 
    if my_pin == pin:
        d = int(input("Enter how much money you want to deposit?"))
        up_balance = d + bal
        print(f"Your balance after deposit is {up_balance}\n")
    else:
        print("Invalid pin")

# To change the current use pin

def change_pin():
    global my_pin
    old_pin = input("Enter your old PIN: ")

    if old_pin != my_pin:
        print(" Incorrect old PIN\n")
        return

    new_pin = input("Enter your new PIN: ")
    if len(str(new_pin)) != 4:
        print(" New PIN must be 4 digits\n")
        return
    
    my_pin = new_pin
    print("PIN changed successfully!")
    print(f"New PIN is: {new_pin}\n")

# Combining all the features(funtions)
print("----------Welcome to SBI-----------")
while True:
    print("1. Check Balance\n2. Withdraw Amount\n3. Deposit Amount\n4. Change PIN\n5. Exit System")
    ch = int(input("What do you what to ? Enter choice(1/2/3/4/5):"))
    if   ch == 1:
        balance()
    elif ch == 2:
        withdraw()
    elif ch == 3:
        deposit()
    elif ch == 4:
        change_pin()
    elif ch ==5:
        print("Exiting the ATM System...")
        break
    else:
        print("Inavlid choice")