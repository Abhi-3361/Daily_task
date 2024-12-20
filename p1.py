# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Convert the sentence to lowercase and remove punctuation (e.g., periods)
sentence = sentence.lower().replace('.', '')

# Split the sentence into words using space as a delimiter
words = sentence.split()

# Initialize an empty dictionary to store word counts
word_count = {}

# Loop through each word in the list of words
for word in words:
    if word in word_count:
        # If word already exists in dictionary, increment its count
        word_count[word] += 1
    else:
        # Otherwise, add the word to the dictionary with a count of 1
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(f"'{word}': {count}")
