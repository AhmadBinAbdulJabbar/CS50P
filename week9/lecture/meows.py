# MEOWS = 3

# MEOWS = 4
# for _ in range(MEOWS):
#     print("meow")


# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()



def meow(n: int) -> str:
    """Meow n times."""
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    # for _ in range(n):
    #     print("meow")
    return "meow\n" * n

number: int = int(input("Number: "))
# meow(number)

meows: str = meow(number)
print(meows, end="")

