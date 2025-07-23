import re
def validation(type,user_input):
    email_pattern = re.compile(r'^([a-zA-Z0-9.-_]+)@([a-zA-Z0-9.-_]+)\.([a-zA-Z]+)$')
    mobile_pattern = re.compile(r'^[7-9][0-9]{9}$')
    if type == 'email':
        if re.match(email_pattern,user_input):
            return 'Valid Email'
        else:
            return 'Invalid Email'
    else :
        if len(user_input) != 10:
            return 'Invalid Mobile Number'
        if re.match(mobile_pattern,user_input):
            return 'Valid Mobile Number'
        else:
            return 'Invalid Mobile Number'
        
print(validation('email', 'joel.alvares@creativecapsule.com'))
print(validation('mobile', '9876543210'))
print(validation('email', 'invalid-email@domain'))
print(validation('mobile', '1234567890'))
    