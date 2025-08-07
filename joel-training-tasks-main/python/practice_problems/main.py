import calculator as c

try:
    print(c.sum_of_number(13,123))
    print(c.sum_of_number(13,"123"))
    print(c.sum_of_number(13,-123))
    print(c.sum_of_number(13,11.2))
except Exception as e:
    print(e)