import json

#example json
x = {"name":"Julian","age":"25", "city":"QC"}

#parse json

y = json.loads(x)
print("The output of the json file is", y)
print("Name",y["name"])