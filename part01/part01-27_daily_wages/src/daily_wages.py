# Write your solution here
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
if day.lower() == "sunday":
    wage *= 2

result = wage * hours

print(f"Daily wages: {result} euros")