#import pipeline
from transformers import pipeline

# Load Summarization Model
summerizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

#Input text
text = input("Enter a long paragraph:\n")

#Generate Summary

summary = summerizer(
    text,
    max_length = 20,
    min_length = 5,
    do_sample = False
)


print("\nOriginal Text: ")
print(text)

print("\nSummary:\n")
print(summary[0]["summary_text"])

