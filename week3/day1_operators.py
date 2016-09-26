# magic methods are strictly used for oop NOT functions
print("tommy" + " programs")
# print("Tommy" + 1) ERROR


class SuperNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return SuperNumber(str(self.value) + str(other.value))

    def __str__(self):
        return "DEBUG: Value is " + str(self.value) # __str__ can only return a string of your instance

s_number_1 = SuperNumber(1)
s_number_2 = SuperNumber("tommy")


print(s_number_1)

x = s_number_1 + s_number_2 + s_number_2

print(x)

#focus on storing conversion rates
#when doing conversion, symbol of money on left is retained
    # if $ + jpy, answer is in $
