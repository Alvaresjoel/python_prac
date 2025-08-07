def count_sum_of_2(element_list,target):

    if len(element_list) > 104 or len(element_list) < 2:
        return "Invalid length"
    if target > 109 or target < -109:
        return "Invalid target"
    for item in element_list :
        if item < -109 or item > 109 :
            return "Invalid array"
    for i in range (0,len(element_list)):
        for j in range(i+1,len(element_list)):
            if element_list[i] + element_list[j] == target :
                return [i,j]
    return "sum not possible"            


print(count_sum_of_2([1,2,3,4,5,6],30))

element_list = [3,2,4]
target = 6 
print(count_sum_of_2(element_list,target))

element_list = [3,3]
target = 6
print(count_sum_of_2(element_list,target))
