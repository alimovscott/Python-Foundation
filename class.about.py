''' CLASS
 (1) What is class 
 (2) Ordinary vs static properties
 (3) special methods

'''

print("==== What is class  ====")
# class - blueprint for object creation! classlar object yasash uchun shablon
# structure > state => constructor => method 


class Person():
    # state 
    message = "static property"
    # constructer
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method 
    def introduce(self):
        print(f"Hi My name is {self.name}, my age is {self.age}")

    def say_age(self):
        print(f"Hi My age is {self.age}")

    @classmethod
    def explain(cls):
        print("Class: static method property excuted!")

    
person1 = Person("Scott", 26)
person2 = Person("Owen", 22)
person3 = Person("Jesus Navas", 28)

name = person1.name

print("person1.name:", person1.name)
    
# Ordinary method
person1.introduce()
person1.say_age()


# call Ordinary method
print("==== Ordinary vs static properties  ====")
new_message = Person.message
print(new_message)


Person.explain()



print("==== special/ magic methods  ====")
# Python most common special methods are below:
# __init__, __new__, __str__, _call__, __getitem__, __eq__, __len__ ...

class Car():
    #Constractor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)
    
    
    #State
    description = "This class makes cars"

    #Constractor
    def __init__(self, name, year):
        self.name = name
        self.year = year

    #Method
    def start_engine(self):
        print(f"the {self.name} started engine!")
    
    def stop_engine(self):
        print(f"the {self.name} stopped engine!")
    
    def __str__(self):
        return f" {self.name} was produced in {self.year} year "
    
    def __call__(self):
        print("Object called like a function")
        return True

    
car1 = Car("Genisis", 2025)
car1.start_engine()
car1.stop_engine()


print("----")
your_car = Car("Ferari", 2026)
print(your_car)

response = your_car()
print(response)