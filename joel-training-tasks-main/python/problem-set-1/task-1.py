DAYS_IN_YEAR = 365
def calculate_days(year):
    if not isinstance(year,int):
        return "Invalid input, please try again"
    if year < 0 :
        return "Invalid"
    no_of_days = year * DAYS_IN_YEAR
    return no_of_days

print(calculate_days(23))
print(calculate_days(0))
print(calculate_days(20))
print(calculate_days(-1))
print(calculate_days("123"))


# year = int(input())
# days = Calculate_Days(year)
# print(days)
# print(Calculate_Days(int(input("Enter year"))))
