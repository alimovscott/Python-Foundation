''' FUNCTIONS 
(1) DEFINE VS CALL
(2) Parametr vs argument
(3) Keyword & default arguments
(4) Scope

'''
print("==== DEFINE VS CALL ====")
# build function print() vs type()
# Function - reusable block of code 
# Instead of block {} in JAVA, Python uses indentation


#DEFINE
def greet(a):
    print(f"how do you do, {a} ")

    
def greeting(b):
    print("greeting is executed")
    return f"hi {b}"

#CALL
result1 = greet("SCOTT")
print("resul1:", result1)

result2 = greeting("JESUS NAVAS")

print("result2:",result2)