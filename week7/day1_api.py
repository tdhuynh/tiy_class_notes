import requests


# result = requests.get("http://swapi.co/api/people/")
# # print(result.text)
# json_result = result.json()
# # print(json_result)
# # print(json_result["name"])

# for person in json_result["results"]:
#     print(person["name"])



# result = requests.get(json_result["next"])
# json_result = result.json()
#
# for person in json_result["results"]:
#     print(person["name"])


###################


def get_data(endpoint, lookup="name"):
    url = "http://swapi.co/api/{}/".format(endpoint)
    while url:
        result = requests.get(url)
        json_result = result.json()

        for person in json_result["results"]:
            print(person[lookup])
        if input("Press Enter to keep going, type 'n' to keep going " ):
            break
        url = json_result["next"]


while True:
    value = input("What do you want to search for? (films) or (people)? ")
    if value == "films":
        get_data(value, lookup="title")
    get_data(value)
