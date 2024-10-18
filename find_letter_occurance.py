# string = input("Enter a string to find its letter occurance: ") # Drawback, not reading input from same line, reading it from bottom line

# For CPH testing
string = input("")


letter_counts = {}

for letter in string.replace(" ", ""):
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print(letter_counts)
print("i" in letter_counts)
