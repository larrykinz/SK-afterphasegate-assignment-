import random
numbers = []


for i in range(10):
    num = random.randint(1, 50)

    numbers.append(num)
print(f'list of 10 numbers beetween 1-50 numbers : {numbers}')
count = 0
for number in numbers:
    count += 1

print(f'length of list : {count}')

CONSTANT = 0
even_sum = 0
for i in range(len(numbers)):
    if i % 2 == CONSTANT:
        even_sum += numbers[i]

print(even_sum)
odd_sum = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        odd_sum += numbers[i]

print(odd_sum)

multiplied_element = 1
for i in range(len(numbers)):
    if (i + 1) % 3 == 0:
        multiplied_element *= numbers[i]

print(multiplied_element)

sum = 0
for number2 in numbers:
    sum += number2

average = sum / len(numbers)

print(average)

largest = numbers[0]
for number3 in numbers:
    if number3 > largest:
        largest = number3

print(largest)

smallest = numbers[0]
for number4 in numbers:
    if number4 < smallest:
        smallest = number4

print(smallest)










