import json
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)
# y = json.loads(x)

# # the result is a JSON string:
# print(y)

print('JSON\nExercise 1: Convert the following dictionary into JSON format then access the value of key2 from the following JSON')

data = {"key1" : "value1", "key2" : "value2"}
converted = json.dumps(data)
print(converted)
py_data = json.loads(converted)
print('The value of key2:', (py_data['key2']))

print('\nExercise 2: Sort JSON keys in and write them into a file. Sort following JSON data alphabetical order of keys') 
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)

print(sampleJson)

print('\nExercise 3: Access the nested key `salary` from the following JSON')

sampleJson2 = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

employee = json.loads(sampleJson2)
print('Employe`s salary:', employee['company']['employee']['payble']['salary'])

# print("Project name: ", developerDict["projectinfo"][0]["name"])

