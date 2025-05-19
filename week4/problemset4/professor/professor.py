import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)

        ans = x + y

        tries = 3
        while tries > 0:
            try:
                z = int(input(f"{x} + {y} = ").strip())
                if z == ans:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                tries -= 1
                print("EEE")

        if tries == 0:
            print(f"{x} + {y} = {ans}")

    print(f"Score: {score}")




def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level < 1 or level > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            break

    return level

def generate_integer(level):
    start = pow(10, level - 1)
    if level == 1:
        start -= 1
    end = pow(10, level) - 1
    rand = random.randint(start, end)
    return rand


if __name__ == "__main__":
    main()
