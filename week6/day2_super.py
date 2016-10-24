
class A:
    def __init__(self):
        self.ready = True

Class B(A):
    def  __init__(self, favorite):
        super().__init__()
        self.favorite = favorite

x = A()
print(x.ready)
# >>> True

y = B('jelly beans')
print(y.favorite)
print(y.ready)
# this would not print "True" because __init__ in class A was overwritten by class B __init__
# we use the super() class to refer back to the parent class's __init__()
# see it as taking everything important in the __init__() of the parent class,
    # and wedging it into class B.
# now print(y.ready) will give you "True"
