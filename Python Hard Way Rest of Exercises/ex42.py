## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##?
class Dog(Animal):

    def __init__(self, name):
        ##?
        self.name = name
class Cat(Animal):

    def __init__(self, name):
        ##?
        self.name = name
##?
class person(object):

    def __init__(self, name):
        ##?
        self.name = name
        ## person has-a pet of some kind
        self.pet = None

class Employee(person):
    def __init__(self, namr, salary):
        ##?? hmm what is this strange magic?
        super(Empolyee, self).__init__(name)
        ##??
        self.salary = salary

##??
class Fish(object):
    pass

##??
class Salamon(Fish):
    pass

##??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

##??
stan = Cat("Satan")

##??
mary = Person("Mary")

##??
Mary.pet = satan

##??
frank = Employee("Frank", 120000)

##??
frank.pet = rover

##??
flipper  = Fish()

##??
crouse = Salamon()

##??
harry = Halibut()
