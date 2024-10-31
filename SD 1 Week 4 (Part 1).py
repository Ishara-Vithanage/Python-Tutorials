print("Question 1")

for i in range(1,6):
    print(i)
    
# ---------------------------------------------------    
print("-"*10)
print("Question 2")

num = 5
while num >= 1:
    print(num)
    num -= 1

# --------------------------------------------------- 
print("-"*10)
print("Question 3")

num = 0
count = 0

while count <= 5:
    num += count
    count += 1

print(num)

# ---------------------------------------------------
print("-"*10)
print("Question 4")

sum = 0
for i in range(2, 11, 2):
    sum += i
    
print(sum)


# ---------------------------------------------------
print("-"*10)
print("Question 5")

sum = 0
while True:
    num = int(input("Enter number: "))
    if num < 0:
        break
    sum += num
    
print(sum)


# ---------------------------------------------------
print("-"*10)
print("Question 6")

num = int(input("Enter number: "))
count = 1
for i in range(1, 11):
    print(f"{num} x {count} = {num*count}")
    count += 1