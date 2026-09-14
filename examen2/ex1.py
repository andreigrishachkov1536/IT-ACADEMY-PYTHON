import copy
import json
#--------------1--------------
class Warrior:
    def __init__(self):
        self._health = 30
        self.attack = 5

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
    def __init__(self):
        super().__init__()

class Mage(Warrior):
    def __init__(self):
        super().__init__()
        self.magic = 6


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




warrior = Warrior()
fighter = Fighter()
mage = Mage()
paladin = Paladin()

print(warrior)
print(fighter)
print(mage)
print(paladin)


mage.take_damage(3)
print(mage.health)

mage.attack_target(warrior)

print(warrior.health)



paladin.health = 40

paladin.attack_target(warrior)

print(warrior.health)
print(paladin.health)

army = Army()

army.add_members(Fighter, 2)
army.add_members(Mage, 2)
army.add_members(Paladin, 1)

print(len(army))
for warrior in army:
    print(warrior)
