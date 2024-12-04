class InsufficientFundsError(Exception):
    def __init__(self, message):
        super().__init__(message)

class BankAccount:
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError("Insufficient funds in the account.")
        self.balance -= amount
        print(f"Withdrew {amount} from the account. New balance: {self.balance}")

account = BankAccount(1500, 500)

try:
    account.withdraw(800)
    account.withdraw(400)  # This will raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Error: {e}")