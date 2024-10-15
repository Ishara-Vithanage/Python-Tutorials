import math

print("task 5")
# This is task 5
# Grade calculator

# Get marks as inputs
mark_1 = int(input("Enter the marks of 1st subject: "))
mark_2 = int(input("Enter the marks of 2nd subject: "))
mark_3 = int(input("Enter the marks of 3rd subject: "))
mark_4 = int(input("Enter the marks of 4th subject: "))
mark_5 = int(input("Enter the marks of 4th subject: "))

# Calculations
avg = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5)/5
print(avg)

# Decide grade
if 100 >= avg > 35:
    if avg >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")
    



print("-"*10)
print("task 6")
# This is task 6
# Savings Goal Tracker

# Get user inputs
target_amt = int(input("Enter target saving amount: "))
current_amt = int(input("Enter current amount: "))
monthly_amt = int(input("Enter monthly saving amount: "))

# Calculations
remain_months = (target_amt - current_amt)/monthly_amt
print(f"You need to save {remain_months} more month/s to achieve the target saving.")



print("-"*10)
print("task 7")
# This is taks 7
# Distance between two points

# Get user inputs
x1 = int(input("Enter x value of first point: "))
y1 = int(input("Enter y value of first point: "))
x2 = int(input("Enter x value of second point: "))
y2 = int(input("Enter y value of second point: "))

# Calculation
dist = math.sqrt((x1-x2)**2+(y1-y2)**2)

# Display output
print(f"Distance is {dist}")

