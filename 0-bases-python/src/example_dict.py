from datetime import datetime

my_dictionary = {
    "first_name": "Alvaro",
    "last_name": "Garzon",
    "age": "unknown",
    "profession": "software engineering",
    "is_active": True,
    "is_not_creating_courses": False,
    "birthdate": datetime.now(),
}

for key in my_dictionary.keys():
    print("Key: ", key)

for value in my_dictionary.values():
    print("Value: ", value)

for key, value in my_dictionary.items():
    print(f"Key: {key} - value: {value}")
