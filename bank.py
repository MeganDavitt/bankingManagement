import os
from customer import Customer
from account import Account

class Bank:

    def __init__(self,datastore):

        self._accounts = datastore.accounts
        self._customers = datastore.customers

    def clearscreen(self):
        os.system('cls')



    def do_user_menu(self):

        selection = "0"

        while(selection != "e"):
            self.clearscreen()
            selection = self.show_user_menu()

            if(selection not in ["1", "2", "3","4","5","6","7","8","e"]):
                self.clearscreen()
                print(f"Invalid menu option [{selection}]. Press return to try again.")
                input()

    def show_user_menu(self):

        print(f"WELCOME TO THE BANK")
        print("------------------------------")
        print("Menu options:")
        print("1. View existing Customers")
        print("2. View all customer Accounts")
        print("3. Search for customers by PPSN")
        print("4. Make customer Deposit")
        print("5. Make customer Withdrawal")
        print("6. Transfer money")
        print("7. Add a new customer")
        print("8. On-screen help and assistance")

        #print("9. Add a new account") <---- not working 

        
        print("e. Exit\n")
        selection = input("Please choose an option (1-8): ")

        if(selection == "1"):
            self.view_customers()

        elif(selection == "2"):
            self.view_accounts()

        elif(selection == "3"):

            search_ppsn = input("Enter PPSN number: ")

            customer = self.search_for_ppsn(search_ppsn)
            if( customer != None):
                self.show_customer_accounts(customer)
            else:
                print("\nNo customer with that PPSN found, here is our current list of customers.")
                self.view_customers()

        elif(selection == "4"):
            print("Here is a list of accounts currently on file:")
            print("=========================================================================================")
            account = self.view_accounts()
            account = self.find_account()
            
            if( account == None):
                
                print("Please re-check customers details")

            else:
                print(account)
                print("=========================================================================================")
                print("To Make a Customer Deposit")
                print("=========================================================================================")
        

                amount = self.get_amount()
                self.account_deposit(account, amount)
            
            print("\nHere is the updated list of accounts:")
            self.view_accounts()



        elif(selection == "5"):
            print("Here is a list of accounts currently on file:")
            print("=========================================================================================")
            self.view_accounts()
            account = self.find_account()

            if( account == None):
                print("Please re-check customer's details")
            
            else:
                print("To Make a Customer Withdrawal")
                print("=========================================================================================")
                amount = self.get_amount()
                self.account_withdrawal(account, amount)
            
            print("\nHere is the updated list of accounts:")
            self.view_accounts()

        
        elif(selection == "6"):
            print("Here is a list of accounts currently on file:")
            print("=========================================================================================")
            self.view_accounts()
            account = self.find_account()
            if(account == None):
                print("This account number does not exist, please re-check customer details")
            
            else:
                print("How much money would you like to transfer")
                print("=========================================================================================")
                amount = self.get_amount()
                self.account_withdrawal(account, amount)
                print("Please enter the recipient account number below")
                account = self.find_account()
                print(account)
                print("=========================================================================================")
                self.account_deposit(account, amount)
            
            print("\nHere is the updated list of accounts:")
            self.view_accounts()
        
        elif(selection == "7"):
            
            customer = self.add_customer()
            print("you have successfully added a new customer")
            self.view_customers()
            print(f"Press Enter to continue")
            input()

        elif(selection == "8"):
            self.on_screen_help()
            

        
        
        #elif(selection == "8" ):
            #account = self.add_account() <------ not working 
            #print(account)
            #self.view_accounts()
            #print(f"Press Enter to continue")
            #input()

        elif(selection == "e"):
            print("Goodbye!")
            

        return selection

    def view_customers(self):
        print(f"{'Customer ID'.ljust(10)} |{'Name'.ljust(20)}|{'PPSN'.ljust(10)}|{'Phone'.ljust(10)}|{'Email'.ljust(30)}")
        print("**************************************************************************")
        for customer in self._customers:
            print(customer)

        print("Return to continue...")
        input()   

    def view_accounts(self):

        print(f"{'Account number:'.ljust(17)} {'Account type:'.ljust(13)} {'Balance:'.ljust(10)} {'Owner:'.ljust(20)} {'Overdraft:'.ljust(10)} {'Interest rate:'.ljust(10)}  ") 
        print("=========================================================================================")

        for acc in self._accounts:
           print(acc)

        print("Return to continue...")
        input()

    def search_for_ppsn(self, ppsn):
        if(len(ppsn) <= 7):
            
            print("Customer's PPSN must have 8 characters")
            print("Return to continue...")
            input()
        
        for customer in self._customers:
            if ppsn == customer.ppsn:
                return customer        
        return None

    def show_customer_accounts(self, customer):    

        this_customer_accounts = []

        for acc in self._accounts:
            if acc.owner.ppsn == customer.ppsn:
                this_customer_accounts.append(acc)

        print(f"{'Owner'.ljust(10)}  {'Account'.ljust(15)} {'PPSN'.ljust(10)} {'Number'.ljust(10)}  {'Overdraft'.ljust(15)} {'Interest'.ljust(2)}  ") 
        print("------------------------------------------------------------------------------------------------------")
        cust_details = "" 
        for acc in this_customer_accounts:
            cust_details = cust_details + f"{(customer.first_name + ' ' + customer.last_name).ljust(15)}"
            cust_details = cust_details + f"{acc._account_type.capitalize().ljust(10)}"
            cust_details = cust_details + f"{str(customer.ppsn).ljust(10)} {str(acc.account_number).ljust(10)}"
    
            if(acc.overdraft_facility):
                cust_details = cust_details + "        Yes " 
            else:
                cust_details = cust_details + "        No  "
            if(acc._balance > 10000):
                cust_details = cust_details + "        10%"
            else:
                cust_details = cust_details + "        2%"
            cust_details = cust_details + "\n"

           
        print(cust_details)        

        
        print("Return to continue...")
        input() 


    def add_customer(self):
        print("Add a new Customer to the current customer list")
        print("======================================================\n")
        first_name = input("Forename: ")
        if(len(first_name) <= 2):
            
            print("Customer's first name should have more than 2 characters, are you sure?")
        
        last_name = input ("Surname: ")
        if(len(last_name)<= 2):

            print("Customer's surname should have more than 2 characters, are you sure?")


        ppsn = input("PPSN: ")    
        if(len(ppsn)!=8):
            
            print("Customers PPSN number must consist of 8 characters, or press return to continue...")
       
      
        
        phone_number = input("Phone Number: ")
        email_address = input("Email Address: ")
        
        #account_type = input("Enter the account type: ")
        #opening_balance = input("Enter an amount: ")
        #overdraft = input("Overdraft facility:")


        new_customer = Customer(first_name,last_name, ppsn, phone_number, email_address)
        
        #new_customer = Account(account_type, opening_balance, overdraft)


        self._customers.append(new_customer)
        
        #self._accounts.append(new_customer)
    
   


    def account_deposit(self, account, amount):
        account.deposit(amount)
        print("Here is the new balance for this account: " + (str(account.balance)))
        
        

    def account_withdrawal(self, account, amount):
        account.withdrawal(amount)
        print("Here is the new balance for this account: " + (str(account.balance)))
        


    def find_account(self):
        account = None
        while(True):
            try:
                account_number = int(input("Enter account number: "))
                print("=========================================================================================")
                break
            except:
                print("Account number must be 8 digits. Please try again.")
                print("Return to exit...")
                input()
        
        account = self.get_account_number(account_number)

        return account
    

    def get_amount(self):
        while(True):
            try:
                amount = float(input("Enter amount: "))
                print("=========================================================================================")
                return amount
            except:
                print("Invalid amount entry.")
                self.clearscreen()
                self.show_user_menu()

    # get an account by account number 
    def get_account_number(self,search_acc_number): # TEST 
        
        for acc in self._accounts:
            if(search_acc_number == acc.account_number):
                return acc
        
        print("No Customer account found with that number")
        self.clearscreen()
        print(f"Invalid account number [{search_acc_number}]. Press return to try again.")
        input()
        return 
    
    def on_screen_help(self):
        
        print("\nWelcome to the help and assistance for ' ' Bank")
        print("------------------------------------------------")
        print(" If you cannot process a customer transaction please use one of the following options")
        print("\n1. Call our staff help-line on 01-089-2233")
        print("2. Email us your queries at bankmanagemen@info.ie")
        print("3. Text our instant message response agents at 083-890-2233")
        print("rerurn to continue...")
        input()


    
    
        

                

        
            

        
        

        


    
    