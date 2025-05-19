import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b(um|Um)\b"
    match = re.findall(pattern, s)

    # print(match)
    if match:
        return len(match)
    else:
        return 0





if __name__ == "__main__":
    main()
