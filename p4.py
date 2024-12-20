# Given string
string = "Welcome to python Training"

# Define a string containing vowels
vowels = "aeiouAEIOU"

# Initialize a counter for vowels
vowel_count = 0

# Initialize an empty string to store the vowels found
vowel_found = ""

# Iterate through each character in the string
for char in string:
    if char in vowels:
        vowel_count += 1
        vowel_found += char + " "

# Display the count and the vowels found
print(f"Vowels in the string: {vowel_found}")
print(f"Total number of vowels: {vowel_count}")
