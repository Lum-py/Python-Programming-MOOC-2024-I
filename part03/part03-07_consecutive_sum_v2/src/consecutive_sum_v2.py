# Write your solution here
number = 1
sum = 1
result = f"The consecutive sum: 1"
limit = int(input("Limit: "))

while sum < limit:
    number += 1
    result += f" + {number}"
    sum += number 
    


print(f"{result} = {sum}")