# 4.13.3: Greetings
# Korbin Griffin
# 2.5.19

name = input ("What is your name: ")

def greeting():
    print ("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


# 4.13.4: Functions and Variables
# Korbin Griffin
# 2.11.19

x =  10

def print_something():
    x = 3
    print('\r\n', x)

print('\r\n', x)
print_something()


# 4.13.6: Functions and Variables, Part 3
# Korbin Griffin
# 2.18.19


def print_number(x):
    print('\n' + x)

print_number(13)
print_number(23)


# 4.14.4: Name and Age
# Korbin Griffin
# 2.18.19

def name_and_age(name, age):
    print('Hi, my name is', name, 'and I am', str(age), 'years old')

name_and_age('Mike',33)
name_and_age('Zane',18)