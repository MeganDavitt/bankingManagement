from bank import Bank
from datastore import Datastore


datastore = Datastore()
datastore.create_accounts_and_customers()



my_bank = Bank(datastore)
my_bank.do_user_menu()




