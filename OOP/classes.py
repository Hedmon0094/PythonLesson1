class Person:
    def __init__(self, name, age ):
        self.name = name
        self.age = age
        
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old"
        

person = Person("John", 23)
print(person.greet())



# def myName(name1, name2):
#     print()
    
# myName("Evans", "Mutuku")