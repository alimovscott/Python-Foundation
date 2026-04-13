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



print("==== Ordinary vs static properties  ====")
new_message = Person.message
print(new_message)


Person.explain()

