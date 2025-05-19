import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"^<iframe[^>]+src=\"https?://(?:www\.)?youtube\.com/embed/(?P<link>\w+)\"[^>]*></iframe>$"

    match = re.search(pattern, s)
    # print(match.groups())
    if match:
        return f"https://youtu.be/{match.group("link")}"
    else:
        return None


if __name__ == "__main__":
    main()
