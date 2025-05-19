from PIL import Image
from PIL import ImageOps
import sys
import os

def main():
    file_extensions = (".jpg", ".jpeg", ".png")
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].lower().endswith(file_extensions) and not sys.argv[2].lower().endswith(file_extensions):
        print("Invalid input")
        sys.exit(1)
    elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
        print("Input and output have different extensions")
        sys.exit(1)


    before_file = sys.argv[1]
    after_file = sys.argv[2]
    try:
        with Image.open(before_file) as before, Image.open("shirt.png") as shirt:
            b_size = before.size
            s_size = shirt.size
            # print(b_size)
            # print(s_size)
            before = ImageOps.fit(before, s_size)
            before.paste(shirt, (0,0), shirt)
            before.save(after_file)


    except FileNotFoundError:
        print("File does not exists")
        sys.exit(1)


if __name__ == "__main__":
    main()
