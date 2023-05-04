
class Account:
    interest_rate = 0.02

    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited into the account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from the account.")

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"The interest earned is {interest}.")


account1 = Account("9765328", 1000, "Checking")

account1.deposit(2500)