# Write your solution here
def grade_input():
    exam_points = []
    exercise_points = []
    total_points = []

    while True:
        usr_input = input("Exam points and exercises completed: ")
        if usr_input == "":
            break
        usr_input = usr_input.split(" ")
        exam_points.append(int(usr_input[0]))
        exercise_points.append(int(usr_input[-1]))

    for i in range(len(exercise_points)):
        total_points.append(convert_points(exercise_points)[i] + exam_points[i])

    return total_points, exam_points


def convert_points(exercise_points: list):
    return [i // 10 for i in exercise_points]
  

def create_grades(total_points: list, exam_points: list):
    grades = []
    limits = [14, 17, 20, 23, 27, 30]
    for i in range(len(total_points)):
        if exam_points[i] < 10:
            grades.append(0)
        else:
            for j in range(len(limits)):
                if total_points[i] <= limits[j]:
                    grades.append(j)
                    break
    return grades


def statistics(total_points: list, exam_points: list):
    print("Statistics:")
    print(f"Points average: {sum(total_points) / len(total_points) :.1f}")
    
    grade_count = create_grades(total_points, exam_points)
    count = 0
    for i in grade_count:
        if i != 0:
            count += 1
    print(f"Pass percentage: {(count / len(total_points)) * 100 :.1f}")

    print("Grade distribution:")
    for grade in range(5, -1, -1):
        print(f"{grade}: {grade_count.count(grade) * "*"}")


total_points, exam_points = grade_input()
statistics(total_points, exam_points)
