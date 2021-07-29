import json
from json.encoder import JSONEncoder
from typing import Type

person = {"name": "Bhagya", "age": 19, "city": "Edmonton", "hasChildren": False, "title": ["Student", "Developer", "Athlete"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# with open("person.json", "r") as file:
#     person = json.loads(file)
# print(person)

# User class w/ name and age
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# created the user
user = User("Bhagya", 19)

def encode_user(o):
    # if an object is an instance of our class, if o is of class User
    if isinstance(o, User):
        return {'name': o.name, "age": o.age, o.__class__.__name__: True}
    else:
        return TypeError("Object of type User is not JSON serializable")


from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

# turned the user into json form w/ default being the function that is applied
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)