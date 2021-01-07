import json

json_open = open('qitta_json.json', 'r')
json_load = json.load(json_open)

print(json_load)
print(json_load['section1']['key'])