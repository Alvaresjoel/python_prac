def prime_number(starting_number,ending_number):
    prime_number = []
    if ending_number < starting_number : 
        return "Invalid format"

    if (starting_number < 0) or (ending_number < 0):
        return "Invalid format"
    if starting_number <= 1 :
        starting_number = 2
    for number in range(starting_number,ending_number):
        flag = True
        for i in range(2,number-1):
            if number % i == 0 :
                flag = False
                break
        if flag == True :
            prime_number.append(number)
    
    return prime_number

print(prime_number(1,10))
print(prime_number(10,20))
print(prime_number(30,20))
print(prime_number(0,20))
