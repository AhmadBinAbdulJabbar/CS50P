# with open("students.csv") as file:
#     for line in sorted(file, reverse=True):
#         # row = line.rstrip().split(",")
#         name, house = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         print(f"{name} is in {house}")

# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)


# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]


# def get_house(student):
#     return student["house"]


# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key=lambda student: student["name"], reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key=get_house, reverse=True):
#     print(f"{student['name']} is in {student['house']}")


# import csv

# students = []


# with open("address.csv") as file:
#     # reader = csv.reader(file)
#     # for row in reader:
#     #     students.append({"name": row[0], "home":row[1]})
#     # for name, home in reader:
#     #     students.append({"name": name, "home":home})

#     reader = csv.DictReader(file)
#     # for row in reader:
#     #     students.append({"name": row["name"], "home":row["home"]})
#     for row in reader:
#         students.append(row)



# for student in sorted(students, key=lambda student: student["name"], reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key=lambda student: student["name"], reverse=True):
#     print(f"{student['name']} is in {student['home']}")

# import csv

# name = input("What's your name? ").strip()
# home = input("Where's your home? ").strip()

# with open("students1.csv", "a") as file:
#     # writer = csv.writer(file)
#     # writer.writerow([name, home])
#     # writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     # writer.writerow({"name": name, "home": home})
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"home": home, "name": name})


 