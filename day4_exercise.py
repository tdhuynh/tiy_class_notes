# input 1 = 'programming is fun'
# input 2 = 'm'
# output = [6, 7]

sentence = 'i decided to learn how to program and it was a good decision'
letter = ' '
output = []

#first way to locate letter

# current_location = 0
# for current_letter in sentence:
#     if current_letter == letter:
#         output.append(current_location)
#     current_location += 1
#
# print(output)

# enumerate will provide a location of where a letter currently is
# this will cut down a large amount of code that you don't need to write

for current_location, current_letter in enumerate(sentence):
    if current_letter == letter:
        output.append(current_location)

print(output)
