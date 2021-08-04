from customer import Customer
from account import Account

#first_name,last_name, ppsn, phone_number="", email_address=""

class Datastore:

    def __init__(self):
       
        self._accounts = []
        self._customers = []

    def create_accounts_and_customers(self):
        
        #customers
        cust1 = Customer("Tim","Smith", "7945612G", "0875002356","tim@gmail.com")
        cust2 = Customer("John","Murphy","4656791F", "098234576", "john@gmail.com")
        cust3 = Customer("Sally","Smith", "7945612X","043657223")
        cust4 = Customer("Pete","Woods","4458891F", "908764887", "pete@hotmail.com")
        cust5 = Customer("Susan","McDermott", "1235612G", "086377366", "susan@gmail.com")
        cust6 = Customer("Megan","Davitt","9997931P", "098776655")

        self._customers.append(cust1)
        self._customers.append(cust2)
        self._customers.append(cust3)
        self._customers.append(cust4)
        self._customers.append(cust5)
        self._customers.append(cust6)

        #make accounts
        acc1 = Account(cust1,300,"current",False)
        acc2 = Account(cust1,300,"deposit")
        acc3 = Account(cust2,100,"current",True)
        acc4 = Account(cust6,15000,"current",True)
        acc5 = Account(cust3,300,"current",False)
        acc6 = Account(cust4,50,"deposit")
        acc7 = Account(cust5,500,"current",False)

        self._accounts.append(acc1)
        self._accounts.append(acc2)
        self._accounts.append(acc3)
        self._accounts.append(acc4)
        self._accounts.append(acc5)
        self._accounts.append(acc6)
        self._accounts.append(acc7)       

       #append to list of accounts
        

    @property
    def accounts(self):
        return self._accounts

    @property
    def customers(self):
        return self._customers




