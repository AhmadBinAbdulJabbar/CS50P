import validators


def main():
    email = input("What's your email address? ").strip()
    print(check_email(email))


def check_email(e):
    valid = validators.email(e)
    if valid:
        return "Valid"
    else:
        return "Invalid"



if __name__ == "__main__":
    main()


