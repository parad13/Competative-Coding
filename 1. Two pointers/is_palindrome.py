# Palindrome is a string 
strings = ["{()-()}", "()() ", "1002001", "Nitin ", "test", "abba"]

# # try1 - simply using pythons inbuilt function for string reversal
# # try1 - step1
# def is_palindrome(string):
#     string = string.strip(" ").lower()
#     # try1 - step2
#     return "{} is Palindrome".format(string) if string == string[::-1] else "{} is not a palindrome".format(string)

# try2 - with classic method using 2 pointer pattern
def is_palindrome(string):
    string = string.strip(" ").lower()
    str_last_letter_index = len(string)-1
    for i in range(0, len(string)):
        a, b = string[i], string[str_last_letter_index]
        if string[i] == string[str_last_letter_index]:
            if(string[i] == string[str_last_letter_index] and i == str_last_letter_index):
                # print("Palindrome")
                return "Palindrome: " + string
            str_last_letter_index -= 1
        else:
            # print("not a palindrome")
            return "Not a Palindrome: " + string

for string in strings:
    print(is_palindrome(string))

# method3
def is_even_palindrome(s):
    # Check if the length of the string is even
    if len(s) % 2 != 0:
        return False  # Not an even-length string
    
    # Initialize two pointers
    left = len(s) // 2 - 1  # Start at the middle-left
    right = len(s) // 2  # Start at the middle-right
    
    # Compare characters from the middle outwards
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            return False  # Characters don't match, not a palindrome
        left -= 1  # Move left pointer outward
        right += 1  # Move right pointer outward
    
    return True  # All characters matched, it's a palindrome

# Example usage:
s = "abccba"  # Even-length palindrome
if is_even_palindrome(s):
    print(f'"{s}" is an even-length palindrome.')
else:
    print(f'"{s}" is not an even-length palindrome.')
