c = 300000000

def main():
    mass = int(input("m: "))
    print(f"E: {energy(mass)}")

def energy(m):
    global c
    e = m * (c ** 2)
    return e

main()
