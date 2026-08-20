def deposit(balance):
    deposit_amount = float(input("Enter Deposit Amount: "))
    balance += deposit_amount
    print("Amount deposited successfully!")
    print(f"Current Balance: {balance}")
    return balance

def withdraw(balance):
    withdrawal = float(input("Enter Withdrawal Amount: "))
    if balance > 0:
        if withdrawal <= balance:
            balance -= withdrawal
            print("Withdrawal successful!")
            print(f"Current Balance: {balance}")
        else:
            print("Insufficient Funds")
    else:
        print("No funds available")
    return balance

def check_balance(balance):
    print(f"Current Balance: {balance}")
    return balance

def menu():
    balance = 50000.0
    while True:
        print("===== BANK MANAGEMENT SYSTEM =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            balance = deposit(balance)
        elif choice == 2:
            balance = withdraw(balance)
        elif choice == 3:
            check_balance(balance)
        elif choice == 4:
            print("Exiting...")
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice.")
menu()
