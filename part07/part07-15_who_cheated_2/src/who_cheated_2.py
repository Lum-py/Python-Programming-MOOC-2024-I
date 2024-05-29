# Write your solution here
import csv
from datetime import datetime, timedelta
def final_points():
    start_times ={}
    with open("start_times.csv") as start:
        for line in csv.reader(start, delimiter= ";"):
            start_times[line[0]] = datetime.strptime(line[-1], '%H:%M')
    
    submissions = {}
    with open("submissions.csv") as end:
        for line in csv.reader(end, delimiter= ";"):
            student = line[0]
            exercise = line[1]
            grade = line[2]
            time = datetime.strptime(line[-1], '%H:%M')
            if student not in submissions:
                submissions[student] = {exercise: grade}
            if exercise not in submissions[student] or grade > submissions[student][exercise]:
                if time < start_times[student] + timedelta(hours=3):
                    submissions[student][exercise] = grade

        end_score = {}
    for student, exercises in submissions.items():        
        total_score = sum(int(exercises[score])for score in exercises)
        end_score[student] = total_score
    #print(end_score)
    return end_score
    





if __name__ == "__main__":
    final_points()