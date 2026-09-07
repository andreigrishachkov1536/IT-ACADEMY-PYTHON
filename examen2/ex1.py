"""1. Базовый класс Warrior — 2 балла
Создайте класс Warrior.
Атрибуты
При создании объекта:
● _health = 30 — здоровье;
● attack = 5 — сила атаки.
Доступ к здоровью должен осуществляться через свойство health.
Свойства
Реализуйте:
● health — геттер возвращает текущее здоровье;
● setter health не должен позволять установить отрицательное
значение;
● is_alive — возвращает True, если здоровье больше 0,
иначе False.
Здоровье воина не может быть отрицательным.
Методы
Реализуйте:
take_damage(damage)
Метод уменьшает здоровье воина на величину damage. Здоровье не
может стать меньше 0.
Реализуйте:
attack_target(target)
Метод атакует другого воина target, нанося ему урон, равный
attack.
Метод должен использовать поведение объекта target, а не
изменять его health напрямую.
2. Наследники Fighter, Mage, Paladin — 2 балла
Создайте три класса-наследника класса Warrior.
Fighter
● наследуется от Warrior;
● attack = 7.
Других изменений в поведении нет.
Mage
● наследуется от Warrior;
● имеет атрибут magic = 6;● получаемый магом урон уменьшается на magic, но не может
стать отрицательным.
Например:
Mage получает 10 урона → получает 4 урона.
Mage получает 5 урона → получает 0 урона.
При атаке:
● если target.attack < magic, маг наносит attack +
magic;
● иначе маг наносит только attack.
Paladin
● наследуется от Warrior;
● начальное здоровье — 50;
● attack = 6.
После успешной атаки паладин восстанавливает себе здоровье в
размере 20% от нанесённого урона.
Максимальное здоровье паладина не должно превышать его
начальное значение — 50.
3. Строковое представление и дуэль — 1 балл
Для всех классов реализуйте метод для строкового представления.
Формат:
ИмяКласса, HP: <здоровье>, ATK: <атака>
Для мага:
Mage, HP: 30, ATK: 5, MAG: 6
Реализуйте функцию:
fight(unit1, unit2)
Функция проводит бой двух воинов:
1. первым атакует unit1;
2. затем unit2;
3. бой продолжается до смерти одного из воинов;
4. если после атаки первый воин умер, второй не атакует;
5. функция возвращает True, если победил unit1, иначе False.
Важно: в функции fight() нельзя проверять конкретные типы
воинов через isinstance(). Боевая логика должна определяться
методами самих классов.4. Перегрузка операторов для Warrior — 1 балл
Реализуйте операторы + и *.
Сложение
Выражение:
stronger = warrior + 2
должно вернуть нового воина, у которого:
● здоровье увеличено на 2;
● атака увеличена на 2.
Исходный объект изменяться не должен.
Умножение
Выражение:
stronger = warrior * 2
должно вернуть нового воина, у которого:
● здоровье умножено на 2;
● атака умножена на 2.
Исходный объект изменяться не должен.
Операторы должны корректно работать с наследниками Warrior.
5. Класс Army — 1 балл
Создайте класс Army, содержащий список воинов.
Реализуйте метод:
add_members(unit_class, count)
который добавляет в армию count экземпляров переданного
класса.
Например:
army.add_members(Fighter, 3)
army.add_members(Mage, 2)
army.add_members(Paladin, 1)
В результате армия содержит 6 воинов.
Итерация
Реализуйте:
__iter__()
__len__()
__getitem__()
Должны поддерживаться операции:for warrior in army:
print(warrior)
len(army)
army[0]
army[1:3]
6. Операторы + и * для Army — 1 балл
Реализуйте операторы + и * для класса Army.
Например: stronger_army = army + 5
должен вернуть новую армию, в которой у каждого воина:
● здоровье увеличено на 5;
● атака увеличена на 5.
Выражение: stronger_army = army * 2
должно вернуть новую армию, в которой у каждого воина:
● здоровье умножено на 2;
● атака умножена на 2.
●
Исходная армия не должна изменяться.
Типы воинов и их дополнительные характеристики (magic у мага и
т.
п.) должны сохраняться.
7. Сериализация — 1 балл
Добавьте каждому воину методы: to_dict() и from_dict()
Для каждого воина необходимо сохранять как минимум:
● тип воина;
● здоровье;
● атаку;
● дополнительные характеристики, если они есть.
Например, маг может быть представлен следующим образом:
{
"type": "Mage",
"health": 25,
"attack": 5,
"magic": 6
}Для Army реализуйте: save_to_file(filename) и
load_from_file(filename)
Методы должны сохранять и загружать состав армии в формате
JSON. После загрузки должны восстанавливаться правильные типы
объектов:
Fighter → Fighter
Mage → Mage
Paladin → Paladin
8. Характеристики армии — 1 балл
Добавить свойства:
total_health
total_attack
alive_members
Например:
army.total_health
army.total_attack
army.alive_members
где:
● total_health — суммарное здоровье всех бойцов;
● total_attack — суммарная атака;
● alive_members — количество живых бойцов."""
import copy
import json
#--------------1--------------
class Warrior:
    attack = 5
    start_health = 30
    def __init__(self):
        self._health = self.start_health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Здоровье не может быть отрицательным")

        self._health = value

    @property
    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        if damage < 0:
            damage = 0

        old_health = self.health
        self.health = self.health - damage

        if self.health < 0:
            self.health = 0

        return old_health - self.health

    def attack_target(self, target):
        target.take_damage(self.attack)

# --------------3 задание кусок тут---------------
    def __str__(self):
            return f"{self.__class__.__name__}, HP: {self.health}, ATK: {self.attack}"

#--------------половина 4 задания--------------
    def __add__(self, value):
        new_warrior = copy(self)
        new_warrior.health = self.health + value
        new_warrior.attack = self.attack + value

        return new_warrior

    #* не понял крч с dict

    @classmethod
    def from_dict(cls, data):
        warrior_class = WARRIOR_TYPES[data["type"]]
        warrior = warrior_class()
        warrior.health = data["health"]
        warrior.attack = data["attack"]

        if "magic" in data:
            warrior.magic = data["magic"]

        return warrior

#--------------2--------------
class Fighter(Warrior):
    attack = 7

class Mage(Warrior):
    attack = 5
    magic = 6

    def take_damage(self, damage):
        damage = damage - self.magic
        if damage < 0:
            damage = 0

        return super().take_damage(damage)

    def attack_target(self, target):
        if target.attack < self.magic:
            damage = self.attack + self.magic
        else:
            damage = self.attack

        target.take_damage(damage)

    def __str__(self):
        return (
            f"Mage, "
            f"HP: {self.health}, "
            f"ATK: {self.attack}, "
            f"MAG: {self.magic}"
        )

class Paladin(Warrior):
    start_health = 50
    attack = 6

    @Warrior.health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Здоровье не может быть отрицательным")

        if value > self.start_health:
            value = self.start_health

        self._health = value

    def attack_target(self, target):
        damage_dealt = target.take_damage(self.attack)

        if damage_dealt > 0:
            self.health += damage_dealt * 0.2



WARRIOR_TYPES = {
    "Warrior": Warrior,
    "Fighter": Fighter,
    "Mage": Mage,
    "Paladin": Paladin
}

#--------------3--------------
def fight(unit1, unit2):
    while unit1.is_alive and unit2.is_alive:

        unit1.attack_target(unit2)

        if not unit2.is_alive:
            break

        unit2.attack_target(unit1)

    return unit1.is_alive

#--------------5 задание--------------
class Army:

    def __init__(self):

        self.members = []

    def add_members(self, unit_class, count):
        for _ in range(count):
            self.members.append(unit_class())

    def __iter__(self):
        return iter(self.members)

    def __len__(self):
        return len(self.members)

    def __getitem__(self, index):
        return self.members[index]

    # --------------6 задание--------------

    def __add__(self, value):
        new_army = Army()

        for warrior in self.members:
            new_army.members.append(warrior + value)

        return new_army


    def __mul__(self, value):
        new_army = Army()

        for warrior in self.members:
            new_army.members.append(warrior * value)

        return new_army

    # --------------7 задание--------------

    def save_to_file(self, filename):
        data = [warrior.to_dict() for warrior in self.members]

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data,file)

    def load_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.members = [Warrior.from_dict(item) for item in data]

    # --------------8 задание--------------
    @property
    def total_health(self):
        return sum(warrior.health for warrior in self.members)

    @property
    def total_attack(self):
        return sum(warrior.attack for warrior in self.members)

    @property
    def alive_members(self):
        return sum(warrior.is_alive for warrior in self.members)




# warrior = Warrior()
# fighter = Fighter()
# mage = Mage()
# paladin = Paladin()

# print(warrior)
# print(fighter)
# print(mage)
# print(paladin)
#
#
# mage.take_damage(3)
# print(mage.health)
#
# mage.attack_target(warrior)
#
# print(warrior.health)



# paladin.health = 40
#
# paladin.attack_target(warrior)
#
# print(warrior.health)
# print(paladin.health)
#
# army = Army()
#
# army.add_members(Fighter, 2)
# army.add_members(Mage, 2)
# army.add_members(Paladin, 1)
#
# print(len(army))
# for warrior in army:
#     print(warrior)
