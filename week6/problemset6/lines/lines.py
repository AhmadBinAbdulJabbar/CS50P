import sys

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not(sys.argv[1].endswith(".py")):
        print("Not a Python file")
        sys.exit(1)

    file_name = sys.argv[1]
    count = 0
    try:
        with open(file_name, "r") as file:
            reader = file.readlines()
            for line in reader:
                if line.strip() != "" and not line.strip().startswith("#"):
                    count += 1
            print(count)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()
