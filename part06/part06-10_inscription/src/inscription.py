# Write your solution here
name = input("Whom should I sign this to:")
filename = input("where shall i save it: ")
with open(filename, "w") as new_file:
    new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")