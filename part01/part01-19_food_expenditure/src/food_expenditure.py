# Write your solution here
amount = int(input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))
weekly = amount * lunch + groceries

print("\nAverage food expenditure:")
print(f"Daily: {weekly / 7} euros")
print(f"Weekly: {weekly} euros")