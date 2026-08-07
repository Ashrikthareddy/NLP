import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter a sentence: ")

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print("\nWord\tPOS Tag")
for word, tag in tags:
    print(word, "\t", tag)