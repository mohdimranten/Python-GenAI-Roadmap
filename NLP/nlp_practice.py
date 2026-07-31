# Mini Practice
# Write Python programs to:

# Convert text to lowercase.
text = input("Enter the Text: ")
print("Output is: ",text.lower())

# Count the total number of words.
text = input("Enter the Text: ")
words = text.split()
print("Total number of words is: ",len(words))

# Count the number of characters.
sentence = input("Enter a sentence: ")

count = len(sentence)

print("Total characters:", count)

# Remove punctuation from a sentence.
import string
text = "Hello !!!! World."
traslator = str.maketrans("","",string.punctuation)
clean_text = text.translate(traslator)
print(clean_text)

# Split a sentence into words.
text = input("Enter the sentence: ")
split_text = text.split()
print(split_text)

# Count the frequency of each word.
text = input("Enter the Text: ")
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word,0) + 1

print(freq)    

# Reverse the order of words in a sentence.
sentence = input("Enter a sentence: ")

reversed_sentence = " ".join(sentence.split()[::-1])

print("Reversed sentence:", reversed_sentence)
# Find the longest word in a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words,key=len)
print("Longest word: ",longest_word)
print("Length: ", len(longest_word))

# Remove duplicate words while preserving order.
sentence = input("Enter a sentence for remove duplicate record: ")
words = sentence.split()
result = []

for word in words:
    if word not in result:
        result.append(word)

print(" ".join(result))        
# Check whether a word exists in a sentence.

sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")

if word in sentence.split():
    print("Word found.")
else:
    print("Word not found.")