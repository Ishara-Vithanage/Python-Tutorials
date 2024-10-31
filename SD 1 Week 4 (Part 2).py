print("Question 7")

count = 1
product = 1
num = int(input("Enter number: "))
while count <= num:
    product = product*count
    count+=1
    
print(f"Factorial of the entered number is {product}")


# --------------------------------------
print("-"*10)
print("Question 8")

for num in range(2, 20):
    fact = 0 # fact use to check how many factors has the number.
    for divid in range(1, num +1): # without +1, it neglects the second factor.
        if num % divid == 0:
            fact += 1
    if fact <= 2: # Prime numbers only have two factors
        print(num)

# --------------------------------------
print("-"*10)
print("Question 9")

for i in range(1, 6):
    print(str(i)*i)




