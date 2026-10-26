text = "Python is useful and Python is powerful."
text = text.lower()

for p in ".,!?":
    text = text.replace(p, "")

words = text.split()
counts = {}

vowels = 0
consonants = 0
characters = text.replace(" ", "")
longest = ""

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

    if len(word) > len(longest):
        longest = word

for letter in characters:
    if letter in "aeiou":
        vowels += 1
    elif letter.isalpha():
        consonants += 1

repeated = []

for word in counts:
    if counts[word] > 1:
        repeated.append(word)

top_five = sorted(counts, key=counts.get, reverse=True)[:5]

print("Words:", len(words))
print("Characters:", len(characters))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Longest word:", longest)
print("Word counts:", counts)
print("Repeated words:", repeated)
print("Top five:", top_five)