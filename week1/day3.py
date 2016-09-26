
for _ in range(5):
    print("i am looping")

turns = 0
while turns < 5:
    print("WHILE LOOPING")
    turns += 1

choice = ""
while choice != 'n': # this is to run through a loop infinitely
    print(choice)
    choice = input("Do you want to loop again? [Y/n] ")
# list is an item storage
    #list = ['tommy', 23, [1, 2, 3]]
    #list[1] will give back 23
# dictionary is a key:value storage
    #d={"name":"tommy", "age":23, "fears":[]}
    #d['age'] will give 23
