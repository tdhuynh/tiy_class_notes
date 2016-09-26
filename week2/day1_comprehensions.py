#
# # method 1 -- one way to do a for loop
# mylist = [4, 1, 11, 13]
# ages = []
# for person in mylist:
#     petyears = person * 7
#     ages.append(petyears)
# print(ages)
#
# # method 2 -- list comprehension method to condense all the above code into one line
# mylist2 = [4, 1, 11, 13]
# ages = [person * 7 for person in mylist2] # read "for person in mylist2" first, then "person * 7"
# # this would give ages = [28, 7, 77, 91]
#
# # method 3 -- giving another condition
# ages = [person * 7 for person in mylist2 if person < 10]
# # this would give ages = [28, 7] since 11 and 13 are larger than 10

list_of_numbers = [9, 10, 5, 100, 23, 2]
half_values = []
for x in list_of_numbers:
    half_of_x = x / 2
    half_values.append(half_of_x)
print(half_values)

##########################################################################

list_of_numbers = [9, 342, 234, 34, 66, 90]
half_values = [x / 2 for x in list_of_numbers]
# outside brackets matter [] gives a list, tuple() gives a tuple, {} gives a set
print(half_values)

##########################################################################
# bloated way of adding squares to a dict
list_of_numbers = [100, 67, 23, 45, 11]
square_num = {}

for num in list_of_numbers:
    square_num[num] = num ** 2
print(square_num)

##########################################################################
# dict comprehension way of doing above

list_of_numbers = [100, 67, 23, 45, 11]
square_num = {num: num ** 2
              for num in list_of_numbers}
print(square_num)

##########################################################################

matrix = [["_", "X", "_"],
          ["O", "X", "O"],
          ["O", "X", "O"]]

target_column = []

for row in matrix:
    target_column.append(row[1])
print(target_column)

##########################################################################

matrix = [["_", "X", "_"],
          ["O", "X", "O"],
          ["O", "X", "O"]]

target_column = [row[1] for row in matrix]
print(target_column)
