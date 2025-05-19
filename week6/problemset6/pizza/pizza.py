from tabulate import tabulate
import csv
import sys


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not(sys.argv[1].endswith(".csv")):
        print("Not a CSV file")
        sys.exit(1)


    file_name = sys.argv[1]
    table = []

    # 1st approach using reader
    # try:
    #     with open(file_name, "r") as file:
    #         reader = csv.reader(file)
    #         for row in reader:
    #             print(row)
    #             table.append(row)
    # except FileNotFoundError:
    #     print("File does not exist")
    #     sys.exit(1)

    # print(tabulate(table, headers="firstrow", tablefmt="grid"))

    # 2nd approach using DictReader
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # print(row)
                table.append(row)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
