import csv
import re

with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for user in reader:
        email_valid = re.fullmatch(r"^[\w.-]+@[\w.-]+\.\w+$", user["email"])
        phone_valid = re.fullmatch(r"^\+375\d{9}$", user["phone"])

        if not email_valid or not phone_valid:
            print("Некорректные данные:")
            print("Имя:", user["name"])

            if not email_valid:
                print("  Некорректный email:", user["email"])

            if not phone_valid:
                print("  Некорректный телефон:", user["phone"])

            print()