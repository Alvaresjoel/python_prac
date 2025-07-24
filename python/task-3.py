class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    
    
product_list = []
product1 = Product("Laptop", 1200.00)
product2 = Product("Smartphone", 800.00)
product_list.append(product1)
product_list.append(product2)

print("Product List:", product_list)