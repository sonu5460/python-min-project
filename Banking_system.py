

import json  # JSON file ke liye data store/load karne ke liye
import os    # File check karne ke liye (exists or not)

DATA_FILE = "accounts.json"  # Data save hone wali file
MIN_BALANCE = 500            # Har account me minimum ₹500 balance hona chahiye


#  Account Class: Ek user ka pura account data manage karta hai
class Account:
    def __init__(self, name, acc_no, pin, balance=MIN_BALANCE, history=None):
        self.name = name          # Account holder ka naam
        self.acc_no = acc_no      # Unique account number
        self.pin = pin            # PIN for login
        self.balance = balance    # Account balance
        self.history = history if history else []  # Transactions list

    #  Deposit method
    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: ₹"))
            if amount <= 0:
                print("❌ Amount must be positive.")
                return
            self.balance += amount  # Amount add kar rahe hai
            self.history.append(f"Deposited ₹{amount}")  # History me store
            print(f"✅ ₹{amount} deposited successfully.")
        except ValueError:
            print("❌ Invalid input.")  # Agar number nahi diya to error

    # Withdraw method
    def withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= 0:
                print("❌ Amount must be positive.")
                return
            if amount > self.balance:
                print("❌ Insufficient balance.")
            
            elif self.balance - amount < MIN_BALANCE:
                print(f"❌ Cannot withdraw. ₹{MIN_BALANCE} must remain.")
            else:
                self.balance -= amount
                self.history.append(f"Withdrew ₹{amount}")
                print(f"✅ ₹{amount} withdrawn successfully.")
        except ValueError:
            print("❌ Invalid input.")

    #  Check Balance
    def check_balance(self):
        print(f"🔎 Account Balance: ₹{self.balance}")

    #  Show transaction history
    def show_history(self):
        print("\n📜 Transaction History:")
        if not self.history:
            print("No transactions yet.")
        else:
            for h in self.history:
                print(" -", h)

    #  Convert account to dict for saving to JSON
    def to_dict(self):
        return {
            "name": self.name,
            "acc_no": self.acc_no,
            "pin": self.pin,
            "balance": self.balance,
            "history": self.history
        }


#  BankSystem Class: Multiple accounts ko manage karta hai
class BankSystem:
    def __init__(self):
        self.accounts = {}  # All accounts stored in a dictionary
        self.load_accounts()  # Load saved accounts from file

    #  Load accounts from JSON file if exists
    def load_accounts(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                for acc_no, acc_data in data.items():
                    self.accounts[acc_no] = Account(**acc_data)

    #  Save all accounts to file
    def save_accounts(self):
        data = {acc_no: acc.to_dict() for acc_no, acc in self.accounts.items()}
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    #  Create new user account
    def create_account(self):
        print("\n📝 Create New Account")
        name = input("Enter account holder name: ")
        acc_no = input("Set 6-digit account number: ")
        if acc_no in self.accounts:
            print("❌ Account number already exists.")
            return
        pin = input("Set 4-digit PIN: ")
        self.accounts[acc_no] = Account(name, acc_no, pin)
        self.save_accounts()
        print("✅ Account created successfully.")

    def delete_account(self, acc):
        confirm = input("Are you sure you want to delete this account? (yes/no): ").lower()
        if confirm == 'yes':
            pin = input("Enter your PIN to confirm: ")
            if pin == acc.pin:
                 del self.accounts[acc.acc_no]  # Remove from dictionary
                 self.save_accounts()  # Save changes to file
                 print("✅ Account deleted successfully.")
                 return True  # To exit menu after deletion
            else:
                 print("❌ Incorrect PIN. Deletion cancelled.")
        else:
            print("⚠️ Deletion cancelled.")
            return False
                                     
    #  Login to existing account
    def login(self):
        print("\n🔐 Login")
        acc_no = input("Enter account number: ")
        pin = input("Enter PIN: ")

        acc = self.accounts.get(acc_no)
        if acc and acc.pin == pin:
            print(f"✅ Welcome {acc.name}!")
            self.account_menu(acc)
        else:
            print("❌ Invalid account number or PIN.")

    #  Menu shown after successful login
    def account_menu(self, acc):
        while True:
            print(f"\n🏦 Account: {acc.name} | No: {acc.acc_no}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Delete Account")
            print("6. Logout")
            choice = input("Choose option: ")

            if choice == '1':
                acc.deposit()
            elif choice == '2':
                acc.withdraw()
            elif choice == '3':
                acc.check_balance()
            elif choice == '4':
                acc.show_history()
            elif choice == '5':
                if self.delete_account(acc):
                    break       # Exit menu after deletion
            elif choice == '6':
                self.save_accounts()
                print("🚪 Logged out.")
                break
            else:
                print("❌ Invalid option.")

    #  Main menu of the system
    def run(self):
        while True:
            print("\n========= WELCOME TO PYBANK =========")
            print("1. Create New Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Select option: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.save_accounts()
                print("👋 Thanks for using PyBank!")
                break
            else:
                print("❌ Invalid choice.")


# Start the banking system
if __name__ == "__main__":
    bank = BankSystem()
    bank.run()
