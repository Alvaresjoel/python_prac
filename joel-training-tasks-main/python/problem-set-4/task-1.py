import string
import csv

def write_csv(user_name,user_email,user_age):
    try:
        with open('users.csv',mode = 'a',newline='') as user_file:
            user_writer = csv.writer(user_file,delimiter=',')
            user_writer.writerow([user_name,user_email,user_age])
    finally :
        user_file.close()    
def string_validation(user_name,user_email,user_age,):
    try:
        for char in user_name:
            if char in string.ascii_letters :
                continue
            else:
                raise ValueError('Invalid Name')
        if user_age < 0 or not isinstance(user_age,int) :
            raise ValueError('Invalid age value')    
        if '@' not in user_email or '.' not in user_email:
            raise ValueError('Invalid email')
        write_csv(user_name,user_email,user_age)
        print("User saved to users.csv")
    
    except ValueError as e:
        print(e)
    except SyntaxError as s:
        print('Invalid syntax',s)
    except TypeError as t:
        print('Invalid value type provided as input:',t)
    
user_name = "joel"
user_email = "alvares@gmail.com"
user_age = 12
value =string_validation(user_name,user_email,user_age)
value =string_validation("vaibhav","vaibhav_mhambrey@gmail.com",20)
value =string_validation("cabru","cabrugmail.com",15)
value =string_validation("aaron","aaron@gmail.com",15)
