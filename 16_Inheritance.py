class Parent:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age

class Child(Parent):
    def __init__(self, name, lname, age, school):
        super().__init__(name, lnamge, age)
        self.school = school

mylist = ["one", "two", "three"]

myiter = iter(mylist)
# print(dir(myiter))
print(next(myiter))

print(dir(mylist))