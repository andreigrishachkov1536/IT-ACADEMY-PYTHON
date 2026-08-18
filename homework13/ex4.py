items = []
while True:
    command = input("Введите команду: ")

    try:
        if command == "add":
            items.append(int(input("Введите число")))
            print(items)

        elif command == "remove":
            index=int(input("Введите индекс"))
            items.remove(items[index])

        elif command == "show":
            print(items)
        elif command == "exit":
            break
        else:
            print("Неизвестная команда")

    except ValueError:
        print("Введено не числовое значение")
    except IndexError:
        print("Введено не корректный индекс")