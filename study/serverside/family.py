import json
import requests
json_open = open('qitta_json.json', 'r')
data = json.loads("family.json")
print(data["children"]["grandchild"]["age"])