class MyOwn:
    def __init__(my, name, age):
        my.name = name
        my.age = age

    def say_hello(my):
        print(f'Hello, my name is {my.name} and I am {my.age} years old.')
    
    def __str__(my):
        return f'MyOwn({my.name}, {my.age})'
    
x = MyOwn('Alice', 30)
x.say_hello()
print(x.__str__())