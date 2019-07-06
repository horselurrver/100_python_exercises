"""
Define a class, which have a class parameter and have a same instance parameter.
"""
class Person:
    def __init__(self, name = None):
        self.name = name

person1 = Person()
print(person1.name)

person2 = Person('Bob')
print(person2.name)
