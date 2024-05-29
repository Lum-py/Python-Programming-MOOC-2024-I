
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data= "exam_points1.csv"

students = {}
with open(student_info) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

Exercises = {}
with open(exercise_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        grade = 0
        for i in parts[1:]:
            grade += int(i)        
        Exercises[parts[0]] = grade    

exam = {}
with open(exam_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        points = 0
        for i in parts[1:]:
            points += int(i)        
        exam[parts[0]] = points

print(f"{'name':<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade"}")

for id, name, in students.items():
    if id in Exercises:
        grade = Exercises[id] // 4
    if id in exam:
        points = exam[id]


    limits = [14, 17, 20, 23, 27, 40]
    for i in range(len(limits)):
        if grade + points <= limits[i]:
            result = i
            break  
    print(f"{name:<30}{Exercises[id]:<10}{grade:<10}{points:<10}{(grade + points):<10}{result}")
    
