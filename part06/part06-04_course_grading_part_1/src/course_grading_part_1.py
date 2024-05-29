# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

students = {}
with open(student_info) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
    #print(students)

grades = {}
with open(exercise_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        grade = 0
        for i in parts[1:]:
            grade += int(i)        
        grades[parts[0]] = grade
    #print(grades)

for id, name in students.items():
    if id in grades:
        grade = grades[id]
        print(f"{name} {grade}")


