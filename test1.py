file = open("student_info.txt", "w")

file.write("2023001\n")
file.write("2023002\n")
file.write("2023003\n")
file.write("2023004\n")
file.write("2023005\n")

file.close()

file = open("student_info.txt", "a")

file.write("2023006\n")
file.write("2023007\n")
file.write("2023008\n")
file.write("2023009\n")

file.close()

file = open("student_info.txt", "r")

for line in file:
    print(line.strip())

file.close()
