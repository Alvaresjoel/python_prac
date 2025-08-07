import re
def find_email(paragraph):
    email_pattern = r'[a-zA-Z0-9._+]{4,15}+@[a-zA-Z0-9.]+\.[a-zA-Z]+'
    if re.findall(email_pattern,paragraph):
        return re.findall(email_pattern,paragraph)
    else:
        return "No email found"

print(find_email("Here are some emails:"))
print(find_email("Here is a valid email: te@example.com"))
print(find_email("Here are some emails: alalal@domain.com, invalid-email@domain, infenf@.com,negative@redimail.com"))
    