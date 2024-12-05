# Q. Find frequency/ Occurance of each letter in given string

string = "Paras waral"
string1 = string.replace(" ", "").lower()

# Method - 1: Using python dictionary to count the frequency
frequency = {}

for i in string1:
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency[i] += 1

sorted_frequecy = dict(sorted(frequency.items()))
print(sorted_frequecy)


# Method - 2: Built in counter import from collections
from collections import Counter

frequency = Counter(string1)

# print(dict(sorted(frequency.items())))
