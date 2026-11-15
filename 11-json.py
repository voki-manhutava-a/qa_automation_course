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
# converted is a string, so converted['key2'] would raise
# TypeError: string indices must be integers
# json.loads parses the string back into a dictionary
py_data = json.loads(converted)
print('The value of key2:', (py_data['key2']))

print('\nExercise 2: Sort JSON keys in and write them into a file. Sort following JSON data alphabetical order of keys') 
sample_json = {"id" : 1, "name" : "value2", "age" : 29}
# dump() writes to a file, dumps() returns a string (s = string); the same for load() and loads()
with open("sampleJson.json", "w") as write_file:
    json.dump(sample_json, write_file, indent=4, sort_keys=True)

print(json.dumps(sample_json, indent=4, sort_keys=True))

print('\nExercise 3: Access the nested key `salary` from the following JSON')

sample_json_2 = """{ 
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

parsed_json = json.loads(sample_json_2)
print("Employee's salary:", parsed_json['company']['employee']['payble']['salary'])

print('\nAccessing a list inside JSON')
projects_json = '{"projects": [{"name": "Alpha"}, {"name": "Beta"}]}'
projects_data = json.loads(projects_json)
print("Project name:", projects_data["projects"][0]["name"])

print('\nHandling invalid JSON')
try:
    json.loads('{"key1": "value1"')
except json.JSONDecodeError:
    print('Invalid JSON')

print('\nPython types in JSON')
types_example = {"none": None, "flag": True, "tuple": (1, 2), 1: "number key"}
print(json.dumps(types_example))