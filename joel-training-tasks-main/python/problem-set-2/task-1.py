def summation_item(item_list):
    sum:int = 0
    for item_value in item_list.values():
        if not isinstance(item_value,int):
            return f'Invalid values present in dictionary'
        # if item_value < 0 :
        #     return f'Negative values present in dictionary'
        sum += item_value

    return sum

flag = True
item_list = {}
# while(flag): 
#     item_name = input("Enter Item name : ")
#     if item_name == "0":
#         break
#     item_value = int(input("Enter Item price : "))
#     item_list[item_name] = item_value


sum_item = summation_item(item_list)
print(sum_item)
item_list2 = {'apple':-100,'pear':200,'papaya':300}
sum_item = summation_item(item_list2)
print(sum_item)

