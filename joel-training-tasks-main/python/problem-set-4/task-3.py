import math

def age_validation(user_age):
    try:
        if(float(user_age)):
            raise TypeError
        if user_age < 0 : 
            raise Exception("Age must be positive number")
        if user_age > 120 or user_age < 1:
            raise Exception("Enter age between 1 to 120")
        if math.floor(user_age) != user_age:
            raise Exception("Please enter a whole number.")
        else:
            print(f"user age : {user_age} is accepted")
    except TypeError as t:
        raise t
    except ValueError as val:
        raise val
    except Exception as e:
        raise e




try:
    age_validation('22.5')
except NameError:
    print('Invalid variable name')
except ValueError as val:
    print(f'Enter a positive number only : {val}')
except TypeError as t :
    print(f'Enter number only')
except Exception as e:
    print(e)