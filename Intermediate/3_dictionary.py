# dictionary: key-value pairs, unordered, mutable

mydict = {"name": "bhagya", "age": 19, "city": "edmonton"}
print(mydict) # 'name': 'bhagya', 'age': 19, 'city': 'edmonton'

mydict2 = dict(name="bhagya", age=19, city="edmonton")
print(mydict2) # 'name': 'bhagya', 'age': 19, 'city': 'edmonton'

mydict["email"] = "bhagya_test@yahoo.com" # new key
print(mydict) # 'name': 'bhagya', 'age': 19, 'city': 'edmonton', 'email': 'bhagya_2002@yahoo.com'

mydict["email"] = "test@yahoo.com" # overwrite
print(mydict) # 'name': 'bhagya', 'age': 19, 'city': 'edmonton', 'email': 'look_its_bhagya@yahoo.com'

del mydict["email"] # delete email key
print(mydict) # 'name': 'bhagya', 'age': 19, 'city': 'edmonton'

mydict.pop("city") # delete city key
print(mydict) # 'name': 'bhagya', 'age': 19

mydict.popitem() # pop last key-value pair
print(mydict) # 'name': 'bhagya'

mydict3 = {"name": "bhagya", "age": 19, "city": "edmonton"}
print(mydict) # 'name': 'bhagya', 'age': 19, 'city': 'edmonton'

if "age" in mydict3:
    print("age is in mydict")

try:
    print(mydict3["name"])
except:
    print("name is not in mydict")
          
for key in mydict3.keys():
    print(key)

for value in mydict3.values():
    print(value)

for key, value in mydict3.items():
    print(key, value)
    
# to copy use .copy()
mydict_copy = mydict3.copy()

p1 = {"name": "bhagya", "age": 19, "email": "bhagya_test@yahoo.com"}
p2 = {"name": "aarush", "age": 12, "city": "edmonton"}

p1.update(p2) # update p1 with p2 (p1 is overridden w/ excess keys)