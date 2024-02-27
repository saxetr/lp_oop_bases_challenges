"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: int, weight: float):
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight


if __name__ == '__main__':
    tomato = Product('Tomato', 'Красный, как хвост дракона.', 75, 1.33)
    print('Информация о продукте: ')
    print(f'\t\tназвание = {tomato.name}')
    print(f'\t\tописание = {tomato.description}')
    print(f'\t\tцена = {tomato.price}')
    print(f'\t\tвес = {tomato.weight}')

