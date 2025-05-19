import random

def main():
    n = get_n("Level: ")
    rand = random.randint(1, n)
    guess(rand)
    return


def guess(rand):
    while True:
        g = get_n("Guess: ")
        if g < rand:
            print("Too small!")
        elif g > rand:
            print("Too large!")
        else:
            print("Just right!")
            return


def get_n(prompt):
    while True:
        try:
            n = int(input(prompt).strip())
            if n <= 0:
                raise ValueError
        except ValueError:
            pass
        else:
            return n

if __name__ == "__main__":
  main()
