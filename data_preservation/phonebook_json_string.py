import json

with open("data_preservation/data.txt", "r") as file:
    content = file.read()
    jscontent = json.loads(content)

print(jscontent)

jscontent["age"] = 35

with open("data_preservation/data.txt", "w") as file:
    content = json.dumps(jscontent, indent=2)
    file.write(content)
    

print(jscontent)