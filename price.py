price = 100
discount = 5
price_with_discount = price - price*discount/100

print(price_with_discount)

def discounted (price, discount):
    price = abs(float(price))
    discount = abs (float(discount))
    if discount >=100:
        discount = price
    else:
        price_with_discount = price - (price*discount/100)
    return price_with_discount

p = discounted (100, 50)
print(p)

product = {"name":"Samsung Galaxy S10", "stock": 8, "price": 50, "discount":50}
# добавляю новый ключ в product - with discount
# в него передаем результат работы ф-ции
product['with_discount'] = discounted(product['price'], product['discount'])
print (product)

import statistics
def get_median(x):
    y = statistics.median (x)
    return y
z = get_median([5, 2, 1, 3, 4])
print (z)