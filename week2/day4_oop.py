
class Person:
    def __init__(self, name):
        self.name = name


class Bike:
    # a function inside a class is called a method
    # a method under class should ALWAYS accept ONE OR MORE parameter
    # DRY - DON'T REPEAT YOURSELF
    def __init__(self, speeds, owner): # __init__ is where you put code that is called ONCE
        self.speed = speeds
        self.color = "grey"
        self._layers = 1
        self.owner = owner

    def set_color(self, new_color):
        self.color = new_color
        self._layers += 1

    def get_layers(self):
        return self._layers

fred = Person("fred")
tommy = Person("tommy")
bike = Bike(100, fred)
tommys_bike = Bike(18, tommy)

print("OWNERS===========")
print(bike.owner.name)
print(tommys_bike.owner.name)

print(bike)
print("color before we change it")
print(bike.color)
print(bike.get_layers())

print("color after we change it")
bike.set_color("red")
print(bike.color)
print(bike.get_layers())

print("color of tommy's bike")
tommys_bike.set_color("pink")
print(tommys_bike.color)

for x in range(100):
    bike.set_color("white")
print(bike.color)
print(bike.get_layers())

# class Cards:
# __init__(self):
    # for x in range(52):
        # 
