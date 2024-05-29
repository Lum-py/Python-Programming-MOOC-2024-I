# Write your solution here
year = int(input("Year: "))
year_l = year
while True:    
    year_l += 1
    if year_l % 100 == 0:
        if year_l % 400 == 0:
            break
    elif year_l % 4 == 0:
        break

print(f"The next leap year after {year} is {year_l}")