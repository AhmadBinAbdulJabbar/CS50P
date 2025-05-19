def main():
    # yell("This is CS50")
    # yell(["This", "is", "CS50"])
    yell("This", "is", "CS50", "by", "harvard")

# def yell(phrase):
#     print(phrase.upper())

# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)


# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)


def yell(*words):
    # uppercased = map(str.upper, words)
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()
