# Income tax calculation
print("Income tax calculation")
income = int(input("Enter your income: "))

if income > 150000:
    tax_owed = income*(45/100)
    net_income = income - tax_owed
    print(f"Your income tax is {tax_owed} and your net income is {net_income}")

elif 150000 >= income > 50000:
    tax_owed = income*(40/100)
    net_income = income - tax_owed
    print(f"Your income tax is {tax_owed} and your net income is {net_income}")
    
elif 50000 >= income > 12500:
    tax_owed = income*(20/100)
    net_income = income - tax_owed
    print(f"Your income tax is {tax_owed} and your net income is {net_income}")
    
else:
    net_income = income
    print(f"Your net income is {net_income} hence you don't need to pay income taxes.")
    

# -------------------------------------------------------------------------------------------
# Advance grade calculation system
print("Advance grade calculation system")

# Get user inputs
coursework = int(input("Enter coursework mark: "))
midterm_exam = int(input("Enter midterm exam mark: "))
final_exam = int(input("Enter final exam mark: "))

# Validate marks and calculation process
if 0 <= coursework <= 100:
    if 0 <= midterm_exam <= 100:
        if 0 <= final_exam <= 100:
            final_marks = coursework*(40/100) + midterm_exam*(25/100) + final_exam*(35/100)
        else:
            print("Invalid marks")
    else:
        print("Invalid marks")
else:
    print("Invalid marks")
    
# Assign grades
if 70 <= final_marks <= 100:
    print(f"Your final score: {final_marks} \nYour grade: A")
elif 50 <= final_marks <= 69:
    print(f"Your final score: {final_marks} \nYour grade: B")
elif 40 <= final_marks <= 49:
    print(f"Your final score: {final_marks} \nYour grade: C")
else:
    print(f"Your final score: {final_marks} \nYour grade: F")
    