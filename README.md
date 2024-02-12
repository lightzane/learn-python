# Working with JSON Data

https://www.youtube.com/watch?v=9N6a-VLBa2I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

---

# JSON to Python

| **JSON**      | **Python** |
| ------------- | ---------- |
| object        | dict       |
| array         | list       |
| string        | str        |
| number (int)  | int        |
| number (real) | float      |
| true          | True       |
| false         | False      |
| null          | None       |

Reference: https://docs.python.org/3/library/json.html#encoders-and-decoders

## Parse JSON to Python

- [Using `json.loads`](#using-jsonloads) - load **string**
- [Using `json.load`](#using-jsonload) - load **file**

## Parse Python to JSON

- [Using `json.dumps`](#using-jsondumps) - dump to JSON **string**
- [Using `json.dump`](#using-jsondump) - dump to JSON **file**

## REST to Python to JSON

[See here](#rest-to-json-file)

## Using `json.loads`

Parsing JSON data from a **STRING**

```py
import json

people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}
'''

data = json.loads(people_string)

print(type(data)) # => <class 'dict'>
print(type(data['people'])) # => <class 'list'>
print(data) # => {'people': [{'name': 'John Smith', 'phone': '615-555-7164', 'emails': ['johnsmith@bogusemail.com', 'john.smith@work-place.com'], 'has_license': False}, {'name': 'Jane Doe', 'phone': '560-555-5153', 'emails': None, 'has_license': True}]}

for people in data['people']:
    print(people)
```

## Using `json.load`

Parsing data from a **FILE**

`data.json`

```json
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}
```

```py
import json

# with open('data.json', 'r') as rf:
with open('data.json') as f: # Read-only by default, so 'r' is not required
    data = json.load(f)

print(type(data)) # => <class 'dict'>
print(type(data['people'])) # => <class 'list'>
print(data) # => {'people': [{'name': 'John Smith', 'phone': '615-555-7164', 'emails': ['johnsmith@bogusemail.com', 'john.smith@work-place.com'], 'has_license': False}, {'name': 'Jane Doe', 'phone': '560-555-5153', 'emails': None, 'has_license': True}]}

for people in data['people']:
    print(people)
```

## Using `json.dumps`

```py
import json

...

for people in data['people']:
    print(people)
    del people['phone']

new_string = json.dumps(data)

print(new_string) # => {"people": [{"name": "John Smith", "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"], "has_license": false}, {"name": "Jane Doe", "emails": null, "has_license": true}]}
```

### Make it more readable

```py
indented_string = json.dumps(data, indent=2)
print(indented_string) # =>
# {
#   "people": [
#     {
#       "name": "John Smith",
#       "emails": [
#         "johnsmith@bogusemail.com",
#         "john.smith@work-place.com"
#       ],
#       "has_license": false
#     },
#     {
#       "name": "Jane Doe",
#       "emails": null,
#       "has_license": true
#     }
#   ]
# }
```

## Using `json.dump`

```py
import json
...
indented_string = json.dumps(data, indent=2)
print(indented_string)

# Creates a new JSON file
with open('data-copy.json', 'w') as f:
    json.dump(data, f, indent=2)
```

## REST to JSON file

Using the Python built-in HTTP request

```py
from urllib.request import urlopen

rest_api = 'https://jsonplaceholder.typicode.com/users'

try:
    with urlopen(rest_api) as response:
        source = response.read()
        source_json = json.loads(source)

    with open('rest-copy.json', 'w') as f:
        json.dump(source_json, f, indent=2)
except:
    print('Unable to fetch rest_api')
```

# References

- https://docs.python.org/3/library/json.html#encoders-and-decoders

| **JSON**      | **Python** |
| ------------- | ---------- |
| object        | dict       |
| array         | list       |
| string        | str        |
| number (int)  | int        |
| number (real) | float      |
| true          | True       |
| false         | False      |
| null          | None       |
