
# import spacy

# nlp = spacy.load("en_core_web_sm")
# text = "I Love Learning NLP"

# doc = nlp(text.lower())

# for token in doc:
#     print(token.text)

import spacy
nlp = spacy.load("en_core_web_sm")
text = input("Enter a text: ")
doc = nlp(text.lower())
for token in doc:
    print(token.text)