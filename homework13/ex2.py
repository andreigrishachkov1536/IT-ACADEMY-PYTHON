balance=input("Введите баланс счета")
summa_perevoda=input("Введите сумму перевода")
try:
    balance=float(balance)
    summa_perevoda=float(summa_perevoda)

    if summa_perevoda > balance:
        print("Ошибка: недостаточно средств на счёте.")
        exit()
    else:
        balance-=summa_perevoda
except ValueError:
    print("Ошибка,введите число")
else:
    print("Операция выполнена успешно")
    print(f"Ваш баланс: {balance}")
finally:
    print("Операция завершена")