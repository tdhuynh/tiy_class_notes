 # tuples are lists that CANNOT be changed
 # to make a tuple with ONE item, put a comma after the item in the tuple
 # tuples are best when you don't want to add or remove anything from the list -- read only data
 # immutable - not able to change/edit after creating

my_tuple = ("tommy", "michael")
print(my_tuple)
# my_tuple.append("fred")
# print(my_tuple)

my_string = 'cellular phone'
print(my_string + 's')
# my_string += 's'
# my_string[2] = 'j' # will not work

# sets can be changed after creation
# sets CANNOT have duplicate items*********
# you can subtract from sets, unlike lists where you cannot subtract a list from a list

my_set = {2, 7, 9, 'tommy'}
my_people_set = {'tommy', 'michael', 'fred', 'moo'}
print(my_set.intersection(my_people_set))
print(help(my_set))
