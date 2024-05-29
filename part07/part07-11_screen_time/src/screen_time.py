from datetime import datetime, timedelta

filename = input("Filename: ")
date = datetime.strptime(input("Starting date: "), '%d.%m.%Y')

days = int(input("Howmany days: "))
with open(filename, "w") as file:
    file.write(f"Time period: {date.strftime('%d.%m.%Y')}-{(date + timedelta(days=days - 1)).strftime('%d.%m.%Y')}\n")

    print("Please type in screen time in minutes on each day (TV computer mobile):")
    total_min = 0
    times = {}
    for _ in range(days):
        t = input(f"Screen time {date.strftime('%d.%m.%Y')}: ").split(" ")
        total_min += sum(map(int, t))
        times[date] = f"{t[0]}/{t[1]}/{t[2]}"
        date += timedelta(days=1)

    file.write(f"Total minutes: {total_min}\n")
    file.write(f"Average minutes: {total_min / days}\n")

    for key, value in times.items():
        file.write(f"{key.strftime('%d.%m.%Y')}: {value}\n")
print(f"Data stored in file {filename}")
