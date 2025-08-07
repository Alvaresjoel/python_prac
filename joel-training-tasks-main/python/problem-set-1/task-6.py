import random 
def guessing_game(random_number):
    print("Attempt No ",no_attempts+1)
    user_input = int(input("Enter Value:"))

    if user_input > 100 :
        return 'invalid value'
    elif user_input < 0 :
        return 'invalid value'

    if user_input == random_number:
        return 'Correct'
    elif user_input > random_number:
        return 'High'
    else :
        return 'Low'

    
no_attempts = 0
random_number = random.randint(1,100)

while no_attempts < 7:
    result = guessing_game(random_number)
    if result == 'Correct':
        print(result)
        exit() 
    elif result == 'High' or result == 'Low':
        no_attempts += 1
        print (result)
print("No of attempts over. Correct ans was ", random_number)
    


