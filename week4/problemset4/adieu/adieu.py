import inflect

def main():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
        except EOFError:
            print()
            break
        else:
            names.append(name)


    line = "Adieu, adieu, to "

    p = inflect.engine()
    names_str = p.join(names)
    print(line + names_str)



main()
