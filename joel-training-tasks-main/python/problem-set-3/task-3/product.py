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

