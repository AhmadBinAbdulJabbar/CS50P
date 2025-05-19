from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()


def main():
    font_list = figlet.getFonts()
    argument_list_length = len(sys.argv)
    if argument_list_length < 2:
        f = choice(font_list)
        figlet.setFont(font=f)

    elif (
        argument_list_length == 3
        and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
        and sys.argv[2] in font_list
    ):
        figlet.setFont(font=sys.argv[2].strip().lower())

    else:
        sys.exit("Invalid usage")

    text = input("Input: ").strip()
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
