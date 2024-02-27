"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income

    def decrease_balance(self, expense: float):
        if self.balance - expense >= 0:
            self.balance -= expense
        else:
            raise ValueError


if __name__ == '__main__':
    u1_acc = BankAccount('Ли Дзен Пин', 19200.9)
    u1_acc.decrease_balance(17)
    print(u1_acc.balance)
    u1_acc.decrease_balance(64999)
    print(u1_acc.balance)
