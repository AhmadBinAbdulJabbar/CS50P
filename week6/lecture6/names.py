# name = input("What's your name? ")
# print(f"hello, {name}")


# names = []

# for _ in range(3):
#     name = input("What's your name? ").strip()
#     names.append(name)

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What's your name? ").strip()

# writing on to a file
# file = open("names.txt", "w")
# file = open("names.txt", "a")
# # file.write(name)
# file.write(f"{name}\n")
# file.close()


# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     # print("hello,", line, end="")
#     print("hello,", line.rstrip())

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip().lower())

# for name in sorted(names):
#     print("hello,", name)

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip().lower())

for name in sorted(names, reserse=True):
    print("hello,", name)

