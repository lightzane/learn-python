import json
from urllib.request import urlopen

data = None

# with open('data.json', 'r') as rf:
with open('data.json') as f: # Read-only by default, so 'r' is not required
    data = json.load(f)

print(type(data)) # => <class 'dict'>
print(data) # => {'people': [{'name': 'John Smith', 'phone': '615-555-7164', 'emails': ['johnsmith@bogusemail.com', 'john.smith@work-place.com'], 'has_license': False}, {'name': 'Jane Doe', 'phone': '560-555-5153', 'emails': None, 'has_license': True}]}

print(type(data['people'])) # => <class 'list'>

for people in data['people']:
    print(people)
    del people['phone']

new_string = json.dumps(data)
print(new_string) # => {"people": [{"name": "John Smith", "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"], "has_license": false}, {"name": "Jane Doe", "emails": null, "has_license": true}]}

indented_string = json.dumps(data, indent=2)
print(indented_string)

with open('data-copy.json', 'w') as f:
    json.dump(data, f, indent=2)

rest_api = 'https://jsonplaceholder.typicode.com/users'

try:
    with urlopen(rest_api) as response:
        source = response.read()
        source_json = json.loads(source)
        
    print(json.dumps(source_json, indent=2))

    with open('rest-copy.json', 'w') as f:
        json.dump(source_json, f, indent=2)
except:
    print('Unable to fetch rest_api')