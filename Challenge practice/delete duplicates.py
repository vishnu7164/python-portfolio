# Using inbuilt method to remove duplicates with in built method

numbers = [3,6,3,14,6,8,2,10,14,3,2,6]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

# Remove duplicate values without using inbuilt method
# counter variable is created to keep looping inner loop until the duplicate values are deleted

numbers = [3,6,3,14,6,8,2,10,14,3,2,6]
count = 0
for number in numbers:
    count = numbers.count(number)
    if count>1:        
        for counter in range(0,count-1):
            numbers.remove(number)
print(numbers)


# It can also delete duplicate name in the list

name = ["Bob", "John", "Marsh", "balleriene", "Adventurous", "John", "balleriene","Bob","John"]
count = 0
for value in name:
    count = name.count(value)
    if count>1:        
        for counter in range(0,count-1):
            name.remove(value)
print(name)

