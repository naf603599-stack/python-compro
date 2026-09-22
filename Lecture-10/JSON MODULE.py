import json

data = {"name": "Alice","age":25}
json_str=json.dumps(data)
print(json_str) #output: JSON string

parsed_data = json.loads(json_str)
print(parsed_data) #output:Python directory
print(parsed_data["name"]) #output: Alice
print(parsed_data["age"]) #output: 25
