import datetime

user_time = "00:50"
try:
    datetime.datetime.strptime(user_time, "%H:%M")
    print("Valid time format.")
except ValueError:
    print("Invalid time format. Please use HH:MM.")
    exit()
