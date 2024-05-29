# Write your solution here
from datetime import datetime

d = int(input("Day: "))
m = int(input("Month: "))
y = int(input("Year: "))
birth = datetime(y, m, d)
result = datetime(1999, 12, 31) - birth

if y < 2000:
    print(f"You were {result.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
