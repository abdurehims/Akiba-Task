largest = None
smallest = None
total = 0
even = 0
odd = 0

for n in range(10):
    number = int(input("Enter the number: "))

    if largest == None or number > largest:
     largest = number

    if smallest is None or number < smallest:
     smallest = number

    if number % 2 == 0:
      even +=1

    else:
      odd+=1

    total+=number
    
average = total / 10
print(f"largest: {largest}, smallest: {smallest}, total: {total}, average: {average}, even: {even},  odd: {odd}")