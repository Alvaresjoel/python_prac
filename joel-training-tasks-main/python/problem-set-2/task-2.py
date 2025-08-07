def swap_element_list(element_list):
    
    list_length = len(element_list)
    if list_length < 2 :
        return f'No change : {element_list}'
    last_index = list_length -1 
    first_index = 0
    temporary : int = element_list[first_index]
    element_list[first_index] = element_list[last_index]
    element_list[last_index] = temporary

    return element_list


print(swap_element_list([1,2,3,4]))
print(swap_element_list([12, 35, 9, 56, 24]))
print(swap_element_list([12, 35]))
print(swap_element_list([12]))
