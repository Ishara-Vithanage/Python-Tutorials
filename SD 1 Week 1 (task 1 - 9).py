print("task -2")
# This is the 2nd task
x = 5
name = "Alice"
print(x)
print(name)


print("-"*10)


print("task -3")
# This is the 3rd task
age = input("Enter your age: ") # Get user age as input
age = int(age) # Converts string value to an integer
print("You are ",age," years old")


print("-"*10)


print("task -4")
# This is the 4th task
first_name = "John"
last_name = "Doe"
full_name = first_name +" "+ last_name
print(full_name)


print("-"*10)


print("task -6")
# This is the 6th task 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operation: ")
# Create if else conditions for each relevent operation
if operator == "+":
    sum = num1 + num2
    print(sum)
elif operator == "-":
    diff = num1 - num2
    print(diff)
elif operator == "*":
    multi = num1*num2
    print(multi)
elif operator == "/":
    div = num1/num2
    print(div)
else:
    print("invalid operaot")


print("-"*10)


# This is the 7th task
print("task -7")
# Get user inputs
name = input("Enter name: ")
age = int(input("Enter age: "))
color = input("Enter favourite color: ")
# Print a greeting message as output
print(f"Hi {name}. You are {age} years old and your favourite color is {color}")


print("-"*10)


# This is the 8th task
print("task -8")
days = int(input("Enter the number of days: ")) # Get the number of days as input
# Hours, minutes and seconds calculations
hours = days*24
minutes = hours*60
seconds = minutes*60
# Print the outputs
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")


print("-"*10)


# This is the 9th task
print("task -9")
# Get user inputs
principal = float(input("Enter pricipal amount: "))
rate_of_interest = float(input("Enter interest ratein %: "))
time = float(input("Enter time: "))
# Calculate simple interest
simple_interest = principal*rate_of_interest*time/100
print(simple_interest)


