import csv


products=[]
count=0
with open("data.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        products.append(row)
print("Все товары:")
for product in products:
    print(product["name"])

cost_more500=[]
for product in products:
    if int(product["price"]) > 500:
        cost_more500.append(product)
        count+=1
print("Товары дороже 500")
for product in cost_more500:
    print(product["name"], product["price"])

print(f"Товаров дороже 500 - {len(cost_more500)}")

most_price = max(products, key=lambda product: int(product["price"]))
print(f"Самый дорогой товар: {most_price["name"]} стоимостью - {most_price["price"]}")





