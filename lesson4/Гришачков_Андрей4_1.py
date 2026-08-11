from random import randint
temp=randint(15,30)

if temp < 19:
    print(f"Включен обогрев. Текущая температура: [{temp}]")
elif temp > 25:
    print(f"Включено кондиционирование. Текущая температура:{temp} ")
else:
    print("Климат в норме. Кондиционер выключен")

