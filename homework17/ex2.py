"""Разработайте систему отправки уведомлений
пользователям.
1. Создайте общий базовый интерфейс для уведомлений.
Отправка сообщения должна выполняться через
единый метод.
2. Реализуйте отдельные классы для:
○ Email;
○ SMS;
○ Push.
3. Каждый способ отправки должен иметь собственное
поведение.
4. Создайте функцию, которая получает список
уведомлений и отправляет через них одно сообщение.Функция должна работать с разными типами
уведомлений через полиморфизм, без проверки
конкретного класса объекта.
5. Добавьте возможность создавать уведомление
альтернативным способом из конфигурации, например
из словаря с настройками получателя.
6. Добавьте статический метод для проверки
корректности данных получателя.
7. Создайте собственную иерархию исключений для
ошибок системы уведомлений. Предусмотрите как
минимум:
○ некорректного получателя;
○ ошибку отправки уведомления.
8. Реализуйте __str__(), чтобы объекты уведомлений
имели понятное строковое представление."""
from abc import ABC,abstractmethod

class NotificationError(Exception):
    pass

class InvalidRecipientError(NotificationError):
    pass

class NotificationSendError(NotificationError):
    pass

class Notification(ABC):
    def __init__(self, recipient):
        if not self.validate_recipient(recipient):
            raise InvalidRecipientError(
                f"Некорректный получатель: {recipient}"
            )
        self.recipient = recipient

    @abstractmethod
    def send(self,message):
        pass

    @staticmethod
    @abstractmethod
    def validate_recipient(recipient):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.recipient}"

class EmailNotification(Notification):

    @staticmethod
    def validate_recipient(recipient):
        return "@" in recipient and "." in recipient


    def send(self,message):
        print(f"Email для {self.recipient}: {message}")


class SmsNotification(Notification):
    @staticmethod
    def validate_recipient(recipient):
        return recipient.startswith("+") and recipient[1:].isdigit()


    def send(self, message):
        try:
            print(f"Sms для {self.recipient}: {message}")
        except Exception as error:
            raise NotificationSendError(f"Ошибка отправки SMS: {error}")

class PushNotification(Notification):

    @staticmethod
    def validate_recipient(recipient):
        return len(recipient) > 0

    def send(self, message):
        try:
            print(f"Push уведомление для {self.recipient}: {message}")
        except Exception as error:
            raise NotificationSendError(f"Ошибка отправки SMS: {error}")

def send_to_all(notifications, message):
    for notification in notifications:
        try:
            notification.send(message)
        except NotificationSendError as error:
            print(error)

def create_notification(configuration):
    notification_type = configuration["type"]
    recipient = configuration["recipient"]

    if notification_type == "email":
        return EmailNotification(recipient)

    elif notification_type == "sms":
        return SmsNotification(recipient)

    elif notification_type == "push":
        return PushNotification(recipient)

    else:
        raise NotificationError(f"Неизвестный тип уведомления: {notification_type}")

notifications = [
    EmailNotification("andrei@example.com"),
    SmsNotification("+375291234567"),
    PushNotification("andrei_123")]

send_to_all(notifications,"У вас новое сообщение!")


print()

Conf = {
    "type": "email",
    "recipient": "andrei_test@example.com"}

notification = create_notification(Conf)

print(notification)
notification.send("У вас новое сообщение!")
