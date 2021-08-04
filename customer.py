class Customer:

    next_id = 0

    def __init__(self, first_name,last_name, ppsn, phone_number="", email_address=""):
        self._first_name = first_name
        self._last_name = last_name
        self._ppsn = ppsn
        self._phone_number = phone_number
        self._email_address = email_address
        self._id = Customer.next_id
        Customer.next_id = Customer.next_id + 1
    
    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if(len(first_name) <= 2):
            
            print("Customer's first name must have more than 2 characters")
        else:
            self._first_name = first_name

    
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    #getter setter for _ppsn
    @property
    def ppsn(self):
        return self._ppsn

    @ppsn.setter
    def ppsn(self, ppsn):
        self._ppsn = ppsn


    #getter setter for _id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number):
        self._phone_number = new_phone_number

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        self.email_address = email_address

    def __repr__(self):
        repr = f"{str(self.id).ljust(11)} {(self.first_name + ' ' + self.last_name).ljust(20)} "
        repr = repr + f"{self.ppsn.ljust(10)}"
        repr = repr + f" {self._phone_number.ljust(10)} {self.email_address.ljust(30)} "
        
        return repr