# Write your solution here
def add_student(students: dict, name: str):
    if name not in students:                                    #if a student doesn't exist:
        students[name] = {"name" : name}                        #add to database

def add_course(students: dict, name: str, course: tuple):
    _, grade = course                                           #"extract" the grade from tuple
    if name in students:
        if grade > 0:                                           #courses should only be added if score > 0
            if "courses" not in students[name]:                 #if the course is new for the student:
                students[name]["courses"] = [course]            #add it to student
            else:
                existing_courses = students[name]["courses"]    #helping variable to store existing course
                for i in range(len(existing_courses)):          #loop true courses 
                    e_course, e_grade = existing_courses[i]     
                    if e_course == course[0]:                   #if course exists  
                        if grade > e_grade:                     #only if the grade is higher
                            existing_courses[i] = course        #the course gets replaced
                        break                
                else:                                           
                    students[name]["courses"].append(course)    #and added to student
    return students

def print_student(students: dict, name: str):
    if name in students:                                        #if searched for student exists
        print(f"{name}:")                                       #print name
        if "courses" in students[name]:                         #if courses are registered
            count = len(students[name]["courses"])
            print(f"", count, "completed courses:")             #print howmany
            x = 0
            for course, grade in students[name]["courses"]:     #and loop 
                print(" ", course, grade)                       #to print each course and grade
                x += grade
            print(f" average grade {x / count :.1f}")           #and the average of the grades
        else: 
            print(" no completed courses")                      #if no courses

    else:
        print(f"{name}: no such person in the database")        #if the person doesn't exist

def summary(students: dict):
    most_courses = 0
    best_average = 0
    most_courses_student = ""
    best_average_student = ""
    
    
    for student, details in students.items():
        if "courses" in details:
            courses = details["courses"]
            course_count = len(courses)

            if course_count > most_courses:                     # Check for the student with the most courses
                most_courses = course_count
                most_courses_student = student

            total_grades = sum(grade for _, grade in courses)   # Calculate the total grades for all completed courses(have to research more about this version)
            
            average_grade = total_grades / max(course_count, 1) # Calculate the average grade, ensuring it's 0 if there are no completed courses

            # Check for the student with the best average grade
            if average_grade > best_average:
                best_average = average_grade
                best_average_student = student

    print("students",len(students))    
    print("most courses completed", most_courses, most_courses_student)
    print("best average grade", best_average, best_average_student)

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)