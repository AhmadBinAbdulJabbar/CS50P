def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not is_first_two_letters(s[:2]):
        return False

    if not is_valid_length(s):
        return False

    if not s.isalnum():
        return False


    if not is_valid_sequence(s):
        return False

    return True



def is_first_two_letters(s):
    for c in s:
        if c.isdigit():
            return False

    return True


def is_valid_length(s):
    if len(s) > 6 or len(s) < 2:
        return False

    return True


def is_valid_sequence(s):
    is_num = False

    for c in s:
        if c.isdigit():
            if c == "0" and is_num == False:
                return False
            is_num = True
        elif is_num:
            return False

    return True



main()
