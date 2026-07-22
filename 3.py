import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

ps = PorterStemmer()

text = input("Enter a sentence: ")

words = nltk.word_tokenize(text)

print("\nWord\tStem")
for word in words:
    print(word, "\t", ps.stem(word))