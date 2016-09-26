import csv

# this is a context manager (with open()....)
with open('data.csv') as open_file:
    contents = open_file.readlines() # read() is good for a large body of text like a book
                                    # readlines() will give each line in that body of text
# print(contents[2].split(',')[2]) # this method is good for calling on a single part of a single line

# we need to parse this csv with python code since it will print out as a long string.

# clean_data = []    # 10 - 18 is scalable/appliable to all data sets, but it's not the best since we have to maintain it
#
# # for row in contents:
# #     row = row.replace("\n", "")
# #     clean_data.append(row.split(','))
#
clean_data = [row.replace('\n', "").split(',') for row in contents]

# print(clean_data)
# print(clean_data[11][4])

#################################################
# another method to open and parse data file. remember to import csv as on line 1

with open("data.csv") as open_file:
#    contents = csv.reader(open_file) #if the separator is not a comma then use (open_file, delimiter = "|")
                                      # the item in the " " should be the separator character
    contents = csv.DictReader(open_file) # DictReader will give a table in the form of a dict
    print(list(contents)[1]["Water Temp"])

#################################################

# ( :) for joel) way 1 to import modules -- for just importing one random function (e.g. randint)
from random import randint as tommy_random
x = randint(1, 20)

# ( :/ for joel)  way 2 -- this method is handy for importing many random functions (e.g. randint, randrange, etc...)
import random
x = random.randint(1, 20)

# ( :( for joel) way 3 -- this will import all the variables --- AVOID THIS ONE IF POSSIBLE
from random import *
x = randint(1, 20)

#################################################

# SERIALIZE converts a simple type to a complex type
