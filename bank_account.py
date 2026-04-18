class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        self.__history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__history.append(("withdraw", amount))

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)
        self.__history.append(("transfer_out", amount))

    def get_balance(self):
        return self.__balance

    def statement(self):
        lines = [f"Account {self.account_number} - {self.owner}"]
        for action, amount in self.__history:
            lines.append(f"  {action}: ${amount:.2f}")
        lines.append(f"Balance: ${self.__balance:.2f}")
        return "\n".join(lines)


if __name__ == "__main__":
    a = BankAccount("1001", "Jordan Lee", balance=500.00)
    b = BankAccount("1002", "Priya Patel")

    a.deposit(250)
    a.withdraw(100)
    a.transfer(b, 150)

    print(a.statement())
    print()
    print(b.statement())
