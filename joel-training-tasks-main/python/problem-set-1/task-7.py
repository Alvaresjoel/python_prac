

def atm_menu():
    flag = True
    user_balance = 10000
    while flag == True :
        print("1. Check Balance \n 2. Deposit \n 3. Withdraw \n 4. Exit ")
        value = int(input(""))

        match value:
            case 1:
                print("Current Balance:" ,user_balance)
            case 2:
                amount_deposit = int(input("Enter Deposit amount:"))
                if amount_deposit < 0 :
                    print ("Invalid amount. Please enter a valid number.")
                else:
                    user_balance += amount_deposit
                    print ("Deposited successfully.")


            case 3: 
                amount_withdrawal = int(input("Enter Withdrawal amount:"))
                if amount_withdrawal < 0 :
                    print("Invalid amount. Please enter a valid number.")
                elif user_balance - amount_withdrawal < 0:
                    print("Insufficient balance!")
                else:
                    user_balance -= amount_withdrawal
                    print("Withdrawal successful.")
            case 4:
                exit()

            case _: 
                print("Invalid option. Please try again.")

atm_menu()