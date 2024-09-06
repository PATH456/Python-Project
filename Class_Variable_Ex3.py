#Exercise 4: Bank Account Class

#Requirements:

    #Create a BankAccount class with instance variables account_holder and balance.
    #Add a class variable interest_rate that is the same for all accounts.
    #Add a method to apply interest to the balance (based on the class-level interest_rate).
    #Create a few accounts and apply interest, then print the updated balances.

class BankAccount:
    interest_rate = 0.08

    def __init__(self, account_holder, balance):
         self.account_holder = account_holder
         self.balance = balance
    def balance_update(self):
         self.balance += self.balance * BankAccount.interest_rate
         print(self.balance)
per1 = BankAccount("Peter", 120000)
per2 = BankAccount("Tom", 80000)
per3 = BankAccount("Lisa", 24679)

print("Account Holder's Information:'")
print("Name:", per1.account_holder,"," "Balance before interest:", per1.balance)
print("Name:", per2.account_holder,"," "Balance before interest:", per2.balance)
print("Name:", per3.account_holder,"," "Balance before interest:", per3.balance)

print("Account Holder's balance after interest: ")
per1.balance_update()
per2.balance_update()
per3.balance_update()










































    






















