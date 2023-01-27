# Open the two files and read their contents

with open('file1.txt', 'r') as f1:

  contents1 = f1.read()


with open('file2.txt', 'r') as f2:

  contents2 = f2.read()


# Split the contents into lists of words

words1 = contents1.split()

words2 = contents2.split()


# Convert the lists of words to sets to make it easier to perform set operations

set1 = set(words1)

set2 = set(words2)


# Display the unique words in both files

unique_words = set1.union(set2)

print("Unique words:", unique_words)


# Display the words that appear in both files

common_words = set1.intersection(set2)

print("Words in both files:", common_words)


# Display the words that appear in the first file but not the second

words_in_first_only = set1.difference(set2)

print("Words in first file only:", words_in_first_only)


# Display the words that appear in the second file but not the first

words_in_second_only = set2.difference(set1)

print("Words in second file only:", words_in_second_only)


# Display the words that appear in either the first or second file, but not both

words_in_either_only = set1.symmetric_difference(set2)

print("Words in either file only:", words_in_either_only)