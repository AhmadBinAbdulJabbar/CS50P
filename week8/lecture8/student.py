# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")


def main():
    # name = get_name()
    # house = get_house()

    # name, house = get_student()
    # print(f"{name} from {house}")

    # student = get_student()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")

    student  = get_student()
    if student['name'] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return name, house
#     # return (name, house)
#     return [name, house]


def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
