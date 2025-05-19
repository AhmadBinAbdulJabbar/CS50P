import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", default=1, type=int, help="number of times to meow")
args = parser.parse_args()

# for _ in range(int(args.n)):
#     print("meow")


for _ in range(args.n):
    print("meow")



