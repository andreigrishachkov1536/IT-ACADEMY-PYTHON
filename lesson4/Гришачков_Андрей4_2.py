sum=int(input("Введите сумму покупки"))
zona=input("Введите клиентскую зону (RU,EU,US)")
if zona=="RU":
    if sum > 5000:
        dilivery=0
    else :
        dilivery=500
elif zona=="EU":
     dilivery=1000
elif zona=="US":
    if sum > 15000:
        dilivery=800
    else :
        dilivery=2000

total_price=sum+dilivery
print(f"Итоговая стоимость = {total_price}")