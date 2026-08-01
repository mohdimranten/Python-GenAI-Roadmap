import nltk
nltk.download("stopwords")

#import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import string



#Load dataset

df = pd.read_csv("spam.csv", encoding="latin-1")

print(df.head())

df = df[['v1','v2']]
df.columns = ['label','message']
print(df.head())

# Text Preprocessing
stopwords = set(stopwords.words("english"))

def preprocess(text):
    text = text.lower()
    text = text.translate(
       str.maketrans("","",string.punctuation)
    )
    words = text.split()
    words = [
        words
        for word in words
        if word not in stopwords
    ]
        
   
    return " ".join(words)

df["message"] = df["message"].apply(preprocess)

df["label"] = df["label"].map({

    "ham":0,

    "spam":1

})

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["message"])

y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)

model = MultinomialNB()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(

    y_test,

    predictions

)

print("Accuracy:", accuracy)

email = [

    "Congratulations! You have won a free iPhone."

]

email = [preprocess(email[0])]

vector = vectorizer.transform(email)

prediction = model.predict(vector)

if prediction[0] == 1:

    print("Spam Email")

else:

    print("Ham Email")