import sys

class Student:
    def __init__(self, name, house):
        self.name  = name
        self.house = house

    def __str__(self):
        # return "a student"
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    # print(repr(student))
    # student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student
    # try:
    #     Student(name, house)
    # except ValueError:
    #     ...


if __name__ == "__main__":
    main()

