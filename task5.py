import re

email_id_pattern = re.compile('[a-zA-Z0-9]+@[a-zA-Z0-9.]+\.[a-zA-Z]+')

def find_all_email(paragraph):
    if(email_id_pattern.findall(paragraph)):
        return f"{email_id_pattern.findall(paragraph)}"
    else:
        return "No email found"
    
# paragraph = input("Enter a paragraph: ")

print(find_all_email("Here are some emails: alalal@domain.com, invalid-email@domain, infenf@.com,negative@redimail.com"))
print(find_all_email("Shivam raikar"))