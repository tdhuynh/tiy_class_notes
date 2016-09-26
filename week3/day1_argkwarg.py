def adder(num1, num2, message="No Message Passed", happy = True): # positional argument are required, and ORDER IS VERY IMPORTANT
    print(message)
    print(happy)
    return num1 + num2

# kwargs -- optional named parameters

print(adder(987654321, 123456789, happy=False, message="DO MATH SON!"))
print(adder("Tommy", " likes programming"))

def add(*args):
    return sum(args)

print(add(1, 5932, 37489274, 87893749812949012))

print(adder(*[9, 4]))

def beginners_luck(name, account_number, *args, **kwargs): # kwargs ALWAYS go right to positional args
    print(name, "NAME")
    print(account_number, "ACCOUNT NUMBER")
    print(args) # args will be assigned everything not assigned a specified posit arg
    print(kwargs)
    return 1

print(beginners_luck("tommy", 24917284, [1, 2, 3], 99, birthday="Today", lol="Tommy"))
