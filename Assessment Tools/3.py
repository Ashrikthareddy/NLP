from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = input("Enter words separated by space: ").split()

print("\nWord\tLemma")
for word in words:
    print(word, "\t", lemmatizer.lemmatize(word))