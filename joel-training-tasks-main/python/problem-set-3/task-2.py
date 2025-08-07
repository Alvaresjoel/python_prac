class Product :
    __product_id:int
    __name:str
    __quantity:int
    __price:int

    def __init__(self,id,name,quantity,price) :
        self.__product_id = id
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def __update_inventory(self,update_info):
        self.__quantity = update_info[0]
        self.__price = update_info[1]

    def retrieve_inventory(self) :
        return [self.__name,self.__price,self.__quantity]

    def stock_value(self):
        return self.__quantity * self.__price

    def get_value(self):
        return self.__quantity * self.__price

class PerishableProduct(Product):
    
    production_date : str

    def __init__(self,__product_id,name,quantity,price) :
        super().__init__(__product_id,name =name,quantity = quantity,price =price)
        self.production_date = 10
        

    def __update_inventory(self,update_info):
        self.__quantity = update_info[0]
        self.__price = update_info[1]

    def retrieve_inventory(self) :
        production_date = self.production_date
        perishable_product = super().retrieve_inventory()
        perishable_product.append(production_date)
        return perishable_product

    def stock_value(self):
        return super().stock_value()

    def get_value(self):
        return super().get_value()


product_object = []
sum_of_inventory = 0

def sum_of_inventory(product_list):
    sum = 0
    for item in product_list:
        sum += item.get_value()
    return sum

def object_product(object_list):
    product_list = []
    for item in object_list:
        product_list.append(item.retrieve_inventory())
    return product_list


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


print(f'Total value of inventory is: {sum_of_inventory(product_object)}')
print(f'All items are {object_product(product_object)}')
# print(product_object)

# print(product1.retrieve_inventory())
# print()

