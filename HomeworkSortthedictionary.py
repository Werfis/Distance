import json
sampleJson = {"id": 1, "name": "value2", "age": 29}
# Sort the dictionary
sorted_dict = dict(sorted(sampleJson.items()))
# Write to file
with open('output.json', 'w') as f:
    json.dump(sorted_dict, f, ensure_ascii=False, indent=4)