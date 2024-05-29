# Write your solution here
from datetime import datetime, timedelta
import csv
def read_files(filename: str):
    student_file = {}
    with open(filename) as file:
        for line in csv.reader(file, delimiter= ";"):
            student = line[0]
            time = datetime.strptime(line[-1], '%H:%M')
            if filename != "start_times.csv":
                if student not in student_file or time > student_file[student]: 
                    student_file[student] = time        
            else:
                student_file[student] = time
    return student_file

def cheaters():
    cheater = []
    start_times = read_files("start_times.csv")
    end_times = read_files("submissions.csv")
       
    for name in start_times:
        if name in end_times:
            if end_times[name] > start_times[name] + timedelta(hours=3):
                cheater.append(name)
    return cheater

    
if __name__ == "__main__":
    cheaters()