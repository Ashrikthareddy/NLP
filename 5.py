from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = input("Enter words separated by space: ").split()

print("\nWord\tStem")
for word in words:
    print(word, "\t", ps.stem(word))