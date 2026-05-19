# Encapsulation

# public → normal (nome)
# _protected → “não mexa direto” (_nome)
# __private → mais protegido (__nome)

class BankAccount():
    def __init__(self, balance: float) -> None:
        self.__balance = balance  # private attribute

    def deposit(self, value: float) -> None:
        self.__balance += value

    def withdraw(self, value: float) -> None:
        if value > 0 and value <= self.__balance:
            self.__balance -= value

    def consultBalance(self) -> float:
        return self.__balance


account = BankAccount(1000)
print(f"Bank Account Update Balance: {account.consultBalance()}")
account.deposit(500)
print(f"Bank Account Update Balance: {account.consultBalance()}")
account.deposit(-500)
print(f"Bank Account Update Balance: {account.consultBalance()}")
account.withdraw(200)
print(f"Bank Account Update Balance: {account.consultBalance()}")
