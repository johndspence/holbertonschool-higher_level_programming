import json

json_data=open('./5-main.json').read()
data=json.loads(json_data)

print data
