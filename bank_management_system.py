accounts = {}

def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    accounts[acc_no] = {"name": name, "balance": balance}
    print("✅ Account created successfully")

def deposit():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    if acc_no in accounts:
        accounts[acc_no]["balance"] += amount
        print("💰 Amount deposited")
    else:
        print("❌ Account not found")

def withdraw():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    if acc_no in accounts:
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print("💸 Withdrawal successful")
        else:
            print("❌ Insufficient balance")
    else:
        print("❌ Account not found")

def check_balance():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print("Balance:", accounts[acc_no]["balance"])
    else:
        print("❌ Account not found")

while True:
    print("\n🏦 Bank Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        break
    else:
        print("❌ Invalid choice")
