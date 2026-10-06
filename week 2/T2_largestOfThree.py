
Number1 = float(input("Enter first number: "))
Number2 = float(input("Enter second number: "))
Number3 = float(input("Enter third number: "))

if Number1 == Number2 == Number3:
    print("All are equal")

elif Number1 > Number2:
    if Number1 > Number3:
        print(Number1, "is the largest")
    else:
        print(Number3, "is the largest")

elif Number2 > Number3:
    print(Number2, "is the largest")

else:
    print(Number3, "is the largest")