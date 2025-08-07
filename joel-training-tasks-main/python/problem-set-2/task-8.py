import string
def remove_punctuation(paragraph):
    for i in string.punctuation :
        paragraph = paragraph.replace(i,"")
    return paragraph


def unique_word(paragraph):
    
    new_string = remove_punctuation(paragraph)
    new_string = new_string.split()
    unique_word= set(new_string)
    return unique_word

paragraph = input().lower()
print(unique_word(paragraph))
