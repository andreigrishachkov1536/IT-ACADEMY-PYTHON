logs = [200, 200, 404, 500, 200]
has_error = False
for log in logs:
    if log == 500:
        print("Внимание! Обнаружена ошибка 500.")
        break
else:
    print("Вся база данных проверена успешно.")


# O(n)
# цикл пройдет линейно максимум шагов это len(logs)