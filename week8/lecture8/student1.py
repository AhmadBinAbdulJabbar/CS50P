import sys

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            # print("Missing Name")
            # sys.exit()
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name  = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        # return "a student"
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🏒"


def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    # print(repr(student))
    print(student)
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name, house, patronus)
    return student
    # try:
    #     Student(name, house)
    # except ValueError:
    #     ...


if __name__ == "__main__":
    main()



