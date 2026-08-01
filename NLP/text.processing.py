import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# import nltk

# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('wordnet')

# # Word tokenization

# from nltk.tokenize import word_tokenize
# text = "I love learning NLP."
# tokens = word_tokenize(text)
# print(tokens)

# # Sentence Tokenization
# from nltk.tokenize import sent_tokenize
# text = "Python is easy. AI is amazing."
# sentences = sent_tokenize(text)
# print(sentences)


# from nltk.corpus import stopwords

# stop_words = stopwords.words("english")

# print(stop_words[:20])

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("I love learning NLP.")

for token in doc:
    print(token.text)