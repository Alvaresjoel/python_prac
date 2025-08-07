class BankAccount :
    __account_number:int
    __account_holder:str
    __balance:int = 0

    def __init__(self,account_number,account_holder):
        self.__account_number =  account_number
        self.__account_holder = account_holder

    def deposit(self,deposit_amount):
        if deposit_amount < 0 :
            return 'Enter Valid amount'
        self.__balance += deposit_amount
        return self.__balance


    def withdraw(self,withdraw_amount):
        if withdraw_amount < 0 :
            return 'Enter Valid amount'
        if withdraw_amount > self.__balance :
            return 'Insuffient Balance'
        self.__balance -= withdraw_amount
        return self.__balance

    def check_acc_balance(self,account_number):
        if self.__account_number == account_number :
            return self.__balance

    def display_balance(self):
        return self.__balance,self.__account_holder,self.__account_number

    def get_balance(self):
        return self.__balance
    def update_balance(self,new_balance):
        self.__balance = new_balance

class SavingsAccount(BankAccount):
    interest_rate:int

    def apply_interest(self,interest_rate):
        if interest_rate < 0 : 
            return 'Invalid value'
        balance  = self.get_balance()
        balance = balance + (balance * interest_rate)//100
        self.update_balance(balance)
        return 'Balance is updated'

user1 = SavingsAccount(132,"Joel Alvares")
print(user1.display_balance())
user1.deposit(500)
user1.withdraw(100)
print(user1.apply_interest(4))
print(user1.display_balance())
print(f'Balance is : {user1.check_acc_balance(132)}')

user2 = SavingsAccount(110,"Vaibhav Mhambrey")
print(user2.display_balance()) 
print(user2.deposit(-100))
print(user2.withdraw(1000))
print(user2.withdraw(-1000))
print(user2.display_balance()) 

