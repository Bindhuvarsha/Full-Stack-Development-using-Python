# import json
# student={
#     "name":"varsha",
#     "age":18,
# }
# data=json.dumps(student) #converts python object into json object
# print(data)

import json
data='{"name":"varsha","age":18}'
result=json.loads(data) #converts json object into python object
print(result["name"])