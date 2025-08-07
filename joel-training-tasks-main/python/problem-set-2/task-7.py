class Product :
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        return f'Product name :{self.name}, Product price : {self.price} , Product category : {self.category}'
        
    

def find_maximum_price(product_list):
    max_product : str = ""
    max_price : int = 0

    for product in product_list:
        if product.price > max_price :
            max_product = product
    
    return max_product

def search_categories(categories):
    categories_list = []
    for item in product_list:
        if item.category == categories : 
            categories_list.append(item)

    return find_maximum_price(categories_list)


product_list = []
# while True :
#     name = input("Enter name : ")
#     if name == '0':
#         break
#     price = int(input("Enter price : "))
#     category = input("Enter category : ")
#     new_product = Product(name,price,category)
#     product_list.append(new_product)
product1 = Product("Phone",30000,"Electronics")
product_list.append(product1)
product2 = Product("Pen",30,"Stationery")
product_list.append(product2)
product3 = Product("Laptop",60000,"Electronics")
product_list.append(product3)
product4 = Product("TV",30000,"Electronics")
product_list.append(product4)
product5 = Product("Microwave",10000,"Electronics")
product_list.append(product5)
product6 = Product("Book",200,"Stationery")
product_list.append(product6)
product7 = Product("Apple",60,"Fruit")
product_list.append(product7)
product8 = Product("Papaya",100,"Fruit")
product_list.append(product8)


categories = input ("Enter ")
product = search_categories (categories)
print(f'The max price of {categories} is {product.name} with Price : {product.price}')

