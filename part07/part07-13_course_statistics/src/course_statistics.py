# Write your solution here
import urllib.request
import json
def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    course_data = json.load(my_request)
    courses = []
    for course in course_data:
        if course["enabled"] == True:
            courses.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))

    return courses

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    courses = json.load(my_request)    
    students = []
    total_hours = 0
    total_exercises = 0
    weeks = len(courses)
    for stats in courses.values():
        total_hours += stats["hour_total"]
        total_exercises += stats["exercise_total"]
        students.append(stats["students"])
    hr_average = total_hours // max(students)
    ex_average = total_exercises // max(students)

    course_data = {
                    'weeks': weeks,
                    'students': max(students),
                    'hours': total_hours,
                    'hours_average': hr_average,
                    'exercises': total_exercises,
                    'exercises_average': ex_average
                    }
    return course_data


if __name__ == "__main__":
    #retrieve_all()
    retrieve_course("docker2019")