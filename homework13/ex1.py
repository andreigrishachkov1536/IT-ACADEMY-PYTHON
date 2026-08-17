while True:

        chislo= input("Введите число от 0 до 100: ")
        if chislo=="exit":
            break
        try:
            chislo = int(chislo)

            if chislo > 100:
                print("Слишком большое число")
            elif chislo < 0:
                print("Слишком маленькое число")

            else:
                print(f"Число принято {chislo}")
                break

        except ValueError:
            print("Ошибка: введите число")













