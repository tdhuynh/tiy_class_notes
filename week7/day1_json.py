l = ['5', 'tommy', None, 4]
string_list = str(l)
print(string_list)

import json

# json.dumps will convert any possible arguments from python to json
json_list = json.dumps(l)
print(json_list)

print(json.dumps({"tommy": 'codes'}))
