from db import Base, engine

from crud import (
    create_user,
    get_users,
    create_order,
    get_orders,
    get_user_by_id,
    get_user_orders,
    update_order_status,
    delete_order,
    find_order
)

Base.metadata.create_all(engine)

def show_menu():
    print("\n" + "=" * 40)
    print("             МАГАЗИН")
    print("=" * 40)

    print("1. Создать пользователя")
    print("2. Показать пользователей")
    print("3. Создать заказ")
    print("4. Показать все заказы")
    print("5. Показать мои заказы")
    print("6. Изменить статус заказа")
    print("7. Удалить заказ")
    print("8. Найти заказ")
    print("0. Выход")

    print("=" * 40)

def add_user():
    name = input("Введите имя: ")
    email = input("Введите email: ")

    if not name or not email:
        print("Имя и email не должны быть пустыми")
        return

    create_user(
        name,
        email
    )

def show_all_users():
    users = get_users()
    if not users:
        print("Пользователей нет.")
        return
    print("\n--- Пользователи ---")

    for user in users:
        print(user)

def add_order():
    try:
        user_id = int(input("Введите ID пользователя: "))
    except ValueError:
        print("ID должен быть числом")
        return

    product = input("Введите название товара: ")
    if not product:
        print("Название товара не должно быть пустым")
        return

    create_order(
        user_id,
        product
    )


def show_all_orders():
    orders = get_orders()

    if not orders:
        print("Заказов нет")
        return

    print("\n--- Все заказы ---")

    for order in orders:
        print(order)


def show_my_orders():
    try:
        user_id = int(
            input("Введите ID пользователя: "))
    except ValueError:
        print("ID должен быть числом")
        return

    user = get_user_by_id(user_id)

    if not user:
        print("Пользователь не найден.")
        return

    orders = get_user_orders(user_id)

    print(f"\n--- Заказы пользователя {user.name} ---")

    if not orders:
        print("Заказов нет.")
        return

    for order in orders:
        print(order)


def change_status():
    try:
        order_id = int(input("Введите ID заказа: "))
    except ValueError:
        print("ID должен быть числом.")
        return

    print("\nВыберите новый статус:")
    print("1. Новый")
    print("2. В обработке")
    print("3. Выполнен")
    print("4. Отменён")

    choice = input("Ваш выбор: ")

    statuses = {
        "1": "Новый",
        "2": "В обработке",
        "3": "Выполнен",
        "4": "Отменён"
    }

    if choice not in statuses:
        print("Неверный выбор.")
        return

    update_order_status(order_id,statuses[choice])


def remove_order():
    try:
        order_id = int(input("Введите ID заказа: "))
    except ValueError:
        print("ID должен быть числом.")
        return

    delete_order(order_id)


def search_order():
    try:
        order_id = int(
            input("Введите ID заказа: ")
        )
    except ValueError:
        print("ID должен быть числом.")
        return

    order = find_order(order_id)

    if not order:
        print("Заказ не найден.")
        return

    print("\n--- Найденный заказ ---")
    print(order)


def main():
    while True:

        show_menu()

        choice = input(
            "Выберите действие: "
        )

        if choice == "1":
            add_user()

        elif choice == "2":
            show_all_users()

        elif choice == "3":
            add_order()

        elif choice == "4":
            show_all_orders()

        elif choice == "5":
            show_my_orders()

        elif choice == "6":
            change_status()

        elif choice == "7":
            remove_order()

        elif choice == "8":
            search_order()

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()