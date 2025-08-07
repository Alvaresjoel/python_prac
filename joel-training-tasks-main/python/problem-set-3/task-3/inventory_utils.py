# Contains helper functions (e.g., calculate total inventory value, filter low stock items, etc.)


product_object = []
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

def low_stock_item(product_list):
    low_stock = []
    for item_obj in product_list :
        item = item_obj.retrieve_inventory()
        print(item)
        if item[2] < 25:
            low_stock.append(item)
    return low_stock