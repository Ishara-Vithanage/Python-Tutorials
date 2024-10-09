print("This is task 10")
# Temperature Conversion
temp = int(input("Enter temperature in Celsius: ")) # Get the input temperature
fa_value = (temp*9/5)+32 # Convert Celsius value to Farenhite
print(f"Farenhite value: {fa_value}")


print("-"*10)


print("This is task 11")
# Grocery bill estimator
# Get user inputs
item_1 = float(input("Enter value of item 1: "))
item_2 = float(input("Enter value of item 2: "))
item_3 = float(input("Enter value of item 3: "))
# Output sum value
sum = item_1 + item_2 + item_3
print(f"Total value is {sum}")


print("-"*10)


print("This is task 12")
#Distance converter
distance_m = int(input("Enter distance in meter: ")) # Get input distance
# Convert it into kilometers and to miles
distance_km = distance_m/1000
distance_mil = distance_km/1.60934
# Print the output
print(f"Distance in kilometers and miles aocordingly {distance_km}, {distance_mil}")


print("-"*10)


print("This is task 13")
# BMI Calculator
# Get user weight and height as inputs
weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
# Calculate BMI value
bmi = weight/(height**2)
# Print the output
print(f"Your BMI is {bmi}")
