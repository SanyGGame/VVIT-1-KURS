#1
def greet(name):
    print(f'Привет, {name}!')

name = 'Артём'
greet(name)

#2
def square(number):
    return number**2
number = 5
print(square(number))

#3
def max_of_two(x,y):
    if x > y:
        return x
    else:
        return y
x = 99
y = 76
print(max_of_two(x,y))
