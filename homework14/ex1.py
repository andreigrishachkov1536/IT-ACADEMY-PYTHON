commands = []
first_str="\n"

while True:
    single_command = input("Введите команду: ")

    if single_command == "Выход":
        commands.append(single_command)
        break

    commands.append(single_command)

with open("log.txt", "w", encoding="utf-8") as file:
    file.write(first_str.join(commands) + "\n")