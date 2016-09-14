
my_list = ["tommy", 23, ["spiders", "the unknown"]]

print(my_list)
my_list.pop()
my_list.append("fred")
print(my_list)
print(my_list[1]) # will print the item at index 1 in the list
print(my_list[2])
print(my_list[2][0]) # since item at index 2 is a list,
                            # you can print an item from that list with a new set of []
my_dictionary = {
    "name": "Tommy",
    "age": 23,
    "fears": ["spiders", "the unknown"]
}

print(my_dictionary)
print(my_dictionary['name'])
print(my_dictionary['age'])
print(my_dictionary['fears'])

print(my_dictionary.keys())
