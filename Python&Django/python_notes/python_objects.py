
# This creates a class of new object, that can be instanced
class Sample():
    pass

x = Sample()

print(type(x))


# Class Attributes
class Dog():
    # Methods are functions inside a class
    # initial method
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def who_am_i(self):
        print(self.name)

    # Attributes are variables inside a class
    # Attributes are always the same regardless of instance, and do not need to be specified on instance creation
    species = 'canidae'

# Instance of the class assigned to a variable
mydog = Dog(breed='Lab', name='jeff')
# print(mydog.breed)


class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return (self.radius * self.radius) * Circle.pi
    
    def set_radius(self,new_radius):
        self.radius = new_radius

    
mycircle = Circle(30)
# print(mycircle.radius)


# Inheritence
class Animal():

    def __init__(self, name):
        self.name = name
        print("animal created")

    def who_am_I(self):
        print("animal")

    def eat(self):
        print("MONCH")


# when creating a new class, you can inherit the attributes of an existing class as below
class Cat(Animal):

# Special methods
    # init specifies starting basic info of the object
    def __init__(self):
        Animal.__init__(self)
        print("CAT CREATED")
    # str references what will be returned when calling the object itself (not a method of the class)
    def __str__(self):
        print(f"")
    # Returns whatever when calling instance with len()
    def __len__(self):
        return self.length


    # You can also make new methods that do not reflect in the original class
    def meow(self):
        print("MEOW")
    
    # You can overwrite methods
    def eat(self):
        print("nomnomnom")


mycat = Cat()
mycat.who_am_I()
mycat.eat()
mycat.meow()



# SPECIAL METHODS
