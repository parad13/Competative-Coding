def is_palindrome(string):
    # Remove non-alphanumeric chars, whitespace at start & end and convert to lowercase
    cleaned_string = string.strip().lower()
    # cleaned_string = ''.join(char.lower() for char in string if char.isalnum()) # Removing non-alphanumeric chars

    # Python string reverse [::-1] 
    return cleaned_string == cleaned_string[::-1]

    # Two pointers technique
    # Initialize two pointers
    left, right = 0, len(cleaned_string) - 1

    # Use two-pointers technicque to check palindrome
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1

    return True




string = "   nitiN   "
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

