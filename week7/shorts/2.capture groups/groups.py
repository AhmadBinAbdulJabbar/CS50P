import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    # pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)

    if match:
        # country_code = match.group(1)
        country_code = match.group("country_code")
        print(country_code)
        print(locations[country_code])
        print("valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()


# +1 617-495-1000
# +505 617-495-1000
# +62 617-495-1000
