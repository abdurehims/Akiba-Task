
n = int(input("Enter a positive number: "))

even = 0
odd = 0
total = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    total += number

print("Even:", even)
print("Odd:", odd)
print("Sum:", total)
