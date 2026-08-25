
class Car:
    def __init__(self, make, model, mileage):
        self.__make = make
        self.__model = model
        self.__mileage = mileage


    @property
    def mileage(self):
        return self.__mileage
    @mileage.setter
    def mileage(self, value):
        if value <0:
            raise ValueError("Пробег не может быть отрицательным")
        elif value < self.__mileage:
            raise ValueError(f"Пробег не может стать меньше чем был: Предыдущее значение {self.__mileage} > чем {value}(Скручивать некрасиво))")

        self.__mileage = value


car= Car("Tesla", "X", 1000)

car.mileage = 500
print(car.mileage)
