def number_in_array(array1,array2,input_number):
    
    flag1 : bool = False
    flag2 : bool = False
    
    for item_array1 in array1: 
        if item_array1 == input_number:
            flag1 = True    
            break
    
    for item_array2 in array2:
        if item_array2 == input_number:
            flag2 = True
            break
            
    return [flag1,flag2]


array1 = [1,2,3,4,5,6,7,8,9]
array2 = [1,3,4,6,8,0,10]
input_number = int(input("Enter your number :"))

flag1,flag2 = number_in_array (array1,array2,input_number)

if flag1 == True and flag2 == True:
    print ('number found in both arrays')
elif flag1 == True and flag2 == False:
    print ('number found only in array 1')
elif flag1 == False and flag2 == True:
    print ('number found only in array 2')
else :
    print ('number not found in both arrays')