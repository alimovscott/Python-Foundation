print("=== Iterable objects & RANGE ===")
# Iterable objects > string dict tuple list range map filter



range_obj = range(3)



text = "SCOTT"
for letter in text:
    print(f"the letter: {letter}")


for ele in range_obj:
    print(f"the ele {ele}")
print(range_obj)

print("=== DICTONARY ===")

# DICTONARY === JSON OBJECT
person = {"name":"SCOTT", "age":26,"single":True}
person_obj = dict(name = "SCOTT", age = 26, single = True)

# METHODS: get()
print(f"person => {person}")
print(f"person_obj => {person_obj}")

name = person_obj["name"]
Ismaried = person_obj.get("single")
hobby = person_obj.get("hobby")

print(f"hobby {hobby}")
print(f"iSmaried=> {Ismaried}")
print(f"name:{name}")

del person_obj["age"]
for key in person_obj:
    print(f"the keys {key}")