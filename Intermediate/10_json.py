import json

person = {"name": "Bhagya", "age": 19, "city": "Edmonton", "hasChildren": False, "title": ["Student", "Developer", "Athlete"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open("person.json", "r") as file:
    person = json.loads(file)
print(person)