shop_list = ["хлеб", "молоко"]
fake_copy = shop_list
true_copy = shop_list.copy()
fake_copy.append("сыр")
true_copy.remove("хлеб")
print(f"Сравнение shop_list и fake copy = {shop_list is fake_copy} \nshop_list и true_copy = {shop_list is true_copy},\n и их id shop_list: {id(shop_list)}\n id fake_copy: {id(fake_copy)}\n id true_copy: {id(true_copy)}")
print(shop_list)
print(fake_copy)
print(true_copy)