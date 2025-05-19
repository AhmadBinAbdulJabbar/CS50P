import csv
import sys


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not(sys.argv[1].endswith(".csv")):
        print("Not a CSV file")
        sys.exit(1)


    read_file = sys.argv[1]
    write_file = sys.argv[2]

    # data = []
    # try:
    #     with open(read_file, "r") as file:
    #         reader = csv.DictReader(file)
    #         for row in reader:
    #             # first, last = row["name"].split(",")
    #             # first = first.strip()
    #             # last = last.strip()

    #             first, last = [part.strip() for part in row["name"].split(",")]
    #             record = {"first": last, "last": first, "house": row["house"]}
    #             data.append(record)


    # except FileNotFoundError:
    #     print(f"Could not read {read_file}")
    #     sys.exit(1)



    # with open(write_file, "w", newline="") as file:
    #     writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    #     writer.writeheader()
    #     writer.writerows(data)

    try:
        with open(read_file, "r") as read, open(write_file, "w") as write:
            reader = csv.DictReader(read)
            writer = csv.DictWriter(write, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                first, last = [part.strip() for part in row["name"].split(",")]
                record = {"first": last, "last": first, "house": row["house"]}
                writer.writerow(record)



    except FileNotFoundError:
        print(f"Could not read {read_file}")
        sys.exit(1)



if __name__ == "__main__":
    main()
