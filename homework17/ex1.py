"""Базовый класс Order. У заказа должны быть:
● номер;
● сумма;
● статус.
Реализуйте методы:
● pay()
● cancel()
Заказ нельзя отменить после оплаты. Если пользователь
пытается выполнить недопустимую операцию, должно
возникать собственное исключение: InvalidOrderStateError.
Создайте иерархию:
OrderError
└──
InvalidOrderStateError
● Добавьте __str__: Объект заказа должен красиво
отображаться: Заказ #1001: 250 EUR, статус: оплачено
● Добавьте __eq__:Два заказа считаются одинаковыми,
если у них одинаковый номер"""



class OrderError(Exception):
    pass

class InvalidOrderStateError(OrderError):
    pass

class Order:
    def __init__(self, number, summa, status="Создан"):
        self.number = number
        self.summa = summa
        self.status = status

    def __str__(self):
        return f"Заказ {self.number}: {self.summa} EUR, статус: {self.status} "

    def __eq__(self,other):
        if self.number == other.number:
            return f"Одинаковые заказы,заказ № {self.number} имеется в системе"

    def pay(self):
        if self.status == "Оплачено":
            raise InvalidOrderStateError(f"Заказ №{self.number} уже оплачен.")
        if self.status == "Отменен":
            raise InvalidOrderStateError(f"Нельзя оплатить отмененный Заказ №{self.number}")
        self.status = "Оплачен"

    def cancel(self):
        if self.status == "Оплачен":
            raise InvalidOrderStateError(
                f"Нельзя отменить оплаченный заказ #{self.number}."
            )

        if self.status == "отменён":
            raise InvalidOrderStateError(
                f"Заказ #{self.number} уже отменён."
            )

        self.status = "отменён"


order1 = Order(1001, 250)
order2 = Order(1001, 350)
order3 = Order(1002, 450)

print(order1)

order1.pay()

print(order1)
print(order1==order2)
try:
    order1.cancel()
except InvalidOrderStateError as error:
    print("Ошибка:", error)
order3.cancel()
print(order3)