MINUS_ONE : int = -1
def sum_of_digits(number):
    if number < 0:
        number = number * MINUS_ONE
    sum = 0
    while(abs(number) > 0):
        sum += number % 10
        number = int(number / 10)
    return sum

print(sum_of_digits(12345))
print(sum_of_digits(-525))