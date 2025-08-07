def star_diagram(number):
    number += 1
    pattern : str = ""
    for row in range (1,number):
        for i in range(1,number - row):
            pattern += " "
        for i in range (2*row - 1):
            pattern += "*"
        pattern += "\n"

    for row in reversed(range(1,number-1)):
        for i in range(1,number - row):
            pattern += " "
        for i in range (2*row - 1):
            pattern += "*"
        pattern += "\n"

    return pattern

print(star_diagram(4))    