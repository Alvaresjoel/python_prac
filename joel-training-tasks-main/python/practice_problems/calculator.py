# perform addition of 2 positive numbers 
# main.py call add method from calculator


def sum_of_number(number1,number2):
    try:
        if number1 < 0 or number2 < 0:
            raise ValueError("Enter positive numbers only")
        # if number1 / 0:
        #     raise ZeroDivisionError
        sum = number1 + number2 
        

    except TypeError :
        return TypeError
    except ValueError :
        return ValueError
    except Exception as e :
        return e
    else :
            return sum