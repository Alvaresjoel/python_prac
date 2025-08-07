def calculator(number1,number2,operator):
    if operator == '+':
        ans = number1 + number2
    elif operator == '-':
        ans = number1 - number2
    elif operator == '*':
        ans = number1 * number2
    elif operator == '/':
        if number2 == 0:
            return("division not possible")
        else:
            ans = number1 / number2
            return ans           
    else: 
        return("invalid operator")
    return ans

result = calculator(100,200,"+")
print(result)

result = calculator(50,60,"-")
print(result)

result = calculator(10,20,"*")
print(result)

result = calculator(10,5,"/")
print(result)

result = calculator(10,5,"$")
print(result)

result = calculator(10,0,"/")


print(result)
