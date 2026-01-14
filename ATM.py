class ATM:
    def __init__(self, balance=0, pin=1234):
        self.balance = balance
        self.pin = pin

    def check_pin(self):
        user_pin = int(input("Enter your 4-digit PIN: "))
        if user_pin == self.pin:
            print("PIN correct. Welcome!")
            return True
        else:
            print("Incorrect PIN. Try again.")
            return False

    def display_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. Remaining balance: ${self.balance:.2f}")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

def main():
    atm = ATM(balance=1000)  

    if atm.check_pin():
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                atm.display_balance()
            elif choice == "2":
                atm.withdraw()
            elif choice == "3":
                atm.deposit()
            elif choice == "4":
                print("Thank you for using our ATM!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()