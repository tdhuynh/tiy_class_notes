# functions take input as parameters, and give outputs as return values
def square(number): # inside the () is the method signature,
                    # parameter is in the method signature and also part of the function
                    # parameter is not to be confused with an argument
                    # 'number' is a parameter, while '94' (below) is an argument
    return_value = number ** 2
    print("WE GOT THE VALUE!")
    return return_value

print(square(94)) # 94 is an argument since it's concrete

def add(left, right): #left and right are parameters
    return left + right

print(add(22, 1000000))
 
