# print("#")
# print("#")
# print("#")


# for _ in range(3):
#     print("#")

def main():
    # print_column(5)
    # print_row(4)
    print_square(3)



def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end = "")


# def print_row(width):
#     print("?" * width)

def print_row(width):
    print("#" * width)



# def print_square(size):
#     for i in range(size):
#         for j in range(size):
#             print("#", end="")
#         print()

def print_square(size):
    for i in range(size):
        print_row(size)

main()
