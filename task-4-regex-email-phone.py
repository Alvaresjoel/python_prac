import re
phone_number_pattern = re.compile('^[7-9][\\d]{9}')
email_id_pattern = re.compile('(^[a-z0-9.-_]+)@([a-z0-9._-]+)\.([a-zA-Z]+)$')

def check_phone_number(phone_number):
    if phone_number_pattern.match(phone_number):
        return "Valid Phone number."
    else:
        return "Invalid Phone number."

def check_email_id(email_id):
    if email_id_pattern.match(email_id):
        return "Valid email id."
    else:
        return "Invalid email id."

phone_number = input("Enter Phone number: ")
email_id = input("Enter email id: ")

print(check_phone_number(phone_number))
print(check_email_id(email_id))