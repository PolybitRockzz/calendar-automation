import json

with open('data.json', 'r') as f:
    data = json.load(f)
    data = json.dumps(data)

print("Loading JSON Data... Done")

import openapi
print("Sending Request...")
res = openapi.get_from_openai(data, "Friday, March 24th, 2023")
print("\n\n\n" + res)