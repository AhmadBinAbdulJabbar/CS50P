# print("Hello, World")

# input("What is your name? ")
# print("Hello, Ahmad")

# Ask User for name
# name  = input("What is your name? ")

# # Say hello to user
# print("Hello, ")
# print(name)

# Ask User for name
name  = input("What is your name? ")

# Say hello to user
print("Hello, " + name)
# used space after hello as only one argument is passed to print function concating the variable value
# and passing one argument like this (Hello, Ahmad) no extra space is add by the interpreter

# or we can use comma operator to pass multiple arguments to print function
print("Hello,", name)
# If multiple arguments are passed into print function space is added by the interpreter after hello,


# print function documentation
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# now we can do like this

# print("Hello, ", end="")
# print(name)

# or we can change the sep value as well from one space to anyother character
# print("Hello,", name, sep="???")

# end and sep are named parameters

# Escaping Characters
# print("Hello, "friend"") # error will occur you cannot use double quotes inside double quotes

print('Hello, "friend"') # you can use duoble quotes inside single quotes vice versa

print("Hello, \"friend\"")

# format string or f-string
print(f"Hello, {name}")

# string built-in methods

# userName = input("Enter Your name: ")


# strip remove whitespaces from the str both left and right
# userName = userName.strip()

# Capitalize users name
# userName = userName.capitalize()
# but it just captializes the first word first letter

# so we can use an other funciton that capitalizes the every word just like title of the book
# userName = userName.title()

# we can do all this in one line by using chaining
# userName = userName.strip().title()

# we can go one step furhter as well like this
# userName = input("Enter Your Name: ").strip().title()

# first, last = userName.split(" ")

# print("Your name is:", userName)

# print(f"Your first name is: {first}")

# you can enter the interactive mode just by typing python in the terminal

# create a function to say hello

# def hello(to="World"):
#     print("Hello, ", to)

# hello()
# myName = input("What is your name? ")
# hello(myName)

def main():
    name = input("What is your name? ")
    hello(name)

def hello(to="World"):
    print("Hello, ", to)

main()
