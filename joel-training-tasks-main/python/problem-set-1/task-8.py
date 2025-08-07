NORMALISATION_VALUE = 86
def sum_of_character(sentence):

    new_sentence = sentence.lower()
    sum = 0

    for char in new_sentence :
        if char == " ":
            continue
        else:
            value = ord(char)
            sum += value - NORMALISATION_VALUE    

    print(sum)



sum_of_character("Test")
sum_of_character("Hello World")
sum_of_character("Test Test")