class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        # self.name = name
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        # self.name = name
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
print(student.name)
