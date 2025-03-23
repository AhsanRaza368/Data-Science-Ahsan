# 1. Encapsulation Task (Secure Bank Account)
# Create a BankAccount class.
# It should have private attributes: __balance and __pin.
# Implement methods to deposit, withdraw, and check balance, ensuring the correct PIN is required for withdrawals.

class Bankaccount:
    def __init__(self,balance,pin):
        self.__balance = balance
        self.__pin = pin
        
    def deposit_balance(self,depositbalance):
        if depositbalance > 0 :
            self.__balance += depositbalance
            print(f"you balance is deposited \n your current balance is:{self.__balance}")
            
              
    def check_balance(self):
        pn = int(input("enter pin:"))
        if pn == self.__pin:
            print(f"your current balance is:{self.__balance}")
        else:
            print("invalid pin")
        
        
    def withdraw_balance(self,wd_amount):
        pn = int(input("enter pin:"))
        if pn == self.__pin:
            if wd_amount<=0:
                print("invalid ammount")
            
            elif self.__balance >= wd_amount:
                self.__balance -= wd_amount
                print(f"now balance is:{self.__balance}")
            else:
                print("insufficient balance")
        else:
            print("invalid pin")
            
obj = Bankaccount(200,234567890)
obj.deposit_balance(400)
obj.withdraw_balance(100)

    