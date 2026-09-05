"""Создайте класс Item, представляющий предмет в инвентаре
персонажа.
Каждый предмет имеет:
● name — название;
● weight — вес;
● price — стоимость.
Необходимо перегрузить операторы:
● + — объединяет два предмета в «набор» и возвращает
их общую стоимость;
● < — сравнивает предметы по весу;
● == — считает предметы одинаковыми, если совпадают
их названия;
● str() — выводит предмет в удобном формате."""

class Item:
    def __init__(self, name:str, weight:float, price:float):
        self.name = name
        self.weight = weight
        self.price = price

    def __add__(self, other):
        return f"Общая стоимость {self.name} и {other.name} = {self.price + other.price}"

    def __lt__(self, other):
            return f"Объект {self.name} легче чем {other.name}" if self.weight < other.weight else f"Объект {self.name} тяжелее чем {other.name}"

    def __eq__(self, other):
            return "Предметы одинаковы" if self.name == other.name else "Предметы разные"

    def __str__(self):
        return f"{self.name} весом {self.weight} килограмм и стоимостью {self.price} $"

class Inventory:
    def __init__(self, items:list=None):
        self.items = items if items is not None else []

    def __add__(self, item):
        return Inventory(self.items + [item])

    def __str__(self):
        if not self.items:
            return "Инвентарь пуст"

        return "\n".join(str(item) for item in self.items)


Sword=Item("Меч Катана", 20, 100)
Sword2=Item("Меч Каратель", 20, 300)
Shield=Item("Shield", 15, 200)
result = Sword + Shield
print(result)
result= Sword<Shield
print(result)
result = Sword==Sword2
print(result)
print(Sword)

inventory = Inventory([Sword, Shield])
new_inventory = inventory + Sword2
print("Новый инвентарь:\n",new_inventory)