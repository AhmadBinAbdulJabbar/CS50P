def main():
    n = int(input("What's n? "))
    # for i in range(n):
    #     print(sheep(i))
    for s in sheep(n):
        print(s)


# def sheep(n):
#     # return "🐑" * n
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock

def sheep(n):
    for i in range(n):
        yield "🐑" * n


if __name__ == "__main__":
    main()


