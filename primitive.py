print("=========")
# in JAVA, variable name of storege location
# in Python, variables is named reference!

count = 100
count_type = type(count)
print("count:", count)
print(count_type)

print(f"i am {count} years old")

result1 = count.bit_count()
result2 = count.numerator

print(result1, result2)

course = "AI python fullstack"
result3 = type(course)

print(f"type of {result3}")

result = course.title()

print(f"the result {result}")

result = course.upper()

print(f"asd{result}")
result = course.replace("AI python fullstack", "Scott")

print(result)


print("====boolean====")
# functions > type() input() bool() int() str()

y = input("give your value for y ")
print(y)

result = y.isnumeric()
print(result)


# TRUTHY vs FALSY value
# TRUTH > true 100 , -100, "SCOTT"
# FALSY > false 0, "" , nan

test_falsy = "" 
print("THE Falsy", bool(test_falsy))