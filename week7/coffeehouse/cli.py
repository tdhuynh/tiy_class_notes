import requests

json_result = requests.get("http://locathost:8000/specials/").json()

for special in json_result:
    print(special['name'])
    print(special['price'])
    print(special['description'])
    print('*'*80)
