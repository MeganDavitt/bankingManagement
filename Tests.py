from account import Account
import customer

new_customer1 = customer.Customer("Tom","Jones", "8420744F", "0875461234", "tom@gmail.com")
new_customer2 = customer.Customer("Tim","smith", "7945612G")



print(new_customer1.first_name, new_customer1.last_name, new_customer1.ppsn, new_customer1.id)
print(new_customer2.first_name, new_customer2.last_name, new_customer2.ppsn, new_customer2.id)

account1 = Account(new_customer1,200)
account2 = Account(new_customer2,200)

print(account1.owner) #<customer.Customer object at 0x00000286A93F6608>
print(account2.owner)

print("******"*20)

new_cust3 = customer.Customer("Tim","smith", "7945612G")


# def show_all_accounts(self):
        
    #     for acc in self._accounts: #FOR TEST
    #         print(acc)



# try:
#opening_balance = float(input("Enter opening balance: "))
#account3 = Account(new_cust3,opening_balance,"current",True)
#print("Opening balance:", account3.balance)
# print(account3)
#account3.withdrawal(150)
#print("After withdrawal:", account3.balance)

    #def add_account(self): #not working because properties cant be set?
        #print("Add a new account to the current list of accounts")
        #print("=========================================================")
        
        #first_name = input("Account holder's first name: ")
        #last_name = input("Account holder's last name: ")
        
        #account_type = input("Enter the account type: ")
        #opening_balance = input("Enter the opening balance amount: ")
        #overdraft = input("Overdraft facility: ")

        #customer = Customer(first_name, last_name)
        #new_account = Account(account_type, opening_balance, overdraft)
        #self._accounts.append(new_account)

from datastore import Datastore

data = Datastore()
data.create_accounts_and_customers()

customers = data.customers
accounts = data.accounts

for customer in customers:
    print(customer)

for acc in accounts:
    print(acc)