from typing import overload


class Account:
    
    default_account_number = 1000_0000

    def __init__(self, owner, opening_balance, account_type="current",overdraft=False):
        if(account_type == "current"):
            self._overdraft = overdraft
            if(opening_balance < 25):
                raise Exception("Current accounts require an opening balance of at least €25")
        elif (account_type == "deposit"):
            self._overdraft = False
            if(opening_balance < 50):
                raise Exception("Deposit accounts require an opening balance of at least €50")

        self._balance = opening_balance
        #owner = customer 
        self._owner = owner
        self._account_number = Account.default_account_number
        Account.default_account_number = Account.default_account_number + 1
        self._account_type = account_type
        

    @property
    def account_type(self):
        return self._account_type

    #Can get the owner of a Bank Account, cant set
    #(no setter)
    @property
    def owner(self):
        return self._owner

    #getter
    @property
    def balance(self):
        return self._balance

    #account_number, account_type, overdraft can be read but not changed (set)
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def account_type(self):
        return self._account_type
    
    @property
    def overdraft_facility(self):
        return self._overdraft

    #withdraw and deposit

    def withdrawal(self, amount):
        #if the amount is less than the balance then make a withdrawl
        #if amount is greater than balance and no overdaft then no widthdrawl
        #if amount is greater than balance and has overdaft then widthdrawl
        
        if( (self._balance-amount) <= 0 ):
            if(self.overdraft_facility):
                self._balance = self._balance - amount
            else:
                pass
        else:
            self._balance = self._balance - amount
            return self.balance + amount

    def deposit(self, amount):
        self._balance = self._balance + amount
        return self.balance + amount

    def __repr__(self):
        #Account type, balance, Owner first name, owner last name, overdraft(yes/no), interest rate
        repr = f"{str(self._account_number).ljust(17)}"
        repr = repr + f"{self._account_type.capitalize().ljust(15)} €{str(self.balance).ljust(10)}"
        repr = repr + f"{self._owner.first_name + ' ' +self._owner.last_name.ljust(20)}"
        if(self._overdraft):
            repr = repr + f"    Yes" 
        else:
            repr = repr + "      No"
        if(self._balance > 10000):
            repr = repr + "      10%"
        else:
            repr = repr + "      2%"
        return repr