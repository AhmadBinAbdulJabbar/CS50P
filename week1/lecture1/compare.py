# x = int(input("What's x? "))
# y = int(input("What's y? "))


# 1st way is by just using if statement (all the conditions will be check every time)
# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")


# 2nd way is to use if elif (check conditions until found true so not all conditions a check)
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")

# 3rd way use else for the last case no need to use elif and check condition
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")


# or

# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")



# if x == y:
#     print("x is equal to y")
# else:
#     print("x is not equal to y")


# score = int(input("Score: "))

# using and operator

# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# if score >= 90:
#     print("Grade: A")
# elif score >= 80 :
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# simple way
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# python way / Pythonic
# def is_even(n):
#     return True if n % 2 == 0 else False

# def is_even(n):
#     return n % 2 == 0


# main()

# match
name = input("What's your name? ")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else: print("Who?")

# using match statement
# match name:
#     case "Harry":
#         print("Griffindor")
#     case "Hermione":
#         print("Griffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")


# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Griffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

