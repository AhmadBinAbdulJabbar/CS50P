import re

def main():
    code = input("Hexadecimal color code: ")
    pattern = r"^#[abcdefABCDEF0123456789]{6}$"
    # pattern = r"#[0-9A-F]"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Match with {match.group()}")
    else:
        print("Invalid.")


if __name__ == "__main__":
    main()

#GGIIKK
#AAAAAA
#AGGGGG
