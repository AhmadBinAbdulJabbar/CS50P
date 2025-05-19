# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# if we are using a variable just to print the result it is good we don't do that

# print(z)

# x = int(input("What's x? "))
# y = int(input("What's y? "))

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)
# z = round(x + y, 2) # rounding till 2 decimal places

# print(x + y)
# print(z)

# print(f"{z:,}")

# division operator
z = x / y
print(z)
print(round(z, 3))
print(f"{z:.3f}")


def main():
    x = int(input("What's x?"))
    print(f"{x} square is {square(x)}")

def square(n):
    # return n*n
    # return n ** 2
    return pow(n,2)

main()
