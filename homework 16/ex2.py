"""Небольшое задание именно на наследование и
переопределение методов. Создайте базовый класс:
Notification. У него должен быть метод: send(message).
Затем создайте:
● EmailNotification;
● SMSNotification;
● PushNotification.
Каждый класс должен по-своему реализовать send().
Проверить в цикле.
Дополнительное усложнение: добавить в Notification общий
атрибут recipient и использовать super().__init__() в дочерних
классах."""

class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self, message):
        print(f"Отправка нового уведомление: {message}")

class EmailNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)
    def send(self, message):
        print(f"Email для {self.recipient}: {message} ")

class SMSNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)
    def send(self, message):
        print(f"Sms для {self.recipient}: {message}")

class PushNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)
    def send(self, message):
        print(f"Push уведомление для {self.recipient}: {message}")

Notifications = [
    EmailNotification("test@gmail.com"),
    SMSNotification("+375111111111"),
    PushNotification("Andrey") ]

for notification in Notifications:
    notification.send("У вас новое сообщение")





