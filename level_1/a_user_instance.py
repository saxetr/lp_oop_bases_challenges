"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    u1 = User('Василий', 'test_user_1', 443, "+160-90")
    print('Информация о пользователе: ')
    print(f'\t\tимя = {u1.name}')
    print(f'\t\tюзернейм = {u1.username}')
    print(f'\t\tвозраст = {u1.age}')
    print(f'\t\tтелефон = {u1.phone}')

