from random import randint
a=randint(1,50)
for i in range(5):
    b=int(input(f"Попытка № {i+1}: Введите число "))
    if a==b:
        print("Ура вы угадали")
        break
    elif a>b:
        print("Больше")
    elif a<b:
        print("Меньше")
else:
    print(f"Загаданное число {a}")



