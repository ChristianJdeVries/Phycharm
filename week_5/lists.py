# string join
week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("".join(week_days))

for day in week_days:
    print(day, "")

for day in week_days:
    print(day, "", end="")
