print("-"*10)
print("Exercise 03")

lap_num = int(input("How many laps: ")) # First input to get the number of laps
count = 1
lap_time = 0 # Time spent to finish all the laps
max_time = 0 # Max time spent for a lap
min_time = 9999 # Min time spent for a lap

for i in range(lap_num):
    time_each = int(input(f"Ënter lap time {count} of {lap_num}: "))
    if time_each > max_time:
        max_time = time_each
    if time_each < min_time:
        min_time = time_each
    lap_time += time_each # each lap time add to lap_time
    count += 1

print(f"Fastest lap time: {min_time}")
print(f"Slowest lap time: {max_time}")
print(f"Average lap time {lap_time/lap_num}")