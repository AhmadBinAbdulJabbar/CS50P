# print("meow")
# print("meow")
# print("meow")

# i = 3
# while i != 0:
#     print("meow")
#     # i = i - 1
#     i -= 1

# i = 1
# while i <= 3:
#     print("meow")
#     i = i + 1

# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# for i in [0,1,2]:
#     print("meow")

# for i in range(3):
#     print("meow")

# for _ in range(3):
#     print("meow")

# print("meow" * 3)

# print("meow\n" * 3, end = "")

# while True:
#     n = int(input("what's n? "))
#     if n < 0:
#         continue
#     else:
#         break

# while True:
#     n = int(input("what's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            # return n
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

