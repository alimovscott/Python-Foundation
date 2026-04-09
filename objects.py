'''
Docstring for objects
(1) What is object
(2) Iterable objects & RANGE
(3) DICTONARY
(4) Error handling
'''

import array # package/module
import math # package/module
from math import ceil


print("==== What is object ====")

#An object has state and method properties
#Everything is object in python

print(type("hello world"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))


#PARADIGMA > Functional Programming & OOP
# OOP 4 CONSEPTS > ABCTRACTION | ENCAPSuLATION | INHERTENCE | POLIFORMISM

result1 = ceil(97.6) #CALL
print(result1)

print("==== Error handling System ====")

car_dist = dict(name = "Tayota", year = "2025", electric = True )

try:
    print("passed here")
    result2 = car_dist["origin"]
except KeyError as err:
    print("No origin date", err)
else:
    print("Execetud successfully without errors")
finally:
    print("Final closing logic")


try:
    print("passed here2")
    result2 = car_dist["year"]
except KeyError as err:
    print("No origin date", err)
else:
    print("Execetud successfully without errors")
finally:
    print("Final closing logic")






