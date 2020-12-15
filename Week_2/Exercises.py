print(5 % 2)
print(12%15)
print(0%7)

print((14+51)%24)

current_time_str = input("What is the time now?")
current_time_int = int(current_time_str)
waiting_time_str = input("How long do you have to wait?")
waiting_time_int = int(waiting_time_str)

time_after = (current_time_int+waiting_time_int) % 24

print("After the waiting time, it is", time_after, "O'clock")
