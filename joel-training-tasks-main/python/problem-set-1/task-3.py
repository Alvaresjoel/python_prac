def reverse_string(user_string):
    string_length = len(user_string)
    reverse_string = ""
    for i in range(string_length-1,-1,-1):
        reverse_string += user_string[i]
    
    return reverse_string

reverse = reverse_string("abcdef")
print(reverse)

reverse = reverse_string(" Hello World ")
print(reverse)