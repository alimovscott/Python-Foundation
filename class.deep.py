''' CLASS deep diving 
    (1) ENCAPSULATION
    (2) INHERITENCE
    (3) POLIMORFISM

'''

print("==== ENCAPSUlATION ====")

'''
c++ java php tpyscript => public private protected
python => name __name _name 
python public __private _protected
'''

class Account():
    # state 
    descrption = "The class makes bank accounts"
    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amout = amount
    

    #method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amout} usd")

    
    def deposit(self, amount):
        print("~~~ Deposit executed!!!=>", amount)
        self.__amout += amount

    def withdrow(self, amount):
        print("~~~ withdrow executed!!!=>", amount)
        self.__amout -= amount

    @property # getter
    def holder(self):
        return self.__owner
    

    @holder.setter
    def holder(self, new_owner):
        print("change_ownership=>", new_owner)
        self.__owner = new_owner


    
    def change_ownership(self, new_owner):
        print("change_ownership=>", new_owner)
        self.__owner = new_owner

my_acoount = Account("SCOTT", 1000)
my_acoount.get_balance()

my_acoount.deposit(3500)
my_acoount.withdrow(400)
my_acoount.get_balance()

print("-----")
try:
    result = my_acoount.__amout
    print("result=> ", result)
except Exception as err:
    print("no amount state found", err)


account_owner = my_acoount.holder

print("account_owner before =>", my_acoount.holder)

my_acoount.change_ownership("JESUS NAVAS")

print("account_owner before =>", my_acoount.holder)

my_acoount.holder = "SCOTT"

print(my_acoount.holder)

    