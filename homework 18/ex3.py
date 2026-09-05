from abc import ABC,abstractmethod

class DiscountStrategy(ABC):

    @abstractmethod
    def calculate(self, price):
        pass

class RegularDiscount(DiscountStrategy):

    def calculate(self, price):
        return price * 0.05

class CustomerDiscount(DiscountStrategy):

    def calculate(self, price):
        return price * 0.10

class VIPDiscount(DiscountStrategy):

    def calculate(self, price):
        return price * 0.20

class BirthdayDiscount(DiscountStrategy):

    def calculate(self, price):
        return price * 0.15

class PromoDiscount(DiscountStrategy):

    def calculate(self, price):
        return price * 0.25

class Order:

    def __init__(self, price, discount_strategy):
        self.price = price
        self.discount_strategy = discount_strategy

    def calculate_discount(self):
        return self.discount_strategy.calculate(self.price)

    def final_price(self):
        return self.price - self.calculate_discount()

DISCOUNTS = {
    "regular": RegularDiscount,
    "customer": CustomerDiscount,
    "vip": VIPDiscount,
    "birthday": BirthdayDiscount,
    "promo": PromoDiscount,
}

price = 100
discount_type = "vip"
strategy = DISCOUNTS[discount_type]()
order = Order(price, strategy)

print("--- ORDER ---")
print(f"Цена: {price}")
print(f"Скидка: {order.calculate_discount()}")
print(f"Итого: {order.final_price()}")