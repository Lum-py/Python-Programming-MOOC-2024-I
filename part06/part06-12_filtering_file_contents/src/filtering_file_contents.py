# Write your solution here
def filter_solutions():
    correct = []
    incorrect = []
    with open("solutions.csv") as file:
       
        for line in file:
            parts = line.strip().split(";")
            name = parts[0]
            calculation = parts[1]
            result = int(parts[2])

            calc_result = eval(calculation)
            if calc_result == result:
                correct.append([name, calculation, result])
            else:
                incorrect.append([name, calculation, result])

    with open("correct.csv", "w") as file:
        for name in correct:
            line = ""
            for value in name:
                line += f"{value};"
            line = line[:-1]
            file.write(line+"\n")

    with open("incorrect.csv", "w") as file:
        for name in incorrect:
            line = ""
            for value in name:
                line += f"{value};"
            line = line[:-1]
            file.write(line+"\n")
    
if __name__ == "__main__":
    filter_solutions()