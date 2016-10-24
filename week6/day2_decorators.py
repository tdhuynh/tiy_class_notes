
def func_caller(func):
    print('lol')
    return "haha"


@func_caller
def remote_control():
    print("I love lamp")
    return 0

remote_control()
# so when remote_control is called, @func_caller will run first since it is a decorator,
    # then it will run remote_control()

# func_caller(remote_control)
