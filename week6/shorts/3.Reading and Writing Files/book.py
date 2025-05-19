def main():
    with open("alice.txt", "r") as f:
        # contents = f.read()
        contents = f.readlines()

    # print(contents[0])
    chapter1 = contents[52:272]
    print(chapter1[0])

    with open("chapter1.txt", "w") as f:
        #  f.write("Chapter I.")
         f.writelines(chapter1)

if __name__ == "__main__":
    main()
