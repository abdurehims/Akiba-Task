
word = input("Enter the work you want to check: ")
lowerWord = word.lower()
reversed_world = lowerWord[::-1]

if lowerWord == reversed_world:
    print("the Word is Palindrome")
else:
    print("Not Palindrome.")