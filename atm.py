# Features of ATM 
''' 
    1. Account Number,
    2. Cash Withdrawal
    3. Deposit
    4. Check Balance
    5. Transfer
    5. Exit
    6. Change Pin
    7. Print Bank Statement
'''

balance = 1000

# Function To check balance
def check_balance():
    print(f"Your balance is: , ksh{balance: .2f}" )

def deposit():
    global balance
    deposit_amount = float(input("Enter your deposit amount: "))
    if deposit_amount > 0:
        balance += deposit_amount
        print(f"${deposit_amount: .2f} has been deposited")
    else:
        print("Invalid deposit")

def withdraw():
    global balance
    withdraw_amount = float(input("Enter amount to withdraw: "))
    if withdraw_amount > 0 and withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"${withdraw_amount: .2f} has been withdrawn")
    elif withdraw_amount > balance:
        print("Insufficient Balance")
    else: 
        print("Invalid input / Invalid withdrawal amount")

while True:
    print("\n Welcome To the ATM")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Please select an option (1/2/3/4): ")
    
    if choice == '1':
       check_balance() 
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for visiting us!")
        break
    else:
        print(" Invalid Option")