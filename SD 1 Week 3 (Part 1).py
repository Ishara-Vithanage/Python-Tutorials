print("Task 1")
num = int(input("Enter number: "))
if num % 5 == 0:
    print("Divisable by 5")


print("-"*10)
print("Task 2")
age = int(input("Enter age: "))
if age <= 18:
    print("Not eligible to vote.")
else:
    print("Eligible to vote.")


print("-"*10)
print("Task 3")
num = int(input("Enter number: "))
if num >= 0:
    print("Positive number")
elif num == 0:
    print("Number is Zero")
else:
    print("Negative number")
    

print("-"*10)
print("Task 4")
num = int(input("Enter number lower than 10: "))
if num < 10:
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Please enter a number lower than 10")
    
    
print("-"*10)
print("Task 5")
year = int(input("Enter year: "))
if year % 4 == 0:
    print("Entered year is a leap year.")
else:
    print("Entered year is not a leap year.")
    

print("-"*10)
print("Task 6")
letter = input("Enter a letter (in lowercase): ")

if letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
    
    
print("-"*10)
print("Task 7")
char = input("Enter character: ")
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
elif char.isalnum():
    print("Special character")
else:
    print("Number")
    
    
print("-"*10)
print("Task 8")
amount = int(input("Enter purchased amount: "))
if amount <= 1000:
    if amount >= 500:
        disc = amount*(5/100)
        print(f"Discount is {disc}")
    else:
        print("No discount")
else:
    disc = amount*(10/100)
    print(f"Discount is {disc}")

    
