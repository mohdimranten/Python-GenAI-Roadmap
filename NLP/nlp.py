text = "I Love Python"
print(text.lower())

# Remove Punctuation
import string

text = "Hello!!! Welcome."
translator = str.maketrans("","", string.punctuation)
clean_text = text.translate(translator)
print(clean_text)

# tokenization
text = "I love learning NLP"

tokens = text.split()
print(tokens)

# Count Words

text = "Python is easy"
words = text.split()
print(len(words))

# Word Frequnecy
text = "python python ai ai ai ai"
words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word,0) + 1

print(freq)