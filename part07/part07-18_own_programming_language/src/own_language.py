from string import ascii_uppercase
def run(program):    
    values = {char: 0 for char in ascii_uppercase}
    output = []

    def jump(parts):
        index = 0
        for line in program:
            if line.strip() == f"{parts[-1]}:":
                return index
            index += 1   
    
    def if_statement(parts):
        number1 = int(parts[1]) if parts[1].isnumeric() else values[parts[1]]
        number2 = int(parts[3]) if parts[3].isnumeric() else values[parts[3]]
        return jump(parts) if eval(f"{number1} {parts[2]} {number2}") else None
 
    i = 0
    while i < len(program):
        line = program[i]
        parts = line.split()
        command = parts[0]
        if command == "END":
            break
        if command in ["JUMP", "IF"]:
            if command == "JUMP":
                jump_to = jump(parts)
            else:
                jump_to = if_statement(parts)
            if jump_to:
                i = jump_to - 1 

        if command in ["MOV", "PRINT", "ADD", "SUB", "MUL"]:
            number = int(parts[-1]) if parts[-1].isnumeric() else values[parts[-1]]
            if command == "MOV":
                values[parts[1]] = number
            if command == "PRINT":
                output.append(number)
            if command == "ADD":
                values[parts[1]] += number
            if command == "SUB":
                values[parts[1]] -= number
            if command == "MUL":
                values[parts[1]] *= number
        i +=1
    return output
       

if __name__ == "__main__":   
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
    
  
    '''
    def move(parts):
        variables[parts[1]] = int(parts[-1]) if parts[-1].isnumeric() else variables[parts[-1]]

    def output_value(parts):
        output.append(int(parts[-1])) if parts[-1].isnumeric() else output.append(variables[parts[-1]])
    
    def add(parts):
        number = int(parts[-1]) if parts[-1].isnumeric() else variables[parts[-1]]
        variables[parts[1]] += int(number)

    def subtract(parts):
        number = int(parts[-1]) if parts[-1].isnumeric() else variables[parts[-1]]
        variables[parts[1]] -= int(number)

    def multiply(parts):
        number = int(parts[-1]) if parts[-1].isnumeric() else variables[parts[-1]]
        variables[parts[1]] *= int(number)
    
    def jump(parts):
        dest = f"{parts[-1]}:"
        index = 0
        for line in program:
            if line.strip() == dest:
                return index
            index += 1   
    
    def if_statement(parts):
        number1 = int(parts[1]) if parts[1].isnumeric() else variables[parts[1]]
        number2 = int(parts[3]) if parts[3].isnumeric() else variables[parts[3]]
        equation = parts[2]
        if eval(f"{number1} {equation} {number2}"):
            jump_to = jump(parts)
            if jump_to:
                return jump_to'''