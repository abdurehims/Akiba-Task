number = int(input("Enter the number to check: "))
is_prime = True


if number <= 1:
 is_prime =False

else:
 for n in range(2, int(number ** 0.5)+1):
  if number % n == 0:
   is_prime =False
   break
   
if is_prime ==False:
 print("Not prime")
else:
 print("Prime")
