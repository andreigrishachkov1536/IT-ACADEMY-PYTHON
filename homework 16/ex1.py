"""Создайте класс BankAccount, который представляет банковский счёт. У объекта должны быть:
owner — имя владельца; _balance — текущий баланс. Реализуйте методы:
● deposit(amount) — пополнение счёта;
● withdraw(amount) — снятие денег;
● get_balance() — получение текущего баланса.
Правила:
● нельзя пополнить счёт на отрицательную или нулевую сумму;
● нельзя снять отрицательную или нулевую сумму;
● нельзя снять больше денег, чем есть на счёте.
Замените get_balance() на property, чтобы баланс можно было получать так: BancAccount.balance"""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Сумма пополнения должна быть больше 0")

        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Сумма снятия должна быть больше 0')

        if amount > self.balance:
            raise ValueError('Недостаточно средств на балансе для снятия')

        self._balance -= amount

    @property
    def balance(self):
        return self._balance

account1=BankAccount("Andrei", 500)
account1.deposit(1100)
account1.withdraw(800)
print(account1.balance)




