"""Implementation of Bank|Account class"""
class BankAccount:

    def __init__(self, balance):
        if balance < 0:
            raise ValueError('You have a debit on your account')

    def withdraw(self, ammount):
        if  balance - ammount < 0:
            raise ValueError('You cannot withdraw more money than you have!')
        else:
            return self.balance - ammount()


    def deposit(self, ammount):
        return self.balance + self.ammount()

money = BankAccount(100)
withdraw = money.withdraw(50)

