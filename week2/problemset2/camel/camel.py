def main():
    camel_case = input("camelCase: ").strip()
    snake_case = ""
    for ch in camel_case:
        if ch.isupper():
            snake_case += "_"
            snake_case += ch.lower()
        else:
            snake_case += ch

    print("snake_case:", snake_case)

main()
