from product import Product,PerishableProduct
import inventory_utils as utils
product_object = []

product1 = Product(123,'TV',10,30000)
product2 = Product(140,'Phone',30,25000)
product5 = PerishableProduct(123,'Apple',10,30)
product6 = PerishableProduct(140,'Pineapple',30,250)
product11= Product(120,'Macbook',20,75000)
product12= Product(103,'Lenovo-Legion',15,50000)

product_object.append(product1)
product_object.append(product2)
product_object.append(product5)
product_object.append(product6)
product_object.append(product11)
product_object.append(product12)

print(f'Total value of inventory is: {utils.sum_of_inventory(product_object)}')
print(f'All items are {utils.object_product(product_object)}')

print(f'The items with low stock are : {utils.low_stock_item(product_object)}')