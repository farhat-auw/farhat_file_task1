file = open("students.csv", "w")

file.write("Name, Age, Course\n")

file.write("Alice Smith, 20, Mathematics\n")
file.write("Bob Johnson, 21, Physics\n")
file.write("Charlie Lee, 19, Computer Science\n")

file.close()

file = open("students.csv", "r")

lines = file.readlines()

file.close()

for line in lines[1:]:
    data = line.strip().split(",")
    student_name = data[1]
    student_age = data[2]

    print(f"{student_name} age is {student_age}")
